import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:4b"

messages = [
    {
        "role": "system",
        "content": "You are a helpful and concise AI assistant."
    }
]

print("Local AI Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

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
                "stream": False
            },
            timeout=120
        )

        response.raise_for_status()

        assistant_message = response.json()["message"]["content"]

        print(f"AI: {assistant_message}\n")

        messages.append({
            "role": "assistant",
            "content": assistant_message
        })

    except requests.exceptions.RequestException as error:
        print(f"Error: {error}\n")