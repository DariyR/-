from tkinter import *
from tkinter import messagebox

root = Tk()


def shifr():
    text1 = LoginInput.get()
    text = list(text1)
    key = int(keyInput.get())
    list_fg = []
    part = ""
    answer = ""
    true_key = key
    while 0 < key:
        for i in range(key - 1, len(text), int(true_key)):
            part += text[i]
        list_fg.append(part)
        key -= 1
        part = ""

    for i in list_fg:
        answer += i

    info = answer
    result_label.config(text=info)

    messagebox.showinfo(title='зашифровано', message=info)


root['bg'] = 'white'
root.title('Шифрування')
root.wm_attributes('-alpha', 1)
root.geometry('600x550')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=600, width=550)
canvas.pack()

frame = Frame(root, bg='#C0C0C0')
frame.place(relwidth=0.7, relheight=0.7,
            relx=0.15, rely=0.15)
title = Label(frame, text='розшифруй', bg='gray', font=40)
title.pack()

btn = Button(frame, text='button', bg='#808080', font=30, command=shifr)
btn.pack()

LoginInput = Entry(frame, bg='#83CCF3')
LoginInput.pack()

keyInput = Entry(frame, bg='#83CCF3')
keyInput.pack()

result_label = Label(frame, bg='#83CCF3', )
# result_label.place(relwidth=1.2, relheight=1.2, relx=0.45, rely=0.45)
result_label.pack()

root.mainloop()