from tkinter import *
from tkinter import messagebox

root = Tk()#створюємо вікно

def btn_click():
    text1 = loginInput.get()
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

    messagebox.showinfo(title='зашифровано', message=info)#використовуємо для виводу інформації

    #Вікно з помилкою
    #messagebox.showerror(title='', message='Error')#використовуємо для виводу інформації

root['bg'] = '#fafafa'#добавили задній фон
root.title("Чистокіл")#добавили назву вікна
#root.wm_attributes('-alpha', 0.95)#добавили прозорість вікна
root.geometry('400x500')#ставимо розміри вікна

root.resizable(width=False, height=False)#чи можна змінювати розмір вікна користувачу

canvas = Canvas(root, height=400, width=500)#дозволяє додати на поле різні графічні приколи
canvas.pack()

frame = Frame(root, bg='gray')#frame це рамка в якій можна легко розташувати всі потрібні елементи
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)#додає данний об'єкт на поле і можна його розтажувати

title = Label(frame, text='Введіть тект нижче \nдля виконання функції', bg="yellow")#за допомогою Label додаємо текст
title.pack()

loginInput = Entry(frame, bg='white')#Додаємо текстове поле
loginInput.pack()

keyInput = Entry(frame, bg='white')#Додаємо текстове поле
keyInput.pack()

btn = Button(frame, text='Натисніть', bg="blue", command=btn_click)#додаємо кнопку. За допомогою команди 'command' задаємо функцію яка буде виконуватися після натиснення кнопки
btn.pack()

result_label = Label(frame, bg='#83CCF3', )
# result_label.place(relwidth=1.2, relheight=1.2, relx=0.45, rely=0.45)
result_label.pack()

root.mainloop()#база