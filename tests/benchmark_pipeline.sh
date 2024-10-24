#!/bin/bash
set -e  # Exit immediately if a command exits with a non-zero status

# File containing questions
QUESTIONS_FILE="benchmark_questions.txt"

# Output benchmark file
BENCHMARK_FILE="benchmark.md"

# Initialize the benchmark file with a header
cat <<EOL > $BENCHMARK_FILE
# Benchmark for GPT-Based OncRDS Chatbot
## `date`

This benchmark is designed to evaluate the performance of the OncRDS GPT-based chatbot in answering users' questions accurately and efficiently. The focus is on assessing the chatbot's ability to:

- Provide precise and helpful answers based on OncRDS documentation.
- Clarify technical and biological terms for users with varying levels of expertise.
- Reference appropriate documentation sources or external links when available.
- Respond appropriately when information is unavailable or when questions fall outside the scope of OncRDS.

EOL

# Check if the questions file exists
if [ ! -f $QUESTIONS_FILE ]; then
    echo "Questions file not found."
    exit 1
fi

# Read questions from the file and process each one
QUESTION_NUMBER=1
while IFS= read -r QUESTION || [ -n "$QUESTION" ]; do
    echo "## Q$QUESTION_NUMBER. $QUESTION" >> $BENCHMARK_FILE
    echo "## Q$QUESTION_NUMBER. $QUESTION"
    bash chatbot_demo.sh -q "$QUESTION" >> $BENCHMARK_FILE
    echo -e >> $BENCHMARK_FILE
    ((QUESTION_NUMBER++))
done < $QUESTIONS_FILE