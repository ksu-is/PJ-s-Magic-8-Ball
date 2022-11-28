from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import random
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.Ctk()

root.title('Tkinter.com - Magic 8-Ball')
root.iconbitmap()
root.geometry("500X500")

def shake():
    responses = [
        "It is certain.": "green",
        "It is decidedly so.": "green",
        "Without a doubt.": "green",
        "Yes definitely.": "green",
        "You may rely on it.": "green",
        "As I see it, yes.": "green",
        "Most likely.": "green",
        "Outlook good.": "green",
        "Yes.": "green",
        "Signs point to yes.": "green",
        "Reply hazy, try again.": "yellow",
        "Ask again later.": "yellow",
        "Better not tell you now.": "yellow",
        "Cannot predict now.": "yellow",
        "Concentrate and ask again.": "yellow",
        "Do not count on it.": "red",
        "My reply is no.": "red",
        "My sources say no.": "red",
        "Outlook not so good.": "red",
        "Very doubtful.": "red"]
    responses_list = list(responses.items())

    random.shuffle(responses_list)
    print(responses_list)

    results.config(text=responses_list[0][0], fg=responses_list[0][1])

ball = ImageTk.PhotoImage(Image.open("C:"))
ball_img = Label(root, image=ball, bd=0)
ball_img.pack(pady=35)

results = Label(root, text="", font=("Helvetica", 28), bg= "#1a1a1a")
results.pack(pady=20)

ball_button = customtkinter.CTkButton(master=root, text= "Shake the Magic 8 ball!", width= 190, height=40, compound="top", command=shake)
ball_button.pack(pady=30)