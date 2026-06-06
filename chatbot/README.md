# 🤖 ChatBot - Simple Rule-Based Python Chatbot

An interactive, rule-based command-line chatbot built in Python. ChatBot parses user queries using regular expressions and keyword pattern matching to identify intents and respond dynamically.

---

## ✨ Features

- **Intent Recognition & Pattern Matching**: Employs Python's standard `re` module to identify user queries (greetings, bot identity, jokes, fun facts, current time/date, mathematical calculations).
- **Basic Math Calculator**: Performs basic arithmetic operations (`+`, `-`, `*`, `/`) dynamically extracted from conversational input.
- **Contextual State**: Remembers your name and uses it in responses throughout the conversation.
- **Organic Visual Flow**: Simulates a human-like typing speed for responses, printing them character-by-character.
- **Console Aesthetics**: Leverages ANSI escape codes for a modern, colorful CLI experience.
- **Windows UTF-8 Compatible**: Automatically reconfigures system standard output and input streams to support UTF-8 characters and emojis across Windows terminals.

---

## 🛠️ Commands & Capabilities

ChatBot is preconfigured to understand a variety of statements and questions. You can try:

| Category | Example Phrases |
| :--- | :--- |
| **Greetings** | `hi`, `hello`, `hey there`, `greetings` |
| **Identity** | `who are you?`, `what is your name?` |
| **Name Update** | `my name is Alice`, `call me Bob`, `i am Charlie` |
| **Jokes** | `tell me a joke`, `make me laugh`, `tell a joke` |
| **Fun Facts** | `tell me a fact`, `random fact`, `give me some trivia` |
| **Time & Date** | `what time is it?`, `what's today's date?`, `current time` |
| **Calculator** | `calculate 12 + 8`, `what is 5 * 25?`, `42 / 6` |
| **Status Check** | `how are you?`, `how is it going?` |
| **Help** | `help`, `commands`, `what can you do` |
| **Exit** | `exit`, `quit`, `bye`, `goodbye` |

---

## 🚀 Running the Chatbot

Ensure you have **Python 3.7+** installed.

1. Open a terminal (CMD, PowerShell, or Bash) in the `chatbot` folder directory.
2. Run the chatbot script:
   ```bash
   python chatbot.py
   ```

---

## 🔍 How it Works Under the Hood

The chatbot is structured around a simple `ChatBot` class:
1. **`start()`**: Prints the welcome banner and requests the user's name.
2. **`match_intent(user_input)`**: Cleanses the input string and scans it sequentially using regular expressions (`re.search`) to match against pre-determined intents.
3. **`respond(intent, entity)`**: Triggers the appropriate output branch. If the math intent is matched, it parses and calculates the numerical operands.
4. **`print_slow(text, color)`**: Helper function that streams output with a brief delay (`sys.stdout.flush`) and colorizes terminal output.
