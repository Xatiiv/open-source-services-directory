#!/usr/bin/env python3
import os
import sys
import re
import json

def load_banned_words():
    """
    Load banned words from a JSON file located in the same directory.
    The JSON file should contain a JSON array of words, e.g.:
        ["word1", "word2", "word3"]
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(script_dir, "banned_words.json")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            banned_words = json.load(f)
            if not isinstance(banned_words, list):
                print(f"Error: {json_path} does not contain a JSON array.")
                return []
            return banned_words
    except Exception as e:
        print(f"Error loading banned words from {json_path}: {e}")
        return []

# Define regex patterns for disallowed HTML tags.
DISALLOWED_TAGS = {
    'script': re.compile(r"<script\b.*?>", re.IGNORECASE),
    'iframe': re.compile(r"<iframe\b.*?>", re.IGNORECASE),
    'object': re.compile(r"<object\b.*?>", re.IGNORECASE),
    'embed': re.compile(r"<embed\b.*?>", re.IGNORECASE),
}

def validate_file(file_path, banned_words):
    """
    Validate the content of a Markdown file.
    Checks for banned words and disallowed HTML tags.
    """
    errors = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        errors.append(f"Error reading {file_path}: {e}")
        return errors

    # Check for banned words.
    for word in banned_words:
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

    # Walk through the docs directory and validate each file.
    for root, dirs, files in os.walk("docs"):
        for file in files:
            file_path = os.path.join(root, file)
            # Ensure only Markdown files are present in docs.
            if not file.endswith(".md"):
                all_errors.append(f"Non-Markdown file found in docs: {file_path}")
            else:
                errors = validate_file(file_path, banned_words)
                if errors:
                    all_errors.extend(errors)

    if all_errors:
        print("Validation errors found:")
        for error in all_errors:
            print(" - " + error)
        sys.exit(1)  # Exit with a non-zero status to fail the GitHub Action.
    else:
        print("All validations passed.")

if __name__ == "__main__":
    main()

