from chatbot import ChatBot
from configparser import ConfigParser
import sys
def main():
    config=ConfigParser()
    config.read('cred.ini')
    api_key=config['gemini_ai']['API_KEY']

    chatbot=ChatBot(api_key=api_key)

    chatbot.start_conversation()

    print("Hello GOJO")

    while True:
        user_input=input("You: ")
        if user_input.lower()=='quit':
            sys.exit('chatbot exiting....')
        
        try:
            response=chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}:{response}")
        except Exception as e:
            print(f"Error occured: {e}")

main()
