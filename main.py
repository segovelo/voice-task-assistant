from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys

recognizer = speech_recognition.Recognizer

speaker = tts.init()
speaker.setProperty("rate",120)

todo_list = ["Go Shopping", "Watch coding videos"]

def hello():
    pass
def create_note():
    global recognizer
    speaker.say("What do would you like to write in your note?")
    speaker.runAndWait()
    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose a file name")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

                with open(filename, "w") as f:
                    f.write(note)
                    done = True
                    speaker.say(f"I successfully created the note {filename}")

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand! Please try again!")
            speaker.runAndWait()

def add_todo():
    global recognizer
    speaker.say("What do you want to add")
    speaker.runAndWait()

    done = False
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                item = recognizer.recognize_google(audio)
                item = item.lower()
                todo_list.append(item)
                done = True
        
                speaker.say(f"I added {item} to the to do List")
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I did not understand! Please try again!")
            speaker.runAndWait()




mappings = {"greeting": hello}
assistant = GenericAssistant("intents.json", intent_methods=mappings)

assistant.train_model()

assistant.request()