import openai
import streamlit as website
import time
import keys
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

#generate response from gpt
def genResponse(user_prompt):
    completion = openai.Completion.create(
        engine='text-davinci-003',
        prompt=user_prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    response = completion.choices[0].text
    
    return response

def main():
    configure()
    openai.api_key = os.getenv('api_key')
    """
    #   What does the AI think about you?
    """
    your_sign = website.text_input("Enter your zodiac sign")

    your_name = website.text_input("Enter your Name")

    your_fav_color = website.text_input('Enter your favorite color')

    prompt = "Insult me based on these facts and make it cinematic, and very long: " + "My name is: " + your_name + ", " +  "My favorite color is: " + your_fav_color + ", " + "My zodiac sign is: " + your_sign + "."

    response = genResponse(prompt)

    website.write("Generating response...")

    time.sleep(5)

    website.write(response)
    
main()