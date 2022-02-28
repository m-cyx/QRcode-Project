from tkinter import *
import qrcode

# Отображение изображения
def showImg(imgName):
    root = Toplevel()
    root.title(imgName)
    img_gif = PhotoImage(file=imgName)
    label_img = Label(root, image=img_gif)
    label_img.pack()
    root.mainloop()

# Обработчик события 
def clicked():
    data = txt.get()

    # Генерируем qr-код
    qrimg = qrcode.make(data)

    # Сохраняем img в файл
    qrimg.save("{}.png".format(data))

    lbl.configure(text = "Вы сгенерировали QR с текстом:\n " + data)

    showImg("{}.png".format(data))


window = Tk()
window.title("Генератор Qr кодов Сухановой Мирославы")
window.geometry('400x200')

mainText = Label(window, text="Введите желаемый текст \n в поле ниже и нажмите кнопку", font=("Arial Bold", 20))
mainText.grid(column=0, row=0)

txt = Entry(window, width=10)
txt.grid(column=0, row=1)
txt.focus()

btn = Button(window, text="Сгенерировать!", command=clicked)
btn.grid(column=0, row=2)

lbl = Label(window, text="")
lbl.grid(column=0, row=3)

window.mainloop()



