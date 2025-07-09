import os
import gradio as gr

from dotenv import load_dotenv

from chatbot import ChatBot


def main():
    load_dotenv()
    openai_api_key = os.environ.get("OPENAI_API_KEY")
    mongo_url = os.environ.get("MONGO_URL")

    chatbot = ChatBot(openai_api_key=openai_api_key, mongo_url=mongo_url)
    gr.ChatInterface(chatbot.run).launch(share=True)


if __name__ == "__main__":
    main()
