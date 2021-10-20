from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql
import random
import time
import mysql.connector
import pyodbc
from decimal import Decimal
import pandas as pd
import numpy as np
from tkinter import filedialog

def ataskaitos():
    master = Tk()
    master.geometry("1280x720")
    master.geometry("800x680+0+0")
    master.configure(background = 'gainsboro')




    # Data_nuo = StringVar()
    # Data_iki = StringVar()
    # Kaina_nuo = DoubleVar()
    # Kaina_iki = DoubleVar()

    MainFrame1 = Frame(master, bd = 10, width = 800, height = 680, relief = RIDGE)
    MainFrame1.grid()


    TopFrame5 = Frame(MainFrame1, bd = 5, width = 780, height = 660, relief = RIDGE, bg ='cadet blue')
    TopFrame5.grid(row = 0, column = 0)
    InnerTopFrame5 = Frame(TopFrame5, bd = 5, width = 770, height = 650, relief = RIDGE)
    InnerTopFrame5.grid()

    scroll_x1 = Scrollbar(InnerTopFrame5, orient = HORIZONTAL)
    scroll_y1 = Scrollbar(InnerTopFrame5, orient = VERTICAL)

    scroll_x1.pack(side = BOTTOM, fill = X)
    scroll_y1.pack(side = RIGHT, fill = Y)

    # scroll_x1 = ttk.Scrollbar(master, orient = "vertical")
    # scroll_y1 = ttk.Scrollbar(master, orient = "horizontal")

    tree_records1 = ttk.Treeview(InnerTopFrame5, height = 30, columns = ("Pavadinimas", "Sum of Kaina", "Sum of Kiekis"), xscrollcommand = scroll_x1.set, yscrollcommand = scroll_y1.set)

    tree_records1.heading("Pavadinimas", text = "Pavadinimas")
    tree_records1.heading("Sum of Kaina", text = "Sum of Kaina")
    tree_records1.heading("Sum of Kiekis", text = "Sum of Kiekis")

    tree_records1['show'] = "headings"

    tree_records1.column("Pavadinimas", width = 300, anchor = tkinter.W)
    tree_records1.column("Sum of Kaina", width = 80, anchor = tkinter.W)
    tree_records1.column("Sum of Kiekis", width = 80, anchor = tkinter.W)

    tree_records1.pack(fill = BOTH, expand = 1)

    df = pd.read_excel(r"C:/Users/justa/Desktop/Report.xlsx")
    df.head()
    pd.pivot_table(df,index=["Row Labels"])
    for _ in range(len(df.index.values)): # use for loop to get values in each line, _ is the number of line.
        if _ == 0 or _ == 7:
            tree_records1.insert('','end',value="")
            tree_records1.insert('','end',value="-----Formatas-----")
            tree_records1.insert('','end',value=tuple(df.iloc[_,[0]].values))
            tree_records1.insert('','end',value="")
        elif _ == 20:
            tree_records1.insert('','end',value="")
            tree_records1.insert('','end',value=tuple(df.iloc[_,[0,1,2]].values))

        else:
            tree_records1.insert('','end',value=tuple(df.iloc[_,[0,1,2]].values)) # [_,[1,2]] represents that you will get the values of second column and third column for each line.
    
