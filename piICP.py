#!/usr/bin/env python3
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk
from tkinter.ttk import *


# Initialize tkinter
def ICP_standards():
    root = tk.Tk()
    root.title("ICP Standard cookbook By John")
    root.geometry("1024x600")
    root.resizable(width = False, height = False)

# Assign buttons for elements
    Al_button = tk.Button(root,
                          text = "Aluminium",
                          font = ("Arial", 15),
                          command = Al_click).grid(row = 1, column = 0,
                                                   padx = 10, pady = 10)
    Ca_button = tk.Button(root,
                          text = "Calcium",
                          font = ("Arial", 15)).grid(row = 1, column = 1,
                                                     padx = 10, pady = 10)
    Cu_button = tk.Button(root,
                          text = "Copper",
                          font = ("Arial", 15)).grid(row = 1, column = 2,
                                                     padx = 10, pady = 10)
    Fe_button = tk.Button(root,
                          text = "Iron",
                          font = ("Arial", 15)).grid(row = 1, column = 3,
                                                     padx = 10, pady =10)
    K_button = tk.Button(root,
                         text = "Potassium",
                         font = ("Arial", 15)).grid(row = 1, column = 4,
                                                    padx = 10, pady = 10)
    Mg_button = tk.Button(root,
                          text = "Magnesium",
                          font = ("Arial", 15)).grid(row = 1, column = 5,
                                                     padx = 10, pady = 10)
    Mn_button = tk.Button(root,
                          text = "Manganese",
                          font = ("Arial", 15)).grid(row = 2, column = 0,
                                                     padx = 10, pady = 10)
    Na_Button = tk.Button(root,
                          text = "Sodium",
                          font = ("Arial", 15)).grid(row = 2, column = 1,
                                                     padx = 10, pady = 10)
    P_button = tk.Button(root,
                         text = "Phosphorus",
                         font = ("Arial", 15)).grid(row = 2, column = 2,
                                                    padx = 10, pady = 10)
    S_button = tk.Button(root,
                         text = "Sulfur",
                         font = ("Arial", 15)).grid(row = 2, column = 3,
                                                    padx = 10, pady = 10)
    Zn_button = tk.Button(root,
                          text = "Zinc",
                          font = ("Arial", 15)).grid(row = 2, column = 4,
                                                     padx = 10, pady = 10)
    root.mainloop()


def Al_click():
    Al_stock_select = tk.Tk()
    Al_stock_select.title("ICP Standard cookbook By John")
    Al_stock_select.geometry("1024x600")
    Al_label = ttk.Label(Al_stock_select,
                         text = "Choose Stock Standard",
                         font = ("Arial", 25)).grid(row = 0, column = 0, columnspan = 5)
    Al_1000 = tk.Button(Al_stock_select,
                        font = ("Arial", 15),
                        text = "1,000 ppm Aluminium",
                        command = lambda: [Al_stock_1000(),Al_stock_select.destroy()]).grid(row = 1,
                                                                    column = 0,
                                                                    padx = 20, pady = 20)
    Al_10000 = tk.Button(Al_stock_select,
                         font = ("Arial", 15), text = "10,000 ppm Aluminium",
                         command = lambda: [Al_stock_10000(), Al_stock_select.destroy()]).grid(row = 2, column = 0,
                                                                    padx = 20, pady = 20)

def Al_stock_1000():
    Al_Check_1 = tk.IntVar()
    Al_Check_2 = tk.IntVar()
    Al_Check_3 = tk.IntVar()
    Al_Check_4 = tk.IntVar()
    Al_1000 = tk.Tk()
    Al_1000.title("ICP Standard cookbook By John")
    Al_1000.geometry("1024x600")
    Al_std1 = ttk.Label(Al_1000,
                        text = "Add 0.625 mL of 1000 ppm Al Stock",
                        font = ("Arial", 15)).grid(row = 0, column = 3)
    Al_std2 = ttk.Label(Al_1000,
                        text = "Add 6.25 mL of 1000 ppm Al Stock",
                        font = ("Arial", 15)).grid(row = 1, column = 3)
    Al_std3 = ttk.Label(Al_1000,
                        text = "Add 12.5 mL of 1000 ppm Al Stock",
                        font = ("Arial", 15)).grid(row = 2, column = 3)
    Al_std4 = ttk.Label(Al_1000,
                        text = "Add 25 mL of 1000 ppm Al Stock",
                        font = ("Arial", 15)).grid(row = 3, column = 3)
    close = tk.Button(Al_1000,
                      font = ("Arial", 15),
                      text = "Close",
                      command = lambda: [Al_1000.destroy()]).grid(row = 4, column = 0)
    std1_check = tk.Checkbutton(Al_1000, text = "STD 1: 2.5 ppm",
                               font = ("Arial", 15),
                               bd = (15),
                               variable = Al_Check_1,
                               onvalue = 1,
                               offvalue = 0,
                               height = 2,
                               width = 10).grid(row = 0, column = 0, padx = 20, pady = 20)
    std2_check = tk.Checkbutton(Al_1000, text = "STD 2: 25 ppm",
                               font = ("Arial", 15),
                               bd = 15,
                               variable = Al_Check_2,
                               onvalue = 1,
                               offvalue = 0,
                               height = 2,
                               width = 10).grid(row = 1, column = 0, padx = 20, pady = 20)
    std3_check = tk.Checkbutton(Al_1000, text = "STD 3: 50 ppm",
                               font = ("Arial", 15),
                               bd = 15,
                               variable = Al_Check_3,
                               onvalue = 1,
                               offvalue = 0,
                               height = 2,
                               width = 10).grid(row = 2, column = 0, padx = 20, pady = 20)
    std4_check = tk.Checkbutton(Al_1000, text = "STD 4: 100 ppm",
                               font = ("Arial", 15),
                               bd = 15,
                               variable = Al_Check_4,
                               onvalue = 1,
                               offvalue = 0,
                               height = 2,
                               width = 10).grid(row = 3, column = 0, padx = 20, pady = 20)

def Al_stock_10000():
    Al_Check_1 = tk.IntVar()
    Al_Check_2 = tk.IntVar()
    Al_Check_3 = tk.IntVar()
    Al_Check_4 = tk.IntVar()
    Al_10000 = tk.Tk()
    Al_10000.title("ICP Standard cookbook By John")
    Al_10000.geometry("1024x600")
    Al_std1 = ttk.Label(Al_10000,
                        text = "Add 0.0625 mL of 1000 ppm Al Stock",
                        font = ("Arial", 15)).grid(row = 0, column = 3)
    Al_std2 = ttk.Label(Al_10000,
                        text = "Add 0.625 mL of 1000 ppm Al Stock",
                        font = ("Arial", 15)).grid(row = 1, column = 3)
    Al_std3 = ttk.Label(Al_10000,
                        text = "Add 1.25 mL of 1000 ppm Al Stock",
                        font = ("Arial", 15)).grid(row = 2, column = 3)
    Al_std4 = ttk.Label(Al_10000,
                        text = "Add 2.5 mL of 1000 ppm Al Stock",
                        font = ("Arial", 15)).grid(row = 3, column = 3)
    close = tk.Button(Al_10000,
                      text = "Close",
                      font = ("Arial", 15),
                      command = lambda: [Al_10000.destroy()]).grid(row = 4, column = 0)
    STD1_check = tk.Checkbutton(Al_10000, text = "STD 1: 2.5 ppm",
                               font = ("Arial", 15),
                               bd = (15),
                               variable = Al_Check_1,
                               onvalue = 1,
                               offvalue = 0,
                               height = 2,
                               width = 10).grid(row = 0, column = 0, padx = 20, pady = 20)
    STD2_check = tk.Checkbutton(Al_10000, text = "STD 2: 25 ppm",
                               font = ("Arial", 15),
                               bd = 15,
                               variable = Al_Check_2,
                               onvalue = 1,
                               offvalue = 0,
                               height = 2,
                               width = 10).grid(row = 1, column = 0, padx = 20, pady = 20)
    STD3_check = tk.Checkbutton(Al_10000, text = "STD 3: 50 ppm",
                               font = ("Arial", 15),
                               bd = 15,
                               variable = Al_Check_3,
                               onvalue = 1,
                               offvalue = 0,
                               height = 2,
                               width = 10).grid(row = 2, column = 0, padx = 20, pady = 20)
    STD4_check = tk.Checkbutton(Al_10000, text = "STD 4: 100 ppm",
                               font = ("Arial", 15),
                               bd = 15,
                               variable = Al_Check_4,
                               onvalue = 1,
                               offvalue = 0,
                               height = 2,
                               width = 10).grid(row = 3, column = 0, padx = 20, pady = 20)

icp = ICP_standards()
