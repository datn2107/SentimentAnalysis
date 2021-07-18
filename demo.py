import tkinter as tk

from PIL import Image, ImageTk
from transformers import pipeline

nlp = pipeline(task='sentiment-analysis',
               model='nlptown/bert-base-multilingual-uncased-sentiment')

def predict(text):
    result = nlp(text)

    if (result[0]['label'] == '1 star'):
        sent = 'Very Negative'
    elif (result[0]['label'] == '2 star'):
        sent = 'Negative'
    elif (result[0]['label'] == '3 stars'):
        sent = 'Neutral'
    elif (result[0]['label'] == '4 stars'):
        sent = 'Positive'
    else:
        sent = 'Very Positive'
    prob = result[0]['score']

    return {'sentiment': sent, 'probability': prob}


def predict_func(text):
    prediction = predict(text)['sentiment']
    if "Positive" in prediction:
        color = "green"
    elif "Neutral" in prediction:
        color = "#ed9b2b"
    else:
        color = "red"
    answer.config(text=prediction, fg=color)

def clear_func():
    text.delete(1.0, tk.END)
    answer.config(text="")


root = tk.Tk()
root.title("We\'re 5 Judgement Bot")
root.geometry("600x600")
root.resizable(width=False, height=False)
root.configure(bg="white")

logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, borderwidth=0)
logo_label.image = logo
logo_label.pack()

text = tk.Text(root, width=40, height=10, font="Raleway", borderwidth=2, relief="groove")
text.pack()

button_frame = tk.Frame(root)
button_frame.pack()

predict_btn = tk.Button(button_frame, text="Predict", command=lambda: predict_func(text.get(1.0, tk.END)),
                        font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
predict_btn.grid(row=0, column=0)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_func, font="Raleway", bg="#20bebe", fg="white",
                      height=2, width=15)
clear_btn.grid(row=0, column=1)

answer = tk.Label(root, text="", font="Raleway", bg="white")
answer.pack(padx=30, pady=30)

root.mainloop()
