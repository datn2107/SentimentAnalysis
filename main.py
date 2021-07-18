import tkinter as tk

from PIL import Image, ImageTk
from transformers import pipeline

from crawl_comment import get_comment_in_post

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


def classify_comment_in_post(url):
    content_list = get_comment_in_post(url)
    count = {'Very Negative': 0, 'Negative': 0, 'Neutral': 0, 'Positive': 0, 'Very Positive': 0}

    for content in content_list:
        count[predict(content)['sentiment']] += 1

    return count


def print_answer(event):
    dict = classify_comment_in_post(entry.get())
    # dict = {'Very Negative': 12, 'Negative': 123, 'Neutral': 123, 'Positive': 123, 'Very Positive': 123}

    very_neg.config(text="Very Negative : " + str(dict['Very Negative']))
    neg.config(text="Negative : " + str(dict['Negative']))
    neutral.config(text="Neutral : " + str(dict['Neutral']))
    pos.config(text="Positive : " + str(dict['Positive']))
    very_pos.config(text="Very Positive : " + str(dict['Very Positive']))


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

frame = tk.Frame(root, bg="white")
frame.pack()

url_text = tk.Label(master=frame, text="URL: ", bg="white", font="Raleway", padx=10, pady=10)
url_text.grid(row=0, column=0)
entry = tk.Entry(master=frame, font="Raleway", width=50)
entry.grid(row=0, column=1)

very_neg = tk.Label(root, text="", font="Raleway", fg="red", bg="white")
very_neg.pack()
neg = tk.Label(root, text="", font="Raleway", fg="red", bg="white")
neg.pack()
neutral = tk.Label(root, text="", font="Raleway", fg="#ed9b2b", bg="white")
neutral.pack()
pos = tk.Label(root, text="", font="Raleway", fg="green", bg="white")
pos.pack()
very_pos = tk.Label(root, text="", font="Raleway", fg="green", bg="white")
very_pos.pack()

root.bind('<Return>', print_answer)
# root.bind('<Return>', lambda e: print("asdfsadf"))

root.mainloop()
