from Brain.AIBrain import ReplyBrain
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait for some seconds.")
from Body.Speak import Speak
from Features.Clap import Tester
# print(">> Starting The Jarvis : Wait for some more few seconds.")

def MainExecution():

    Speak("Hello Sir")
    Speak("I'm Jarvis, I'm Ready to Assist you Sir.")

    while True:

        Data = MicExecution()
        Data = str(Data)
        Reply = ReplyBrain(Data)
        Speak(Reply)

def ClapDetect():
    query = Tester()
    if "True-Mic" in query:
        print("")
        print(">> Clap Detected!! >>")
    else:
        pass

ClapDetect()

