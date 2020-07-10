import sys
import time
import tkinter as tk

counter = 120
def count_label(label):
    counter = 120
    def count():
        global counter
        if counter == 0:
            return
        if run:
            # Just beore starting
            if counter == 120:
                show = "Starting"
            else:
                show = str(counter)
            label['text'] = show
            #Increment the count after
            #every 1 second
            label.after(1000, count)
            counter -= 1

    count()

# While Running
def Start(mark):
   global run
   run = True
   count_label(mark)
   start['state'] = 'disabled'
   stop['state'] = 'normal'
   reset['state'] = 'normal'

# While stopped
def Stop():
   global run
   start['state'] = 'normal'
   stop['state'] = 'disabled'
   reset['state'] = 'normal'
   run = False

# For Reset
def Reset(label):
   global counter
   counter = 120
   if run == False:
      reset['state'] = 'disabled'
      label['text'] = 'Welcome'
   else:
      label['text'] = 'Start'
      start['state'] = 'normal'

if __name__=="__main__":
    root = tk.Tk()
    root.title("stopwatch")
    root.minsize(width=300, height=200)

    label = tk.Label(root, font = ("times ", 25, "bold"))
    label.pack()

    start = tk.Button(root, text='Start',width = 20, height = 1, font = "10", command=lambda: Start(label))
    stop = tk.Button(root, text='Stop', width=20, height = 1, font = "10", state='disabled', command=Stop)
    reset = tk.Button(root, text='Reset',width=20, height = 1, font = "10", state='disabled', command=lambda: Reset(label))

    start.pack()
    stop.pack()
    reset.pack()


    root.mainloop()
