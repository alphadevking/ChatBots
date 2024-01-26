def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! How can I help you?"
    elif "how are you" in user_input:
        return "I'm just a script, but I'm doing well! How about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Can you try asking something else?"


def run_chatbot():
    print("Welcome to the chatbot! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot: " + response)

        if "bye" in user_input.lower():
            break


if __name__ == "__main__":
    run_chatbot()
