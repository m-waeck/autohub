from datetime import datetime
from mistralai import Mistral

def get_response(message, save_chat, api_key, model):

    client = Mistral(api_key=api_key)

    messages = [
        {"role": "user", "content": message}
    ]

    # No streaming
    chat_response = client.chat.complete(
        model=model,
        messages=messages,
    )

    if save_chat:
        chat = "Message:\n" + message + """\n---\n""" + "Response:\n" + chat_response.choices[0].message.content
        with open(f"completions/chat_{datetime.now().strftime('%d-%m-%Y_%H:%M:%S')}.txt", "w") as f:
            f.write(chat)

    return chat_response.choices[0].message.content