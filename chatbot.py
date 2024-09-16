import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am just a bot, but I am doing great!', 'I am fine, thanks for asking!']),
    (r'what is your name?', ['I am a chatbot created by OpenAI.', 'You can call me Chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Have a nice day!']),
    (r'(.*)', ['I am not sure how to respond to that.', 'Can you please rephrase?', 'Sorry, I don\'t understand.'])
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I am your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['bye', 'goodbye']:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chat()
