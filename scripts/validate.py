#!/usr/bin/env python3
"""
AIFreePlan 发布前验证脚本
每次部署前必须运行此脚本，确保所有页面符合标准
"""

import glob
import re
import sys
from collections import defaultdict

class WebsiteValidator:
    def __init__(self, root_dir='.'):
        self.root_dir = root_dir
        self.errors = defaultdict(list)
        self.warnings = defaultdict(list)
        
    def validate_all(self):
        """验证所有页面"""
        print("🔍 开始验证 aifreeplan.com 网站...\n")
        
        html_files = glob.glob(f'{self.root_dir}/**/*.html', recursive=True)
        html_files = [f for f in html_files if 'backups' not in f and 'node_modules' not in f]
        
        print(f"📄 找到 {len(html_files)} 个 HTML 文件\n")
        
        for filepath in html_files:
            self.validate_page(filepath)
        
        self.print_report()
        return len(self.errors) == 0
    
    def validate_page(self, filepath):
        """验证单个页面"""
        with open(filepath, 'r', errors='ignore') as f:
            content = f.read()
        
        page_name = filepath.replace(self.root_dir + '/', '')
        
        # 1. HTML 结构检查
        if '<!DOCTYPE html>' not in content[:100]:
            self.errors['HTML结构'].append(f"{page_name}: 缺少 DOCTYPE")
        
        if 'lang="' not in content[:200]:
            self.errors['HTML结构'].append(f"{page_name}: 缺少 lang 属性")
        
        if 'charset=' not in content[:500]:
            self.errors['HTML结构'].append(f"{page_name}: 缺少 charset")
        
        if 'viewport' not in content[:1000]:
            self.errors['HTML结构'].append(f"{page_name}: 缺少 viewport")
        
        # 2. SEO 检查
        title_match = re.search(r'<title>([^<]+)</title>', content)
        if not title_match:
            self.errors['SEO'].append(f"{page_name}: 缺少 <title>")
        elif len(title_match.group(1)) < 10:
            self.warnings['SEO'].append(f"{page_name}: title 太短 ({len(title_match.group(1))} 字符)")
        
        desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
        if not desc_match:
            self.errors['SEO'].append(f"{page_name}: 缺少 meta description")
        elif len(desc_match.group(1)) < 50:
            self.warnings['SEO'].append(f"{page_name}: description 太短 ({len(desc_match.group(1))} 字符)")
        
        if 'hreflang' not in content:
            self.errors['SEO'].append(f"{page_name}: 缺少 hreflang 标签")
        
        if 'canonical' not in content:
            self.warnings['SEO'].append(f"{page_name}: 缺少 canonical 标签")
        
        # 3. 可访问性检查
        img_no_alt = re.findall(r'<img(?![^>]*alt=)[^>]*>', content)
        if img_no_alt:
            self.warnings['可访问性'].append(f"{page_name}: {len(img_no_alt)} 个图片缺少 alt 属性")
        
        # 4. 安全检查
        ext_links = re.findall(r'<a[^>]*href="https?://[^"]*"[^>]*>', content)
        for link in ext_links:
            if 'aifreeplan.com' not in link and 'rel=' not in link:
                self.warnings['安全'].append(f"{page_name}: 外部链接缺少 rel 属性")
                break
        
        # 5. 语言版本检查
        if '/zh/' in filepath or filepath.endswith('/zh.html'):
            if '/en/' not in content and 'English' not in content:
                self.warnings['多语言'].append(f"{page_name}: 缺少英文版本链接")
        elif '/en/' in filepath or filepath.endswith('/en.html'):
            if '/zh/' not in content and '中文' not in content:
                self.warnings['多语言'].append(f"{page_name}: 缺少中文版本链接")
    
    def print_report(self):
        """打印验证报告"""
        print("=" * 60)
        print("📊 验证报告")
        print("=" * 60)
        
        total_errors = sum(len(v) for v in self.errors.values())
        total_warnings = sum(len(v) for v in self.warnings.values())
        
        if total_errors == 0 and total_warnings == 0:
            print("\n✅ 恭喜！所有页面验证通过！")
            print("\n🚀 可以安全部署了！")
            return
        
        if total_errors > 0:
            print(f"\n❌ 发现 {total_errors} 个错误（必须修复）:")
            print("-" * 40)
            for category, errors in self.errors.items():
                print(f"\n  [{category}]")
                for error in errors[:5]:
                    print(f"    • {error}")
                if len(errors) > 5:
                    print(f"    ... 还有 {len(errors) - 5} 个")
        
        if total_warnings > 0:
            print(f"\n⚠️  发现 {total_warnings} 个警告（建议修复）:")
            print("-" * 40)
            for category, warnings in self.warnings.items():
                print(f"\n  [{category}]")
                for warning in warnings[:3]:
                    print(f"    • {warning}")
                if len(warnings) > 3:
                    print(f"    ... 还有 {len(warnings) - 3} 个")
        
        print("\n" + "=" * 60)
        
        if total_errors > 0:
            print("🚫 验证失败！请修复上述错误后再部署。")
            print("=" * 60)
        else:
            print("⚠️  有警告但可以部署。建议后续修复警告项。")
            print("=" * 60)

def main():
    validator = WebsiteValidator()
    success = validator.validate_all()
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
