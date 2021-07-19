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
    list_content = {'Negative': [], 'Neutral': [], 'Positive': []}

    for content in content_list:
        prediction = predict(content)['sentiment']
        if "Negative" in prediction:
            list_content["Negative"].append(content)
        elif "Neutral" in prediction:
            list_content["Neutral"].append(content)
        elif "Positive" in prediction:
            list_content["Positive"].append(content)

    return list_content


def clean_old_answer():
    negative.config(text="Negative : ")
    list_negative.delete(1.0, tk.END)
    neutral.config(text="Neutral : ")
    list_neutral.delete(1.0, tk.END)
    positive.config(text="Positive : ")
    list_positive.delete(1.0, tk.END)


def print_answer(event):
    clean_old_answer()
    dict = classify_comment_in_post(entry.get())
    # dict = {'Negative': ["asdf"], 'Neutral': ["asdf", "Asdf"], 'Positive': ["asdf", "asdf"]}

    negative.config(text="Negative : " + str(len(dict['Negative'])))
    for content in dict['Negative']:
        list_negative.insert(tk.END, content + '\n\n')
    neutral.config(text="Neutral : " + str(len(dict['Neutral'])))
    for content in dict['Neutral']:
        list_neutral.insert(tk.END, content + '\n\n')
    positive.config(text="Positive : " + str(len(dict['Positive'])))
    for content in dict['Positive']:
        list_positive.insert(tk.END, content + '\n\n')


root = tk.Tk()
root.title("We\'re 5 Judgement Bot")
root.resizable(width=False, height=False)
root.configure(bg="white")

# back_ground = tk.PhotoImage(file = "background.png")
# canvas = tk.Canvas(root, width=1000, height=1000)
# canvas.create_image(0, 0, image = back_ground, anchor = "nw")
# canvas.grid(rowspan=5, columnspan=3)

logo = Image.open("logo.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, borderwidth=0)
logo_label.image = logo
logo_label.grid(row=0, column=2)

url_text = tk.Label(master=root, text="URL", bg="white", font="Raleway", padx=10, pady=10)
url_text.grid(row=1, column=2)
entry = tk.Entry(master=root, font="Raleway", width=50)
entry.grid(row=2, column=2)

empty1 = tk.Label(root, text="____", font="Raleway", fg="white", bg="white")
empty1.grid(row=3, column=0)
negative = tk.Label(root, text="Negative : ", font="Raleway", fg="red", bg="white")
negative.grid(row=3, column=1)
neutral = tk.Label(root, text="Neutral : ", font="Raleway", fg="#ed9b2b", bg="white")
neutral.grid(row=3, column=2)
positive = tk.Label(root, text="Positive : ", font="Raleway", fg="green", bg="white")
positive.grid(row=3, column=3)
empty2 = tk.Label(root, text="____", font="Raleway", fg="white", bg="white")
empty2.grid(row=3, column=4)

list_negative = tk.Text(root, font="Raleway", bg="white", width=30)
list_negative.grid(row=4, column=1)
list_neutral = tk.Text(root, font="Raleway", bg="white", width=30)
list_neutral.grid(row=4, column=2)
list_positive = tk.Text(root, font="Raleway", bg="white", width=30)
list_positive.grid(row=4, column=3)

root.bind('<Return>', print_answer)

root.mainloop()

# https://www.rottentomatoes.com/m/black_widow_2021/reviews?type=user

# https://www.facebook.com/windows/posts/10158599769677669
# https://www.facebook.com/TeslaMotorsCorp/posts/867733636990431?__cft__[0]=AZWNwxZKpPbbBn4kghANiuXlpmT6CHldWbVdheR-eg-Rwnj_hH3hZE1T8vjRu0QMxti9aE3d_z2PFQ1D6kOwV6quGvLT-CuZotQnCI3vlnQVQ0ffMlNXN7SAD9Sw19AXAHg0cXxlUIsERYEbDeCnTunt&__tn__=%2CO%2CP-R