from openai import OpenAI

class ChatBot:
    def __init__(self, openai_api_key):
        self.client = OpenAI(api_key=openai_api_key)
        self.history = []

    def run(self, user_input, history):

        messages = []
        for human, assistant in history:
            messages.append({"role": "user", "content": human})
            messages.append({"role": "assistant", "content": assistant})
        messages.append({"role": "user", "content": user_input})

        response = self.client.responses.create(
            model="gpt-4.1-nano",
            input=messages
        )

        assistant_response = response.output_text
        return assistant_response