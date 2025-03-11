#!/bin/sh

set -e  # Exit immediately on error

# Detect OS (Linux, macOS, Windows)
OS="$(uname -s 2>/dev/null || echo "Windows")"

# Verify `gum` is installed
if ! command -v gum >/dev/null 2>&1; then
    echo "gum is not installed. Please install it first: https://github.com/charmbracelet/gum"
    exit 1
fi


TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

echo $TIMESTAMP