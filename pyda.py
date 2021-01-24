import tkinter as tk
import wolframalpha
import wikipedia
import json
from tkinter import messagebox
import os
import speech_recognition as sr

os.system("espeak 'Welcome'")
config={}
with open('config.json') as config_file:
    config = json.load(config_file)
api_key = config.get("api_key")
client = wolframalpha.Client(api_key)


class app(tk.Frame):

    def __init__(self):
        self.root= tk.Tk()
        self.canvas1 = tk.Canvas(self.root, width = 600, height = 100)
        self.canvas1.pack()
        self.label1 = tk.Label(self.root, text='Enter Your Search Query : ')
        self.canvas1.create_window(200, 20, window=self.label1)
        self.entry1 = tk.Entry(self.root)
        self.canvas1.create_window(300,50,window=self.entry1,height=40,width=500)
        self.root.bind('<Return>', self.getSearchResults)
        self.root.mainloop()

    def getSearchResults(self,event):
        my_input = self.entry1.get()
        if(my_input == ''):
            r=sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                my_input = r.recognize_google(audio)
            except sr.UnknownValueError:
                print("PyDa could not understand audio")
            except sr.RequestError as e:
                print("PyDa; {0}".format(e))
        try:
            print("trying from wolfram for {}".format(my_input))
            res = client.query(my_input)
            ans = next(res.results).text
            sp_var = "espeak ' Your Result "+ans+"'"
            os.system(sp_var)
            messagebox.showinfo("result",ans)
        except:
            try:
                print("trying from wikipedia for {}".format(my_input))
                ans = wikipedia.summary(my_input)
                sp_var = "espeak 'Wikipedia tells'"
                os.system(sp_var)
                messagebox.showinfo("result",ans)
            except:
                os.system("espeak 'Sorry, Nothing to Show! Please try modifying the query'")
                messagebox.showinfo("result","Sorry, Nothing to Show! Please try modifying the query")
        self.entry1.delete(0,tk.END)

myApp = app()

