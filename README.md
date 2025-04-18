# CS325 Project 1 - Local Language Models

## Project Overview
This project implements two local language models (**GPT-2** and **DistilGPT-2**) to process and generate responses to specific prompts. The models run entirely on the local machine, demonstrating the capability to use small-scale language models without requiring external API calls.

The goal is to evaluate how smaller models perform on simple text generation tasks and understand the process of working with local language models.

---

## Setup Instructions

Follow these steps to set up the project on your local machine.

```bash
git clone https://github.com/Rohoxoxo/CS325_project1.git
cd CS325_Project1

2. Create and Activate Virtual Environment
python -m venv llm_project_env
source llm_project_env/bin/activate

3. Install Dependencies
pip install -r requirements.yaml

How to Run the Program
After setting up the environment, run the main.py script:
python main.py
The program will:

Load GPT-2 and DistilGPT-2 models locally.
Process the given prompts.
Save the responses into text files.

Prompts Used
The following prompts were used as inputs for both models:
A shocking Chinese AI advancement called DeepSeek is sending US stocks plunging
As sales slump, Kohl’s turns to a new CEO to bring back customers
Expect record-high egg prices for most of the year

Output Files
After running the script, two text files will be generated containing the model responses:

GPT2_responses.txt — Responses generated by GPT-2.
DistilGPT2_responses.txt — Responses generated by DistilGPT-2.
Each file contains the original prompts followed by the corresponding generated responses.

Project Details
Models Used:

GPT-2: A generative language model with 117M parameters.
DistilGPT-2: A distilled, smaller version of GPT-2 optimized for faster performance with fewer parameters.
Libraries:

transformers — For loading and running the pre-trained language models.
torch — Backend for running the models.
Special Handling:

Truncation: Enabled to prevent exceeding maximum token limits.
Padding: Set using pad_token_id to properly format model outputs.

How This Works
Tokenization: The input prompts are tokenized into a format understandable by the models.
Text Generation: The models predict the next tokens based on the given prompts.
Decoding: The generated tokens are converted back into readable text.
Saving Output: The responses are written to text files for review.

Author
Name: Rohit Chandel
Course: CS325 — Spring 2025
Project: Local Language Models (Project 1)

A
