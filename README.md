# AI_arena
LLM Arena — Gemini vs Groq

A simple, interactive Large Language Model (LLM) comparison application built with Python and Gradio. LLM Arena allows users to submit the same prompt to two different models, compare their responses side by side, and vote for the response they prefer.

The project is part of my hands-on learning journey in Generative AI and AI Engineering, exploring LLM API integration, model comparison, and user feedback.

✨ Features

Side-by-side comparison: Submit one prompt and view responses from both models.

Multiple LLM providers: Integrates Google Gemini and Groq APIs.

Interactive interface: Built using Gradio for a simple, browser-based experience.

User feedback: Vote for your preferred response using thumbs-up and thumbs-down buttons.

Environment-based configuration: Keeps API credentials outside the application source code.

🛠️ Tech Stack

Language: Python

UI Framework: Gradio

LLM Providers: Google Gemini API and Groq API

API Integration: OpenAI Python SDK with OpenAI-compatible endpoints

Configuration: Python dotenv

🏗️ How It Works

Enter a prompt in the web interface.

The application sends the same prompt to the configured Gemini and Groq models.

Both responses are displayed side by side.

Vote for the response you find more useful.

🚀 Getting Started

Prerequisites

Python 3.10 or later

A Google Gemini API key

A Groq API key

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/llm-arena-gemini-groq.git
cd llm-arena-gemini-groq

Replace YOUR_USERNAME with your GitHub username.

2. Create a virtual environment

python -m venv env

Activate it on Windows:

.\env\Scripts\Activate.ps1

3. Install dependencies

pip install -r requirements.txt

4. Configure API keys

Create a .env file in the project root:

GOOGLE_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key

Use valid API keys from Google AI Studio and Groq Console.

Security: Never commit your .env file or expose API keys in public repositories.

5. Run the application

python arena_app.py

Open the local URL shown in your terminal, typically:

http://127.0.0.1:7860

🎯 Learning Objectives

This project provides hands-on experience with:

Integrating multiple LLM providers into one application.

Working with chat-completion APIs and model identifiers.

Building interactive AI applications with Gradio.

Collecting human feedback on model-generated responses.

Managing API credentials and troubleshooting integration issues.

🔮 Future Improvements

Planned enhancements include:

Measuring and comparing model response latency.

Executing model requests concurrently.

Persisting prompts, responses, and user votes.

Building a reusable evaluation dataset.

Comparing model outputs using defined evaluation criteria.

Displaying aggregate model performance metrics.

👨‍💻 About

I'm building practical projects as I deepen my understanding of Machine Learning, Generative AI, Large Language Models, and AI Engineering.

This project reflects my approach to learning: build something functional, experiment with real APIs, identify limitations, and improve through iteration.
