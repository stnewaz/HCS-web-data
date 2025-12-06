from openai import OpenAI
from question_answering_bot import manage_query
import os


class Bot():
    def __init__(self, sys_message=None):
        self.messages = []
        if sys_message:
            self.set_sysMessage(sys_message)

        # create OpenAI client using environment variable
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def set_sysMessage(self, sys_message):
        # store system message in memory
        self.system_message = {"role": "system", "content": sys_message}
        self.messages = [self.system_message]

    def handle_input(self, query):
        # add user input
        self.messages.append({"role": "user", "content": query})

        # call OpenAI API
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=self.messages
        )

        reply = response.choices[0].message.content

        # store response
        self.messages.append({"role": "assistant", "content": reply})

        # return message text
        class DummyMsg:
            def __init__(self, content):
                self.content = content
        return DummyMsg(reply)


def BotUser_dialogue_cycle(bot, user):

    f = open(f"chatlog/chat{user}.txt", "a")

    ai_message = bot.handle_input("Hi")

    print("You are talking to SFU counselling information Chatbot. If you wish to exit the conversation, please type in the word: exit")

    end_flag = False
    while end_flag is not True:
        print("Bot>> " + ai_message.content)
        print("Bot>> " + ai_message.content, file=f)
        print("Please remember that this chatbot is is only equipped to handle questions regarding services and resources provided by SFU Health and Couneslling website. This bot is not a licensed medical practicioner. Please see a doctor of professional for medical advice and diagnoses.")
        print(file=f)


        user_inpt = input("User>>")
        print("User>>" + user_inpt, file=f)
        print(file=f)

        if user_inpt == "exit":
            end_flag = True
            break

        augmented_prompt = manage_query([], user_inpt)

        ai_message = bot.handle_input(augmented_prompt)
    return
