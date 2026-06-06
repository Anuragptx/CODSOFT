import re
import random
from datetime import datetime

name = ""

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you call a fake noodle? An impasta!"
]

facts = [
    "Honey never spoils.",
    "Bananas are berries, but strawberries aren't."
]

print("Simple Rule-Based Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ").lower().strip()

    if user in ["exit", "bye", "quit"]:
        print("Bot: Goodbye!")
        break

    elif user == "help":
        print("Bot: You can ask about time, date, jokes, facts, or say hello.")

    elif user in ["hi", "hello", "hey"]:
        print("Bot: Hello!")

    elif "my name is" in user:
        name = user.replace("my name is", "").strip().title()
        print(f"Bot: Nice to meet you, {name}!")

    elif "your name" in user or "who are you" in user:
        print("Bot: I am a simple chatbot made in Python.")

    elif "how are you" in user:
        print("Bot: I am fine and working properly.")

    elif "joke" in user:
        print("Bot:", random.choice(jokes))

    elif "fact" in user:
        print("Bot:", random.choice(facts))

    elif "time" in user or "date" in user:
        now = datetime.now()
        print("Bot:", now.strftime("%d-%m-%Y %I:%M %p"))

    elif re.search(r'(\d+)\s*([\+\-\*/])\s*(\d+)', user):
        match = re.search(r'(\d+)\s*([\+\-\*/])\s*(\d+)', user)

        a = int(match.group(1))
        op = match.group(2)
        b = int(match.group(3))

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        else:
            result = "Cannot divide by zero" if b == 0 else a / b

        print("Bot:", result)

    else:
        print("Bot: Sorry, I don't understand that.")