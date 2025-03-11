#!/usr/bin/env python3
import os
import sys
import re
import json

# Define patterns to detect disallowed HTML tags.
DISALLOWED_TAGS = {
    'script': re.compile(r"<script\b.*?>", re.IGNORECASE),
    'iframe': re.compile(r"<iframe\b.*?>", re.IGNORECASE),
    'object': re.compile(r"<object\b.*?>", re.IGNORECASE),
    'embed': re.compile(r"<embed\b.*?>", re.IGNORECASE),
}

def load_banned_words():
    """
    Loads the banned words from a JSON file.
    The JSON file should contain an array of words, for example:
        ["word1", "word2", "word3"]
    """
    # Determine the path relative to this script.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "banned_words.json")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            banned_words = json.load(f)
            # Ensure the loaded data is a list.
            if not isinstance(banned_words, list):
                print(f"Error: {json_path} does not contain a JSON array.")
                return []
            return banned_words
    except Exception as e:
        print(f"Error loading banned words from {json_path}: {e}")
        return []

def validate_file(file_path, banned_words):
    errors = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        errors.append(f"Error reading {file_path}: {e}")
        return errors

    # Check for banned words.
    for word in banned_words:
        # Use word boundaries for accurate, case-insensitive matches.
        if re.search(r"\b" + re.escape(word) + r"\b", content, re.IGNORECASE):
            errors.append(f"Found banned word '{word}' in {file_path}")

    # Check for any disallowed HTML tags.
    for tag, pattern in DISALLOWED_TAGS.items():
        if pattern.search(content):
            errors.append(f"Found disallowed <{tag}> tag in {file_path}")

    return errors

def main():
    banned_words = load_banned_words()
    all_errors = []
    # Walk through the 'docs' directory to validate each Markdown file.
    for root, dirs, files in os.walk("docs"):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                file_errors = validate_file(file_path, banned_words)
                if file_errors:
                    all_errors.extend(file_errors)

    if all_errors:
        print("Markdown validation errors found:")
        for error in all_errors:
            print(" - " + error)
        sys.exit(1)  # Non-zero exit code to fail the action.
    else:
        print("All Markdown files passed validation.")

if __name__ == "__main__":
    main()
