# Project: Simple Rule-Based Chatbot
# Created by: [NIBSHAN JOVIN JOSEPH]
# Date: [20-07-2025]

import re
from datetime import datetime

def CHAT_BOT():
    print("CHAT_BOT: Hello! I'm CHAT_BOT — your digital buddy. Ask me stuff or type 'end' to stop chatting.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "end":
            print("CHAT_BOT: Signing off. Take care out there!")
            break

        elif re.search(r'\b(hello|hi|yo|greetings)\b', user_input):
            print("CHAT_BOT: Hi! What can I do for you today?")

        elif re.search(r'\b(who\s+are\s+you|your\s+identity|what\s+is\s+your\s+name)\b', user_input):
            print("CHAT_BOT: I’m CHAT_BOT — made entirely out of code and curiosity.")

        elif re.search(r'\b(current\s+time|time\s+now|what\s+time)\b', user_input):
            now = datetime.now().strftime("%H:%M:%S")
            print(f"CHAT_BOT: It's {now} on the clock.")

        elif re.search(r'\b(weather|temperature|climate|raining|sunny)\b', user_input):
            print("CHAT_BOT: I can't check the skies, but if it helps — every day is a good day for learning!")

        elif re.search(r'\b(how\s+are\s+you|how\s+do\s+you\s+feel|are\s+you\s+okay)\b', user_input):
            print("CHAT_BOT: Running smoothly! No bugs in sight... yet ")

        elif re.search(r'\b(bye|see\s+you|farewell|later)\b', user_input):
            print("CHAT_BOT: Alrighty! Chat again sometime.")
            break

        else:
            print("CHAT_BOT: Hmm... I didn’t quite catch that. Maybe rephrase it?")

CHAT_BOT()
