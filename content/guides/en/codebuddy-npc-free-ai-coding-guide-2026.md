# CodeBuddy NPC Full Guide: Summon an AI Colleague With @ to Work for You

## TL;DR

Tencent Cloud's CNB platform launched CodeBuddy NPC, powered by the DeepSeek-V4-Flash engine. Just @ it in any repo comment and it starts working on its own. Three steps to summon it: open a repo → @CodeBuddy NPC → enable "work-for-me" mode, and the AI automatically handles requirement understanding → task breakdown → coding → quality verification. Free until the end of 2026.

## What Is CodeBuddy NPC

CodeBuddy is an AI coding assistant integrated into Tencent Cloud's CNB (Cloud Native Build) platform. It was upgraded in August 2026 to run on DeepSeek-V4-Flash, built around one idea: **@ it once, and the AI does the work for you**.

Official certification: it has passed the CAICT (China Academy of Information and Communications Technology) certification covering five core capabilities:
- Requirement understanding
- Task breakdown
- Coding execution
- Quality verification
- Workflow collaboration

## How It Differs From JoyCode

A lot of people mix these two up. Simply put:
- **JoyCode**: a standalone client from JD, credit-based (10,000 credits/month, burns fast)
- **CodeBuddy NPC**: integrated into Tencent Cloud CNB, @-summon model, free through year-end

### Comparison

| Feature | CodeBuddy NPC | JoyCode |
|---------|---------------|---------|
| Platform | cnb.cool | joycode.jd.com |
| Integration | @-summon + repo integration | Standalone client |
| Model | DeepSeek-V4-Flash | Multi-model (GLM-5/DeepSeek/Kimi, etc.) |
| Free policy | Free through 2026-12-31 | 10,000 credits/month |
| Core function | Auto-completes dev tasks | AI-assisted coding |
| Best for | Users who want it to "work for them" | Everyday coding |

## How to Use It (Step by Step)

### Step 1: Register a CNB Account

Go to https://cnb.cool and sign up. Supports phone number, WeChat, and GitHub login.

### Step 2: Create or Import a Repo

- New repo: click "+" in the top-right to create one
- Import repo: bring in an existing project from GitHub/GitLab

### Step 3: Summon CodeBuddy NPC

In any **issue, PR, or comment** in your repo, type:

```
@CodeBuddy NPC
```

Then describe what you need, for example:
- "@CodeBuddy NPC write me a user registration endpoint"
- "@CodeBuddy NPC how do I fix this bug?"
- "@CodeBuddy NPC write unit tests for this function"

### Step 4: Enable "Work-For-Me" Mode

Add the trigger keyword or button in a comment (exact UI may vary by platform). Once "work-for-me" is on, CodeBuddy NPC will automatically:
1. Understand your requirement
2. Break the task down
3. Write the code
4. Run the tests
5. Submit a PR or reply in the thread

## Real Use Cases

### Case 1: Build a New Feature

Describe it in an issue:
```
@CodeBuddy NPC implement a REST API that supports user login, registration, and password change
```

CodeBuddy NPC will automatically:
- Analyze the existing code structure
- Generate the endpoint code
- Write the database model
- Write test cases
- Submit a PR for review

### Case 2: Fix a Bug

In a PR comment:
```
@CodeBuddy NPC this function has a bug — it crashes when the username is empty
```

CodeBuddy NPC will:
- Locate the faulty code
- Analyze the root cause
- Generate a fix
- Submit a patch

### Case 3: Code Review

```
@CodeBuddy NPC review this code and check for security issues
```

CodeBuddy NPC will:
- Analyze the logic
- Check for vulnerabilities
- Give optimization suggestions
- Generate a review report

## Things to Know

### 1. Free Period

The offer runs through **December 31, 2026**. That means:
- Now is the golden window to use it for free
- It may be paid or restricted starting January 2027
- Use and test it heavily while you can

### 2. Suitable Projects

- Works for web projects (frontend + backend)
- Supports mainstream frameworks (React, Vue, Express, Django, etc.)
- Not ideal for niche areas like embedded or game dev

### 3. Quality Assessment

- DeepSeek-V4-Flash is a lightweight model; code quality is mid-to-upper
- Manually review complex logic
- Generated code may miss edge cases

### 4. Versus Cursor

| Feature | CodeBuddy NPC | Cursor |
|---------|---------------|--------|
| Free | Free through end of 2026 | Free tier is limited |
| Mode | @-summon, auto-executes | Manual chat |
| Integration | Inside the CNB platform | Standalone IDE |
| Best for | Users who want to "relax" | Users who want to control every step |

## FAQ

**Q1: Is CodeBuddy NPC actually free?**
A1: Yes, it is free through 2026-12-31. No credit card required during the free window.

**Q2: Which model does it run on?**
A2: DeepSeek-V4-Flash, a lightweight engine optimized for fast repo-aware coding tasks.

**Q3: Can it write tests on its own?**
A3: Yes. In "work-for-me" mode it generates test cases and can run them before submitting a PR.

**Q4: Does it work with my existing GitHub repo?**
A4: Import your GitHub project into CNB first, then @-summon CodeBuddy NPC in the imported repo.

**Q5: When will it start charging?**
A5: The official free period ends 2026-12-31. After that it may move to a paid or restricted model — plan your usage before the cutoff.

## Summary

CodeBuddy NPC is Tencent Cloud CNB's AI coding assistant, powered by DeepSeek-V4-Flash, built around the "work for me" concept. Three steps to summon it: open a repo → @CodeBuddy NPC → enable work-for-me mode, and the AI does the work.

**Best for:**
- Developers who don't want to type every line
- Builders who want to validate ideas fast
- Teams looking to boost throughput

**Not for:**
- Teams that need tight control over code quality
- Commercial projects that demand rock-solid stability

**Recommendation:** while it's free, explore the use cases that fit you. Year-end may bring pricing, so get familiar early.

## Related Links

- CNB site: https://cnb.cool
- CodeBuddy entry: @-summon inside any repo on cnb.cool
- Compare: see the JoyCode and Cursor guides on aifreeplan.com

---

*More AI tool free-tier info at aifreeplan.com*
