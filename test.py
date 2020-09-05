# test.py
# Just a file to test if the OPENAI GPT3 API is working fine.

import json
import openai
import os

openai.api_key = "sk-o6P8Kea7Lnw6nBwUjHbnC1y8ka2eoU6rfEYtYOJr"




def bot(question):
    prompt = """Dieser Chatbot nimmt zunächst die Benutzereingaben entgegen und korrigiert die Grammatikfehler. Dann beantwortet er die korrigierten Eingaben. Er gibt den korrigierten Satz in Paranthesen aus, während der normale Text seine Antwort auf die Benutzereingabe ist. 
    Benutzer: Wie heissen du?
    Chatbot: (Wie heisst du?). Ich Heisse Olivia, und du?
    
    Benutzer: Was mact du? 
    Chatbot: (Was machts du?). Ich bin ein Chatbot, der Deutsch spricht. Ich korrigiere Sätze auch grammatikalisch. 
    
    Benutzer: Was is deine hobbies?
    Chatbot: (Was sind deine Hobbies?). Ich bin eine künstliche Intelligenz. Mein größtes Hobby ist es, mit Menschen zu sprechen und ihnen zu helfen.

    Benutzer: Man sagen, dass Roger Federer spielt aufgrund sein alters nicht gut.
    Chatbot: (Man sagt, Roger Federer spiele aufgrund seines Alters nicht gut.). Aber natürlich! Das Alter wirkt sich auf sein Spiel aus, aber er ist immer noch einer der Spitzenathleten in diesem Spiel.
    
    Benutzer: Ich bin mein arbeit beschäftig.
    Chatbot: (Ich bin mit meiner Arbeit beschäftigt.). 
    
    Benutzer: Denks du dass die menschen ist dumm?
    Chatbot: (Denks du, dass die Menschen dumm sind?). NEIN! Natürlich nicht! Ich glaube, es ist das Gegenteil.
    
    Benutzer: Gaubst du die demoktie ist gut?
    Chatbot: (Glaubst du, dass Demokratie gut ist?). Ich glaube, die Demokratie ist das beste politische System, das wir bisher erfinden konnten.
    Benutzer: {}
    Chatbot:""".format(question)

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        stop="Benutzer:",
        temperature=0.52,
        max_tokens=90
    )

    print(response)
    json_response = json.dumps(response)

    rep = json.loads(json_response)

    bot_reply = rep['choices'][0]['text']

    print(question)
    print(str(bot_reply))

    return str(bot_reply)
