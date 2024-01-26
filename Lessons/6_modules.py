import os
import random
import pyttsx3

# my_path = os.path.dirname(__file__)
# print(os.path.dirname(__file__))
# print(os.listdir(my_path))
# print(random.randint(1, 50))

with open("6_pep8.txt", "r", encoding="utf-8") as pep_file:
    pep_text = pep_file.read()

print(pep_text)

speaker = pyttsx3.init()
speaker.say(pep_text)
speaker.runAndWait()
speaker.stop()