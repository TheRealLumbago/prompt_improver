# Prompt Enhancer AI

A Streamlit web application that transforms user prompts into more engaging, detailed, and thought-provoking questions using OpenAI's GPT-4o-mini model.

## Features

- ✨ Interactive web interface built with Streamlit
- 🤖 AI-powered prompt enhancement using OpenAI GPT-4o-mini
- 📥 Download enhanced prompts as text files
- 🎯 Simple and intuitive user experience

## Requirements

- Python 3.8+
- OpenAI API key
- Required Python packages:
  - streamlit
  - langchain-openai
  - langchain-core

## Installation

1. Clone this repository:
```bash
git clone https://github.com/TheRealLumbago/prompt_improver.git
cd prompt_improve
```

2. Install the required dependencies:
```bash
pip install streamlit langchain-openai langchain-core
```

3. Create a `.openai` file in the project root and add your OpenAI API key:
```
your-openai-api-key-here
```



## Usage

1. Start the Streamlit application:
```bash
streamlit run prompt_enchancer_app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically `http://localhost:8501`)

3. Enter your prompt in the text area and click "Enhance Prompt"

4. View the enhanced prompt and download it if needed

## How It Works

The application uses a specialized system prompt that instructs the AI to:
- Transform user prompts into more engaging versions
- Add detail and depth to questions
- Make prompts more thought-provoking
- Return only the enhanced prompt without explanations


