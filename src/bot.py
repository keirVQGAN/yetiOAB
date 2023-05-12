import time
from src.generate_bot_response import generate_bot_response

def bot(history, openai_api_key):
    user_message = history[-1][0]
    bot_response = generate_bot_response(user_message, openai_api_key)
    user_message = history[-1][0]
    bot_response = generate_bot_response(user_message)
    history[-1] = (user_message, "")
    for character in bot_response[-1][-1]:
        history[-1] = (user_message, history[-1][-1] + character)
        time.sleep(0.05)
        yield history
