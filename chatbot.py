import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:4b"

SYSTEM_PROMPT = (
    "You are a helpful AI assistant. "
    "Answer clearly and concisely."
)

messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def print_help():
    print("""
Commands:
  /help   Show this help
  /clear  Clear conversation history
  /model  Show current model
  /exit   Exit chatbot
""")


def clear_conversation():
    global messages

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    print("Conversation cleared.\n")


def chat(user_input):
    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "messages": messages,
                "stream": True
            },
            stream=True,
            timeout=120
        )

        response.raise_for_status()

        assistant_message = ""

        print("AI: ", end="", flush=True)

        for line in response.iter_lines():
            if not line:
                continue

            data = line.decode("utf-8")

            import json
            chunk = json.loads(data)

            content = chunk.get("message", {}).get("content", "")

            print(content, end="", flush=True)
            assistant_message += content

            if chunk.get("done"):
                break

        print("\n")

        messages.append({
            "role": "assistant",
            "content": assistant_message
        })

    except requests.exceptions.ConnectionError:
        print(
            "\nError: Ollama is not running. "
            "Start Ollama and try again.\n"
        )

        messages.pop()

    except requests.exceptions.Timeout:
        print("\nError: Request timed out.\n")
        messages.pop()

    except requests.exceptions.RequestException as error:
        print(f"\nError: {error}\n")
        messages.pop()


def main():
    print("=" * 50)
    print("                 LOCAL AI CHATBOT")
    print("=" * 50)
    print(f"Model: {MODEL}")
    print("Type /help for available commands.\n")

    while True:
        try:
            user_input = input("You: ").strip()

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        if user_input == "/exit":
            print("Goodbye!")
            break

        elif user_input == "/help":
            print_help()

        elif user_input == "/clear":
            clear_conversation()

        elif user_input == "/model":
            print(f"Current model: {MODEL}\n")

        else:
            chat(user_input)


if __name__ == "__main__":
    main()