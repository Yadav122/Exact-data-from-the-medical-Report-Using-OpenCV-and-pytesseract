# import os
#
# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 1.1. Created by Harsh kumar")
#     x=input("Enter What yimport os
#
# if __name__ == '__main__':
#     print("Welcome to RoboSpeaker 1.1. Created by Harsh kumar")
#     x = input("Enter What you want me to Speak: ")
#     command = f'say "{x}"'  # Enclose the input string in double quotes
#     os.system(command)ou want me to Speak")
#     command=f'say "{x}"'
#    os.system(command)


import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Harsh kumar")

while (True):
            x = input("Enter What you want me to Speak: ")
            if x=="q":
                x=pyttsx3.init()
                x.say("Bye bye Friend")
                x.runAndWait()

                break

            # Initialize the text-to-speech engine
            engine = pyttsx3.init()

            # Say the input text
            engine.say(x)

            # Wait for the speech to finish
            engine.runAndWait()