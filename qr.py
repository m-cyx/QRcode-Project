import qrcode

# Генератор

while True:
    # Ввод данных
    print("Введите текст для кодирования: ")
    data = input()

    # Генерируем qr-код
    img = qrcode.make(data)

    # Сохраняем img в файл
    img.save("{}.png".format(data))
