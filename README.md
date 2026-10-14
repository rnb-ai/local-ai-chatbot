# Local AI Chatbot

A simple command-line chatbot that connects to a local Ollama server and uses a local language model to generate responses in the terminal.

## Features

- Interactive chat in the terminal
- Uses Ollama's `/api/chat` endpoint
- Keeps a short conversation history for context
- Includes built-in commands for help, clearing the chat, checking the model, and exiting

## Requirements

- Python 3.9+
- Ollama installed and running locally
- A model available in Ollama, such as `qwen3:4b`

## Setup

1. Clone the repository.
2. Create and activate a virtual environment if desired.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start Ollama locally and pull the model used by the app:

```bash
ollama pull qwen3:4b
```

## Run the chatbot

```bash
python chatbot.py
```

## Commands

Inside the chat session, you can use:

- `/help` - Show available commands
- `/clear` - Clear conversation history
- `/model` - Show the current model
- `/exit` - Exit the chatbot

## Configuration

The application is configured in `chatbot.py`:

- `OLLAMA_URL = "http://localhost:11434/api/chat"`
- `MODEL = "qwen3:4b"`

If you want to use a different model, update the `MODEL` value in the file.

## Notes

This project is intentionally lightweight and designed for local use. Ensure Ollama is running before starting the chatbot, or the app will display a connection error.
