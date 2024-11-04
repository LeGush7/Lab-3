import tkinter as tk
import pygame


alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
pictcount = 0


def key(block):
    if len(block) != 5:
        return 'неверная длина блока'
    part1 = block
    part2 = ''
    part3 = ''
    for x in range(5):
        positionalp = alphabet.find(block[x])
        positionnum = nums.find(block[x])
        if block[x].isdigit():
            part2 += nums[positionnum + 3
            if positionnum + 3 < 10 else positionnum + 3 - 10]
        elif block[x].isalpha() and block[x] in alphabet:
            part2 += alphabet[positionalp + 3
            if positionalp + 3 < 26 else positionalp + 3 - 26]
        else:
            return 'неверные символы в блоке'
    for x in range(5):
        positionalp = alphabet.find(block[x])
        positionnum = nums.find(block[x])
        if block[x].isdigit():
            part3 += nums[positionnum - 5
            if positionnum - 5 >= 0 else 5 + positionnum]
        elif block[x].isalpha() and block[x] in alphabet:
            part3 += alphabet[positionalp - 5
            if positionalp - 5 >= 0 else 21 + positionalp]
        else:
            return 'неверные символы в блоке'
    return part1 + '-' + part2 + '-' + part3


def buttonclc():
    inputtxt = enter.get().upper()
    output.config(text=f'Сгенерированный ключ: {key(inputtxt)}',
                        font=('Times New Roman', 14))


def music():
    pygame.mixer.music.load('kcdmusic.mp3')
    pygame.mixer.music.play(-1)


def pictchange():
    global pictcount
    if pictcount == 12:
        canvas.create_image(0, 0,
                            image=pictures[0], anchor='nw')
        pictcount = 0
    else:
        canvas.create_image(0, 0,
                            image=pictures[pictcount], anchor='nw')
    pictcount += 1
    root.after(110, pictchange)


pygame.init()
pygame.mixer.init()
root = tk.Tk()
root.title('Генератор ключа')
root.geometry('1200x630')

pictures = [tk.PhotoImage(file=f'KCD{i}.png') for i in range(0, 12)]
canvas = tk.Canvas(root, width=500, height=400)
canvas.pack(fill='both', expand=True)

enter = tk.Entry(root, font=('Times New Roman', 14))
canvas.create_window(600, 310, window=enter)

button = tk.Button(root, text='Показать ключ',
                   font=('Times New Roman', 14), command=buttonclc)
canvas.create_window(600, 410, window=button)

output = tk.Label(root, text='', font=('Times New Roman', 14),
                        bg='lightgrey', width=50)
canvas.create_window(600, 360, window=output)

music()
pictchange()
root.mainloop()
pygame.mixer.music.stop()
