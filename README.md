# AI-Powered Coding Assistant
A lightweight AI tool designed to automate local development tasks. This project leverages Google’s Gemini LLM to interpret natural language instructions and execute real-world file system operations and code execution.

## Overview
This agent uses Tool (Function Calling) to interact with local environment. It doesn't just suggest code; it can explore your directory structure, read files, apply fixes, and verify those fixes by running the Python interpreter.

## Key Features
- Autonomous Task Execution: Accepts high-level coding prompts and breaks them down into actionable steps.
- Context-Aware File Operations: Automatically scans directories and reads file contents to gather context for a task.
- Self-Correction Loop: The agent can execute Python scripts, capture errors from the terminal, and iterate on its solution until the code runs successfully.

## How It Works
The agent operates in a loop:
1. Analyze: The LLM determines the next best step based on the user's prompt and current state.
2. Act: The agent calls a predefined Python function (e.g., write_file or run_python_file).
3. Observe: The output of the function is fed back into the LLM.
4. Repeat: The process continues until the agent provides a final response confirming the task is complete.

## Getting Started
- API Key: Gemini API key 
- Execution:
`uv run main.py "Your coding task here"`