#!/usr/bin/env python3
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk
from tkinter.ttk import *

class GUI:

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
                            command = lambda: [GUI.stock_conc("Aluminium")]).grid(row = 1, column = 0,
                                                    padx = 10, pady = 10)
        Ca_button = tk.Button(root,
                            text = "Calcium",
                            font = ("Arial", 15),
                            command = lambda: [GUI.stock_conc("Calcium")]).grid(row = 1,
                                                                                column = 1,
                                                                                padx = 10,
                                                                                pady = 10)
        Cu_button = tk.Button(root,
                            text = "Copper",
                            font = ("Arial", 15),
                            command = lambda: [GUI.stock_conc("Copper")]).grid(row = 1,
                                                                               column = 2,
                                                                               padx = 10,
                                                                               pady = 10)
        Fe_button = tk.Button(root,
                            text = "Iron",
                            font = ("Arial", 15),
                            command = lambda: [GUI.stock_conc("Iron")]).grid(row = 1,
                                                                            column = 3,
                                                                            padx = 10,
                                                                            pady =10)
        K_button = tk.Button(root,
                            text = "Potassium",
                            font = ("Arial", 15),
                            command = lambda: [GUI.stock_conc("Potassium")]).grid(row = 2,
                                                                                 column = 1,
                                                                                 padx = 10,
                                                                                 pady = 10)
        Mg_button = tk.Button(root,
                            text = "Magnesium",
                            font = ("Arial", 15),
                            command = lambda: [GUI.stock_conc("Magnesium")]).grid(row = 2,
                                                                                 column = 2,
                                                                                 padx = 10,
                                                                                 pady = 10)
        Mn_button = tk.Button(root,
                            text = "Manganese",
                            font = ("Arial", 15),
                            command = lambda: [GUI.stock_conc("Manganese")]).grid(row = 2,
                                                                                 column = 3,
                                                                                 padx = 10,
                                                                                 pady = 10)
        Na_Button = tk.Button(root,
                            text = "Sodium",
                            font = ("Arial", 15),
                            command = lambda: [GUI.stock_conc("Sodium")]).grid(row = 3,
                                                                              column = 0,
                                                                              padx = 10,
                                                                              pady = 10)
        P_button = tk.Button(root,
                            text = "Phosphorus",
                            font = ("Arial", 15),
                            command = lambda: [GUI.stock_conc("Phosphorus")]).grid(row = 3,
                                                                                  column = 1,
                                                                                  padx = 10,
                                                                                  pady = 10)
        S_button = tk.Button(root,
                            text = "Sulfur",
                            font = ("Arial", 15),
                            command = lambda: [GUI.stock_conc("Sulfur")]).grid(row = 3,
                                                                              column = 2,
                                                                              padx = 10,
                                                                              pady = 10)
        Zn_button = tk.Button(root,
                            text = "Zinc",
                            font = ("Arial", 15),
                            command = lambda: [GUI.stock_conc("Zinc")]).grid(row = 3,
                                                                            column = 3,
                                                                            padx = 10,
                                                                            pady = 10)
        root.mainloop()

    def stock_conc(element):
        stock_select = tk.Tk()
        stock_select.title("ICP Standard Cookbook by John")
        stock_select.geometry("1024x600")
        choose_label = tk.Label(stock_select,
                                text = "Choose " + element + " Stock Standard",
                                font = ("Arial", 25)).grid(row = 0, column =0, columnspan = 5)
        ppm_1000 = tk.Button(stock_select,
                             font = ("Arial", 15),
                             text = "1,000 ppm " + element,
                             command = lambda: [GUI.desired_conc(),
                                                stock_select.destroy()]).grid(row = 1,
                                                                              column = 0,
                                                                              pady = 20)
        ppm_10000 = tk.Button(stock_select,
                             font = ("Arial", 15),
                             text = "10,000 ppm " + element,
                             command = lambda: [GUI.desired_conc(),
                                                stock_select.destroy()]).grid(row = 2,
                                                                              column = 0,
                                                                              pady = 20)

    def desired_conc():
        conc_select = tk.Tk()
        conc_select.title("ICP Standard Cookbook by John")
        conc_select.geometry("1024x600")
        check1 = tk.IntVar()
        check2 = tk.IntVar()
        check3 = tk.IntVar()
        check4 = tk.IntVar()
        check5 = tk.IntVar()
        check6 = tk.IntVar()
        check7 = tk.IntVar()
        check8 = tk.IntVar()
        check9 = tk.IntVar()
        check10 = tk.IntVar()
        check11 = tk.IntVar()
        check12 = tk.IntVar()
        check13 = tk.IntVar()
        check14 = tk.IntVar()
        conc_1 = tk.Checkbutton(conc_select,
                                text = "0.25 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check1,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 0, column = 0, padx = 10, pady = 10)
        conc_2 = tk.Checkbutton(conc_select,
                                text = "0.50 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check2,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 0, column = 1, padx = 10, pady = 10)
        conc_3 = tk.Checkbutton(conc_select,
                                text = "1.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check3,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 0, column = 2, padx = 10, pady = 10)
        conc_4 = tk.Checkbutton(conc_select,
                                text = "2.5 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check4,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 0, column = 3, padx = 10, pady = 10)
        conc_5 = tk.Checkbutton(conc_select,
                                text = "5.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check5,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 1, column = 0, padx = 10, pady = 10)
        conc_6 = tk.Checkbutton(conc_select,
                                text = "10.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check6,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 1, column = 1, padx = 10, pady = 10)
        conc_7 = tk.Checkbutton(conc_select,
                                text = "20.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check7,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 1, column = 2, padx = 10, pady = 10)
        conc_8 = tk.Checkbutton(conc_select,
                                text = "25.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check8,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 1, column = 3, padx = 10, pady = 10)
        conc_9= tk.Checkbutton(conc_select,
                                text = "40.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check9,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 2, column = 0, padx = 10, pady = 10)
        conc_10 = tk.Checkbutton(conc_select,
                                text = "50.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check10,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 2, column = 1, padx = 10, pady = 10)
        conc_11 = tk.Checkbutton(conc_select,
                                text = "100.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check11,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 2, column = 2, padx = 10, pady = 10)
        conc_12 = tk.Checkbutton(conc_select,
                                text = "200.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check12,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 2, column = 3, padx = 10, pady = 10)
        conc_13 = tk.Checkbutton(conc_select,
                                text = "400.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check13,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 3, column = 0, padx = 10, pady = 10)
        conc_14 = tk.Checkbutton(conc_select,
                                text = "800.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check14,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10).grid(row = 3, column = 1, padx = 10, pady = 10)

class control:

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
                            command = lambda: [control.Al_stock_1000(),Al_stock_select.destroy()]).grid(row = 1,
                                                                        column = 0,
                                                                        padx = 20, pady = 20)
        Al_10000 = tk.Button(Al_stock_select,
                            font = ("Arial", 15), text = "10,000 ppm Aluminium",
                            command = lambda: [control.Al_stock_10000(), Al_stock_select.destroy()]).grid(row = 2, column = 0,
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

icp_gui = GUI.ICP_standards()
