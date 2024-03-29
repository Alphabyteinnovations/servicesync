#!/bin/bash

# Function to check and display version
check_version() {
    program=$1
    version_command=$2

    echo -n "$program version: "
    $version_command 2>/dev/null || echo "Not installed"
}

# Check Go version
check_version "Go" "go version"

# Check Rust version
check_version "Rust" "rustc --version"

# Check Python version
check_version "Python" "python3 --version"

# Check Python version
check_version "Docker" "docker --version"

# Display information
echo "Made by Alphabyteinnovations.com"
echo "Alphabyteinnovations.com:300"
echo "GitHub: github.com/smarthobbyjd/servicesync"
echo "Visit: Alphabyteinnovations.com:3000"

# Open a URL
#URL="http://www.Alphabyteinnovations.com:3000"

# Detect the operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open $URL
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
    # Linux
    xdg-open $URL
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    start $URL
else
    echo "Unsupported operating system"
fi
