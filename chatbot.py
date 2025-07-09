from openai import OpenAI
import datetime

from mongodbclient import MongodbClient

class ChatBot:
    def __init__(self, openai_api_key, mongo_url):
        self.client = OpenAI(api_key=openai_api_key)
        self.mongo_client = MongodbClient(mongo_url)
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
        self.history.append((user_input, assistant_response))

        record = {
            "user_input": user_input,
            "assistant_response": assistant_response,
            "time": datetime.datetime.now()
        }

        self.mongo_client.insert(record)
        
        return assistant_response