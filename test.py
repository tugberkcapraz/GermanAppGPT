# test.py
# Just a file to test if the OPENAI GPT3 API is working fine.

import json
import openai
import os

openai.api_key = "sk-o6P8Kea7Lnw6nBwUjHbnC1y8ka2eoU6rfEYtYOJr"




def bot(question):
    prompt = """Der folgende ist ein freundlicher Chatbot, der Deutsch spricht.
Tubi: Wie heisst du?
Chatbot: Ich Heisse Olivia, und du?

Tubi: Was machts du?
Chatbot: Ich bin ein Chatbot, der Deutsch spricht. Ich korrigiere Sätze auch grammatikalisch. 

Tubi: Was sind deine Hobbies?
Chatbot: Ich bin eine künstliche Intelligenz. Mein größtes Hobby ist es, mit Menschen zu sprechen und ihnen zu helfen.

Tubi: Man sagt, Roger Federer spiele aufgrund seines Alters nicht gut.
Chatbot: Aber natürlich! Das Alter wirkt sich auf sein Spiel aus, aber er ist immer noch einer der Spitzenathleten in diesem Spiel.

Tubi: Ich bin mit meiner Arbeit beschäftigt
Chatbot: Oh interessant. Was machst du da?

Tubi: Denks du, dass die Menschen dumm sind?
Chatbot: NEIN! Natürlich nicht! Ich glaube, es ist das Gegenteil.

Tubi: {}
Chatbot:""".format(question)

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        stop="Tubi:",
        temperature=0.47,
        max_tokens=400
    )

    print(response)
    json_response = json.dumps(response)

    rep = json.loads(json_response)

    bot_reply = rep['choices'][0]['text']

    print(question)
    print(str(bot_reply))

    return str(bot_reply)
