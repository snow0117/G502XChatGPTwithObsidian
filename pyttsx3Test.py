import pyttsx3

def list_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for index, voice in enumerate(voices):
        print(f"Voice {index}: {voice.name} - {voice.id}")

def text_to_speech(word, voice_index):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_index].id)
    engine.say(word)
    engine.runAndWait()

list_voices()

word = "Hello"
voice_index = int(input("Enter the voice index for English pronunciation: "))
text_to_speech(word, voice_index)

