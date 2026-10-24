
import random

responses = {
    "hi": ["Hello!", "Hi there!", "Welcome to the chatbot!"],
    "hello": ["Hello!", "Hi there!", "Welcome to the chatbot!"],
    "welcome": ["Thank you!", "Welcome to the chat!"],

    "how are you": ["Fine, and you?", "I'm good!", "I'm happy!"],

    "what are you doing": [
        "Nothing much.",
        "I'm working.",
        "Enjoying a movie.",
        "Watching TV."
    ],

    "where are you from": [
        "I'm from Latur.",
        "I'm from Pune.",
        "I'm from Mumbai."
    ],

    "what is your profession": [
        "I'm an engineer.",
        "I'm a doctor.",
        "I'm a businessman."
    ],
    "what do you do": [
        "I'm an engineer.",
        "I'm a doctor.",
        "I'm a businessman."
    ],

    "what is your hobby": [
        "Watching TV.",
        "Reading.",
        "Swimming.",
        "Travelling."
    ]
}

exit_commands = ["exit", "close", "quit"]

def chatbot():
    print("Welcome to Bot Chat!")
    print("Type 'exit' or 'close' to end the chat.\n")

    while True:
        user_input = input("User: ").strip().lower()

        # Exit the chatbot
        if user_input in exit_commands:
            print("Bot: Thank you for chatting!")
            break

        # Find a matching response
        if user_input in responses:
            print("Bot:", random.choice(responses[user_input]))
        else:
            print("Bot: Sorry, I didn't understand.")
            print("Please try another question.")

        print()

chatbot()
