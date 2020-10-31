# A.I mood detection GUI

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from textblob import TextBlob
import emoji

win = Tk()
win.geometry("200x200")
win.resizable(width=False, height=False)
win.title("Mood Detetor")

def mood():
    y = e1.get("1.0", "end-1c")
    edu = TextBlob(y)
    x = edu.sentiment.polarity
    if x<0:
        try:
            m1 = ("Negative sentence, demotivating", emoji.emojize(":disappointed_face:"))
            messagebox.showinfo("Mood Detector", f"{m1}")
        except:
            messagebox.showerror("Error", "Text box is empty!")

    elif x==0:
        try:
            m2 = ("Neutral", emoji.emojize(":zipper-mouth_face:"))
            messagebox.showinfo("Mood Detector", f"{m2}")
        except:
            messagebox.showerror("Error", "Text box is empty!")

    elif x>0 and x<=1:
        try:
            m3 = ("Positive, Joyfull", emoji.emojize(":grinning_face_with_big_eyes:"))
            messagebox.showinfo("Mood Detector", f"{m3}")
        except:
            messagebox.showerror("Error", "Text box is empty!")

Label(win, text = "Type your sentence: ", font = "-size 9 -weight bold").place(x = 40, y = 20)
b1 = Button(win, text="Decide Mood", command = mood, fg = "white", bg = "purple", font = "-size 9 -weight bold").place(x = 60, y = 160)

e1 = Text(win, height = 5, width = 20)
e1.place(x = 20, y = 50)

win.mainloop()
