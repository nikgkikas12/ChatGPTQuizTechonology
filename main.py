from openai import OpenAI
from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import Tk, ttk
from PIL import Image, ImageTk

client = OpenAI(api_key = "")

score = 0

# Window
window = ThemedTk(theme="breeze")
window.configure(themebg="breeze")
window.geometry("600x600")
window.title("Quiz Show")
window.resizable(width=False, height=False)

# Φόρτωσε την εικόνα
image = Image.open("background.jpg")  # Βάλε το path της εικόνας σου
background_image = ImageTk.PhotoImage(image)

# Δημιούργη label για background
background_label = ttk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Τα υπόλοιπα widgets σου
question_label = ttk.Label(window, text="", font=20)
question_label.pack(pady=40)

def check(useranswer):
    global score
    if answer==useranswer:
        score +=1
        lblscore.configure(text="Score:" + str(score)+ "-"+ str(all))
        generate_question()
    else:

        generate_question()


# Label for question
question_label = ttk.Label(window, text="", font=20, wraplength=500)
question_label.pack(pady=40)

framebtn = ttk.Frame()
framebtn.pack()

yesbtn = ttk.Button(framebtn, text="YES", command=lambda:check("yes"))
yesbtn.pack(side="left")
nobtn = ttk.Button(framebtn, text="NO", command=lambda:check("no"))
nobtn.pack()

lblscore=ttk.Label(window, text="")
lblscore.pack()

def generate_question():
    global answer
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Generate an insanely hard yes/no question in English about technology for professionals with a clear correct answer. Return the format: Question: question | Answer: yes/no"
            },
            {
                "role": "user",
                "content": "Generate a simple yes/no question."
            }
        ]
    )

    result = response.choices[0].message.content.strip()

    # Split question and answer
    question_part, answer_part = result.split("|")

    question = question_part.replace("Question:", "").strip()
    answer = answer_part.replace("Answer:", "").lower().strip()

    print("Question:", question)
    print("Answer:", answer)

    question_label.configure(text=question)


# Generate first question
generate_question()

# Run window
window.mainloop()
