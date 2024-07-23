

import random
import tkinter as tk

def noise(r,g,b):
    # выход за FF
    r += random.randint(40, 80)
    g += random.randint(40, 80)
    b += random.randint(40, 80)
    #print(*[r, g, b])
    return [r, g, b]

def add_noise(hex_rgb):
    assert (isinstance(hex_rgb, str) and hex_rgb[0] == '#' and len(hex_rgb) == 7)
    r = int(hex_rgb[1:3], 16)
    g = int(hex_rgb[3:5], 16)
    b = int(hex_rgb[5:7], 16)

    r, g, b = noise(r, g, b)

    return ["#" + hex(r)[2:].upper().rjust(2,'0') + hex(g)[2:].upper().rjust(2,'0') + hex(b)[2:].upper().rjust(2,'0'), [r, g, b]]


app = tk.Tk()
app.geometry('600x400+200+500')

def click():
    print('Clicked!')

row_num = 5
col_num = 5

Butons = []
buts_number = row_num*col_num
number_of_different_col = random.randrange(25)

but_side = 5
but_color = '#A000A0'

for row in range(row_num):
    for coll in range(col_num):

        if coll + row_num*row == number_of_different_col:
            col = add_noise(but_color)[0]
            print(col)

        else:
            col = but_color

        B = tk.Button(app, command=click, height=but_side, width=but_side, bg=col)
        Butons.append(B)

        c1 = 15
        c2 = 15

        B.place(x=c1*but_side*coll, y=c2*but_side*row)


#B1 = tk.Button(app, command=click, height = but_height, width=but_side, bg = '#FF00FF')
#B2 = tk.Button(app, command=click, height = but_side, width=but_side, bg = '#FF00FF')

# B1.place(x=10, y=10)
# B2.pack()

app.mainloop()

# print(add_noise(but_color)[0])
#
# print(add_noise(but_color)[1])

