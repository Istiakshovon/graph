from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Graph")
root.geometry("500x500")

def graph():
    house_price = np.random.normal(200000,25000,5000)
    plt.hist(house_price, 50)
    plt.show()

button = Button(root, text="Graph it!", command=graph)
button.pack()


root.mainloop()