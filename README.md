# 🧠 ChatBot with OpenAI API

A simple command-line chatbot using the OpenAI API (`gpt-4.1-nano`) with environment variable support.

## 📦 Requirements

- Python 3.7+
- `openai` package
- `python-dotenv` package

## 🛠 Installation

```bash
pip install openai python-dotenv
```

## ⚙️ Setup

Create a `.env` file in the project directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your-api-key-here
```

## 🚀 Usage

Run the chatbot script:

```bash
python main.py
```

You’ll see:

```
User: Hello
ChatBot: Hi! How can I help you today?
```

Type `quit` to end the conversation.

## 📁 Project Structure

```
project/
│
├── chatbot.py         # Contains the ChatBot class
├── main.py            # Entry point for running the bot
├── .env               # Stores your OpenAI API key
└── README.md
```

## 📚 How It Works

- Loads `OPENAI_API_KEY` from the `.env` file.
- Creates a chatbot instance using the `ChatBot` class.
- Maintains conversation history.
- Uses `gpt-4.1-nano` for responses.

## 📝 Notes

- Make sure your API key is valid and the model is accessible on your OpenAI plan.
- Don’t share your `.env` file or API key publicly.
