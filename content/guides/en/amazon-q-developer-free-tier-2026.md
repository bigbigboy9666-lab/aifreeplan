# Amazon Q Developer Free Tier Guide 2026: AWS Official AI Coding Assistant

Amazon Q Developer used to be a great free coding assistant from AWS. But the situation has changed.

Good news: if you already have an account, the free tier still works. Bad news: new registrations have been shut down since May 15, 2026.

So the free entry point is essentially closed. But if you can still get an account, the free tier benefits are still solid.

---

## What's in the Free Tier

The free tier is permanent but limited:

- **50 Agent requests/month** — including Q&A chat and agentic coding
- **1,000 lines of code transformation/month** — e.g., Java 8 to Java 17 upgrade
- **Unlimited code completions** — auto-suggestions as you type have no limit
- **Security scanning** — basic vulnerability detection included
- **Reference tracking** — automatically marks open-source code snippet sources

Supported environments: VS Code, JetBrains IDEs, Visual Studio, Eclipse, and CLI.

---

## Free vs Pro

| Feature | Free | Pro ($19/mo) |
|---------|------|-------------|
| Agent requests | 50/month | 1,000/month |
| Code transformation | 1,000 lines/month | 4,000 lines/month |
| Code completion | Unlimited | Unlimited |
| Security scanning | Basic | Advanced + IP indemnity |
| SSO integration | No | Yes (IAM Identity Center) |
| Admin dashboard | No | Yes |

If you just code casually, 50 Agent requests + unlimited completions should suffice. But 50 is really not many — one Agent task might consume several requests. Heavy users should consider Pro.

---

## How to Register

**Important: New registrations are CLOSED.** As of May 15, 2026, AWS stopped accepting new Amazon Q Developer accounts.

If you previously registered via Builder ID or IAM Identity Center, your account is unaffected and continues to work normally.

Registration method (for existing account recovery or migration scenarios):

1. Download the IDE plugin (VS Code / JetBrains / Visual Studio / Eclipse)
2. Log in with your AWS Builder ID
3. Free tier activates automatically

**Note**: Builder ID is a personal account system, separate from paid AWS accounts. The free tier only supports Builder ID and IAM users, not IAM Identity Center (that's a Pro feature).

---

## Core Features

**Code completion** — Real-time suggestions, comparable to GitHub Copilot. This is the only truly unlimited feature in the free tier.

**Agentic coding** — Let AI understand your entire project structure and execute multi-step tasks. Like "refactor this module" or "generate unit tests." Each Agent task consumes request quota.

**Security scanning** — Automatically detects security vulnerabilities with fix suggestions. Free tier includes basic scanning.

**Code transformation** — Automatic Java version upgrades, .NET framework migration. Free tier gets 1,000 lines/month.

**AWS integration** — Answers questions about AWS resources, generates CLI commands, diagnoses console errors.

---

## Real-World Experience

Code completion quality is decent, not far behind GitHub Copilot. The Agent feature is limited by the 50-request/month cap — one code refactoring might burn through several requests.

Security scanning is okay for basic use — catches common vulnerabilities but lacks depth compared to professional security tools.

Code transformation is helpful for Java projects, but the 1,000-line monthly limit means it works for small modules, not large projects.

---

## Alternatives

Since new registration is closed, if you need a similar free coding assistant, consider:

- **GitHub Copilot Free** — Limited free tier for individual developers
- **Codeium** — Completely free AI coding assistant
- **Cursor Free** — Has a free tier
- **Amazon Q in the Cloud** — Still free in the AWS console (unaffected by this change)

---

## Summary

Amazon Q Developer's free tier used to be great — unlimited code completions + basic Agent + security scanning. But new registrations are closed, and existing users can continue until April 30, 2027 (EOL date).

If you already have an account, use it while you can. If you don't, don't wait — AWS has clearly stated no new registrations.

The free tier's 50 Agent requests/month is tight, but code completions and security scanning are genuinely free benefits. Light users should find it adequate; heavy users may need other solutions.

---

*Data current as of July 14, 2026. AWS policies may change. Check aws.amazon.com/q/developer/pricing/ for the latest information.*
