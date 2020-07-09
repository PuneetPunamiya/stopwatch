import sys
import time
import tkinter as tk

counter = 120
def counter_label(label):
    counter = 120
    def count():
        global counter

        if counter == 0:
            return

        counter = counter - 1
        label.config(text=str(counter))
        label.after(1000, count)

    count()

root = tk.Tk()
root.title("stopwatch")
label = tk.Label(root, font = ("times ", 20, "bold"),  width = 10)
label.pack()
counter_label(label)
button = tk.Button(root, text = "stop", width = 40, command = root.destroy)
button.pack()
root.mainloop()
