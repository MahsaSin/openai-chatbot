import os
import gradio as gr

from dotenv import load_dotenv

from chatbot import ChatBot


def main():
    load_dotenv()
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    chatbot = ChatBot(openai_api_key=openai_api_key)
    gr.ChatInterface(chatbot.run).launch(share=True)

if __name__ == "__main__":
    main()
