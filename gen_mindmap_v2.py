#!/usr/bin/env python3
"""Generate and deploy the AI mindmap comparison guide with proper bilingual content."""
import json
import os
import sys

today = '2026-07-24'
slug = 'ai-mindmap-tools-free-comparison-2026'

# Read content from the file
with open('/home/ubuntu/aifreeplan/tmp_mindmap_content.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

title_zh = lines[0].strip()
title_en = lines[1].strip()
desc_zh = lines[2].strip()
desc_en = lines[3].strip()
content_zh_full = lines[4].strip()  # This is actually the Chinese content

# Extract just the Chinese content (first section before English)
# The file has Chinese content first, then English content
# We need to split them properly

# Actually let me read the file and parse it properly
with open('/home/ubuntu/aifreeplan/tmp_mindmap_content.txt', 'r', encoding='utf-8') as f:
    full_content = f.read()

# Split by finding where English content starts
# The Chinese content has <h1>AI Mind Map Tools Free Tier Comparison...</h1> which is actually the EN title
# Let me re-read the structure - the file has:
# Line 0: Chinese title
# Line 1: English title  
# Line 2: Chinese desc
# Line 3: English desc
# Line 4+: HTML content (which appears to be all English based on what we wrote)

# Wait - I made a mistake. The content in line 4 is the English version.
# I need to generate proper Chinese content separately.

print("Content file loaded")
print(f"Title ZH: {title_zh}")
print(f"Title EN: {title_en}")
print(f"Desc ZH: {desc_zh}")
print(f"Desc EN: {desc_en}")
print(f"Content length: {len(full_content)} chars")
