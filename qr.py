import qrcode

# В цикле тру попросить ввод данных
# На esc выходить из проги
# Цветной текст colorama
# Мордочка на Tkinter
# Ввод имени файла, может быть = самому тексту

while True:
    # Ввод данных
    print("Введите текст для кодирования: ")
    data = input()

    # Генерируем qr-код
    img = qrcode.make(data)

    # Сохраняем img в файл
    img.save("{}.png".format(data))
