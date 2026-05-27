#!/usr/bin/env python3
"""
aifreeplan.com 内容发布流水线（四步）

步骤：
  1. 质检 (quality_gate.py)    — 模式匹配检查：虚假产品描述、过时模型名、缺字段
  2. 核查 (fact_check.py)      — 事实核查：关键数字与可信数据源交叉验证
  3. 构建 (npx astro build)    — 生成静态HTML
  4. 部署 (git push)           — 推送到deploy-static分支

用法：
  python3 scripts/publish_pipeline.py                    # 完整流水线
  python3 scripts/publish_pipeline.py --skip-deploy      # 跳过部署（只质检+核查+构建）
  python3 scripts/publish_pipeline.py --check-only       # 只做质检+核查
  python3 scripts/publish_pipeline.py --slug xxx         # 只检查指定文章
"""
import subprocess
import sys
import os
import shutil
import tempfile

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)

def run_step(name, cmd, cwd=PROJECT_DIR, critical=True):
    """执行流水线步骤"""
    print(f"\n{'='*60}")
    print(f"步骤: {name}")
    print(f"{'='*60}")
    
    result = subprocess.run(
        cmd, cwd=cwd, shell=True,
        capture_output=True, text=True, timeout=300
    )
    
    if result.stdout:
        print(result.stdout)
    
    if result.returncode != 0:
        if result.stderr:
            print(f"⚠️  stderr: {result.stderr[:500]}")
        
        if critical:
            print(f"\n❌ {name} 失败（退出码 {result.returncode}），流水线中止")
            return False
        else:
            print(f"\n⚠️  {name} 有警告（退出码 {result.returncode}），继续执行")
    
    return True


def main():
    args = sys.argv[1:]
    skip_deploy = '--skip-deploy' in args
    check_only = '--check-only' in args
    slug = None
    
    if '--slug' in args:
        idx = args.index('--slug')
        if idx + 1 < len(args):
            slug = args[idx + 1]
    
    print("=" * 60)
    print("aifreeplan.com 内容发布流水线")
    print("生成 → 质检 → 核查 → 构建 → 部署")
    print("=" * 60)
    
    # ========== 步骤1：质检 ==========
    quality_cmd = f"python3 {SCRIPT_DIR}/quality_gate.py"
    if not run_step("质检 (quality_gate.py)", quality_cmd, critical=True):
        return 1
    
    # ========== 步骤2：事实核查 ==========
    fact_cmd = f"python3 {SCRIPT_DIR}/fact_check.py"
    if slug:
        fact_cmd += f" --slug {slug}"
    # 事实核查有警告不中止，但会显示
    run_step("事实核查 (fact_check.py)", fact_cmd, critical=False)
    
    if check_only:
        print("\n✅ 质检+核查完成（check-only模式）")
        return 0
    
    # ========== 步骤3：构建 ==========
    build_cmd = "rm -rf dist && npx astro build"
    if not run_step("构建 (astro build)", build_cmd, critical=True):
        return 1
    
    if skip_deploy:
        print("\n✅ 质检+核查+构建完成（skip-deploy模式）")
        return 0
    
    # ========== 步骤4：部署 ==========
    print(f"\n{'='*60}")
    print("步骤: 部署 (deploy-static)")
    print(f"{'='*60}")
    
    # 复制dist到临时目录
    dist_tmp = tempfile.mkdtemp(prefix='aifreeplan_dist_')
    shutil.copytree(os.path.join(PROJECT_DIR, 'dist'), dist_tmp, dirs_exist_ok=True)
    
    deploy_cmds = [
        f"git checkout deploy-static",
        f"rm -rf en zh images *.html *.ico *.svg *.txt *.png robots.txt",
        f"cp -r {dist_tmp}/* .",
        f"git add -A && git commit -m 'deploy: 自动发布'",
        f"git push origin deploy-static",
        f"git checkout main",
    ]
    
    for cmd in deploy_cmds:
        result = subprocess.run(
            cmd, cwd=PROJECT_DIR, shell=True,
            capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0 and 'nothing to commit' not in result.stdout:
            print(f"⚠️  部署步骤失败: {cmd}")
            print(f"   stderr: {result.stderr[:200]}")
            # 恢复到main
            subprocess.run("git checkout main", cwd=PROJECT_DIR, shell=True,
                         capture_output=True, text=True)
            return 1
    
    # 清理临时目录
    shutil.rmtree(dist_tmp, ignore_errors=True)
    
    print("\n✅ 流水线完成：质检 → 核查 → 构建 → 部署")
    print("   Cloudflare Pages 将在 30-60 秒内生效")
    return 0


if __name__ == '__main__':
    sys.exit(main())
