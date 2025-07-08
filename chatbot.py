from openai import OpenAI


class ChatBot:
    def __init__(self, openai_api_key):
        self.client = OpenAI(api_key=openai_api_key)
    
    def run(self):

        history = []

        while True:
            user_input = input("User: ")
            if user_input.lower() == "quit":
                break

            history.append({"role": "user", "content": user_input})

            response = self.client.responses.create(model="gpt-4.1-nano", input=history)

            print("ChatBot:", response.output_text)
            history += [
                {"role": "assistant", "content": response.output_text}
            ]
