from gtts import gTTS
import os

if __name__=='__main__':
    print("--welcome--")
    while True:
        text=input("enter a text or type 'done' to exit: ")
        if text.lower=='done':
            print("program ended!!")
            break
        tts=gTTS(text=text, lang='en')
        tts.save("output.mp3")

    os.system("start output.mps")
