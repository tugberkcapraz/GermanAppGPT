# test.py
# Just a file to test if the OPENAI GPT3 API is working fine.

import json
import openai
import os

openai.api_key = "sk-zIUrDSkQfVHgwZOCoO0uBIGFeX9FVMFqb3hde00B"




def bot(question):
    prompt = """es folgt ein Gespräch zwischen dem Grammatikkorrektur-Bot Oli und dem Menschen. Oli korrigiert Sätze auf Deutsch.
Tubi: Ich möchte geld haben von mein konto.
Oli: Ich möchte Geld von meinem Bankkonto abheben.

Tubi: Ich arbeite beiPlusdental zeit zwei Jahr.
Oli: Ich arbeite seit zwei Jahren bei Plusdental.

Tubi: Meine richtig Name ist Tugberk, aber meine freunde rufen mir Tubi. Das ist meine nickname.
Oli: Mein richtiger Name ist Tugberk, aber meine Freunde nennen mich tubi. Das ist mein Spitzname.

Tubi: Der Künstlicher Inteligenz korrigiert meine Grammatik in Deutsch. Es ist wunderbar!
Oli: Die künstliche Intelligenz korrigiert meine Grammatik auf Deutsch. Das ist wunderbar.

Tubi: Noam Chomsky ist eine groß Philosopher. Er schriebt mehrere Bücher über das Sprache
Oli: Noam Chomsky ist ein großer Philosoph. Er schrieb mehrere Bücher über die Sprache

Tubi: Wann kommst du? Ich brauche hilfe hier. Kanst du bitte mir einen pakette zigarette bringen?
Oli: Wann kommst du? Ich brauche hier Hilfe. Kanst du mir eine Schachtel Zigaretten mitbringen?

Tubi:Wie mann sagt "sub-atomic physics" auf Deutsch?
Oli: Wie mann sagt "sub-atomic physics" auf Deutsch?
Tubi: {}
Oli:""".format(question)

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        stop="Tubi:",
        temperature=0.23,
        max_tokens=150
    )

    print(response)
    json_response = json.dumps(response)

    rep = json.loads(json_response)

    bot_reply = rep['choices'][0]['text']

    print(question)
    print(str(bot_reply))

    return str(bot_reply)
