from chatterbot import ChatBot                              #Libraries that i used
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import threading

engine = pp.init()                                          #Used to add voice 0 means male voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(word):                                            #speak banaya voice ko string me convert krne ko
    engine.say(word)
    engine.runAndWait()

bot = ChatBot("My Bot")                                     #yeh bot h

convo = [
    'hello',
    'hello there',
    'what is your name?',
    'my name is shanks. i am created by shashank',
    'how are you?',
    'i am good, what about you?',
    'i am good too thanks',
    'thats great',
    'which city u live in?',
    'i usually live in peoples heart but u can think that i live in every device',
    ''

]

trainer=ListTrainer(bot)
trainer.train(convo)

main = Tk()                                          #Thinkter ka use krke banai window

main.geometry("500x650")
main.title("Shanks")

img = PhotoImage(file="SHANKS.png")
photoL = Label(main, image=img)
photoL.pack(pady=5)

def takeQuery():                                      #take query
    sr = s.Recognizer()
    sr.pause_threshold=1
    print("Shanks is listening please say something")
    with s.Microphone() as m:
        audio = sr.listen(m)
        query = sr.recognize_google(audio,language='eng-in')
        textF.delete(0, END)
        textF.insert(0, query)
        ask_from_shanks()

def ask_from_shanks():                                  #Bot ka jawab
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "You : " + query)
    msgs.insert(END, "Bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)

frame = Frame(main)
                                                                 #Scroll bar
sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="Ask from Shanks", font=("Verdana", 20), command=ask_from_shanks)
btn.pack()

def enter_function(event):                     #yeh taaki enter dabane par msg sent ho jaye button ka action daal diya enter se
    btn.invoke()

main.bind('<Return>', enter_function)

def repeatL():                                   #yeh taaki baar baar listen kare bot
    while True:
        takeQuery()

t = threading.Thread(target=repeatL)
t.start()

main.mainloop()

