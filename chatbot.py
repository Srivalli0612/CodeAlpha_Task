import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [r"my name is (.*)", ["Hello %1, how can I help you today?", "Hi %1, nice to meet you!"]],
    [r"hi|hello|hey", ["Hello! How can I assist you?", "Hi there! What can I do for you?"]],
    [r"how are you", ["I'm just a bot, but I'm doing well! How about you?", "I'm doing great, thank you for asking!"]],
    [r"what is your name", ["I am a chatbot created to help you."]],
    [r"quit", ["Goodbye! Have a great day ahead."]],
    [r"(.*) created you", ["I was created by a programmer to chat with you."]],
    [r"(.*) (location|city)", ["I live in the digital world, where do you live?"]],
    [r"(.*) weather (.*)", ["I'm not sure about the weather. You can check online for the latest updates."]],
    [r"(.*) your favorite color", ["I like all colors, but I think blue is quite calming."]],
    [r"(.*) (food|eat)", ["I don’t eat, but I enjoy learning about different cuisines."]],
    [r"(.*) (age|old)", ["Age is just a number! I’m as old as technology allows me to be."]],
    [r"(.*) (hobby|hobbies)", ["I like chatting with interesting people like you!"]],
    [r"(.*) love (.*)", ["Love is a beautiful feeling. How do you describe it?"]],
    [r"(.*) (sport|game)", ["I enjoy learning about various sports. Do you have a favorite?"]],
    [r"do you (.*) (like|love) (.*)", ["I find %3 quite fascinating."]],
    [r"can you (.*)", ["I can try my best to %1. What do you need help with?"]],
    [r"(.*) help (.*)", ["Sure! What do you need help with?"]]
]
chatbot=Chat(pairs, reflections)
def start_chatbot():
    print("Hello! I am a basic chatbot. Type 'quit' to exit.")
    while True:
        user_input=input("You: ")
        if user_input.lower()=='quit':
            print("Goodbye!")
            break
        response=chatbot.respond(user_input)
        if response:
            print("Bot: ", response)
        else:
            print("Bot: Sorry, I didn't understand that.")
if __name__=="__main__":
    start_chatbot()
