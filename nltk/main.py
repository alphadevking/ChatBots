from nltk.chat.util import Chat, reflections
from pairs import PAIRS


class ElizaBot:
    def __init__(self):
        self.eliza = Chat(PAIRS, reflections)

    def respond(self, user_input):
        if user_input == "__first":
            return "Hi! I'm ALBERT, your digital assistant."
        return self.eliza.respond(user_input)


def main():
    print("ALBERT: Hi! I'm ALBERT, your digital assistant. Type 'quit' to exit.")
    bot = ElizaBot()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = bot.respond(user_input)
        print(f"ALBERT: {response}")


if __name__ == "__main__":
    main()
