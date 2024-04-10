import tkinter as tk

def button1_click():
    print("Button 1 clicked!")

def button2_click():
    print("Button 2 clicked!")

root = tk.Tk()
root.title("Button Click Example")

# Create a label widget to display some text
label = tk.Label(root, text="Click a button:")
label.pack()

# Create button 1
button1 = tk.Button(root, text="Button 1", command=button1_click)
button1.pack()

# Create button 2
button2 = tk.Button(root, text="Button 2", command=button2_click)
button2.pack()

root.mainloop()
