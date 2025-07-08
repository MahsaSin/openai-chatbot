# 🧠 ChatBot with OpenAI API

A simple command-line chatbot using the OpenAI API and the `gpt-4.1-nano` model.

## 📦 Requirements

- Python 3.7+
- `openai` Python package

## 🛠 Installation

```bash
pip install openai
```

## 🚀 Usage

1. Set your OpenAI API key.
2. Run the script.

### Example

```python
from openai import OpenAI
from chatbot import ChatBot  # if saved as chatbot.py

bot = ChatBot(openai_api_key="your-api-key-here")
bot.run()
```

Or directly:

```bash
python chatbot.py
```

You’ll see:

```
User: Hello
ChatBot: Hi! How can I help you today?
```

Type `quit` to end the conversation.

## 📚 How It Works

- Uses `gpt-4.1-nano` model via `OpenAI` client.
- Maintains conversation history.
- Runs in a loop until the user types `quit`.

## 📝 Notes

- Replace `"your-api-key-here"` with your actual OpenAI API key.
- Ensure your API plan supports `gpt-4.1-nano`.