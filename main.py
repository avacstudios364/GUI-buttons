from tkinter import *

window = Tk()
window.geometry('700x600')
window.title('4 buttons')

top_button = Button(window, text = 'This is on the top', background = 'red', command = window.destroy)
top_button.pack(side = 'top')

left_button = Button(window, text = 'This is on the left', background = 'green', command = window.destroy)
left_button.pack(side = 'left')

bottom_button = Button(window, text = 'This is on the bottom', background = 'purple', command = window.destroy)
bottom_button.pack(side = 'bottom')

right_button = Button(window, text = 'This is on the right', background = 'yellow', command = window.destroy)
right_button.pack(side = 'right')

window.mainloop()
