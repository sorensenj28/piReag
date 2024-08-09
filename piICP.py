42#!/usr/bin/env python3
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

    def conc_checks():
        concentrations = [0.25, 0.50, 1.0, 2.5, 5.0, 10.0, 20.0, 25.0, 40.0, 50.0, 100.0,
                          200.0, 400.0, 800.0]
        checkbutton_vars = []
        concentration_for_standards = []
        conc_select = tk.Tk()
        conc_select.title("ICP Standard Cookbook by John")
        conc_select.geometry("1024x600")
        for i in range(14):
            if i <= 3:
                var = tk.IntVar()
                checkbutton_vars.append(var)
                checkbutton = tk.Checkbutton(conc_select,
                                            text = str(concentrations[i]) + "ppm",
                                            font = ("Arial", 15),
                                            bd = (15),
                                            variable = var,
                                            command = lambda: [concentration_for_standards.append(concentrations[i])]).grid(row = 0,
                                                                 column = i,
                                                                 padx = 10,
                                                                 pady = 10)
            elif i > 3 and i < 8:
                var = tk.IntVar()
                checkbutton_vars.append(var)
                checkbutton = tk.Checkbutton(conc_select,
                                            text = str(concentrations[i]) + "ppm",
                                            font = ("Arial", 15),
                                            bd = (15),
                                            variable = var).grid(row = 1,
                                                                 column = i - 4,
                                                                 padx = 10,
                                                                 pady = 10)
            elif i > 7 and i < 12:
                var = tk.IntVar()
                checkbutton_vars.append(var)
                checkbutton = tk.Checkbutton(conc_select,
                                            text = str(concentrations[i]) + "ppm",
                                            font = ("Arial", 15),
                                            bd = (15),
                                            variable = var).grid(row = 2,
                                                                 column = i - 8,
                                                                 padx = 10,
                                                                 pady = 10)
            elif i > 11:
                var = tk.IntVar()
                checkbutton_vars.append(var)
                checkbutton = tk.Checkbutton(conc_select,
                                            text = str(concentrations[i]) + "ppm",
                                            font = ("Arial", 15),
                                            bd = (15),
                                            variable = var).grid(row = 3,
                                                                 column = i - 12,
                                                                 padx = 10,
                                                                 pady = 10)
        conc_button = tk.Button(conc_select,
                                text = "Accept STD concentrations:",
                                font = ("Arial", 15),
                                command = lambda: [print(concentration_for_standards)]).grid(row =4,
                                                                       column = 2,
                                                                       padx = 10,
                                                                       pady = 10)

    def desired_conc():
        standards = []
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
                                width = 10,
                                command = lambda: standards.append(0.25)).grid(row = 0, column = 0, padx = 10, pady = 10)
        conc_2 = tk.Checkbutton(conc_select,
                                text = "0.50 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check2,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(0.50)).grid(row = 0, column = 1, padx = 10, pady = 10)
        conc_3 = tk.Checkbutton(conc_select,
                                text = "1.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check3,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(1.0)).grid(row = 0, column = 2, padx = 10, pady = 10)
        conc_4 = tk.Checkbutton(conc_select,
                                text = "2.5 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check4,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(2.5)).grid(row = 0, column = 3, padx = 10, pady = 10)
        conc_5 = tk.Checkbutton(conc_select,
                                text = "5.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check5,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(5.0)).grid(row = 1, column = 0, padx = 10, pady = 10)
        conc_6 = tk.Checkbutton(conc_select,
                                text = "10.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check6,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(10.0)).grid(row = 1, column = 1, padx = 10, pady = 10)
        conc_7 = tk.Checkbutton(conc_select,
                                text = "20.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check7,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(20.0)).grid(row = 1, column = 2, padx = 10, pady = 10)
        conc_8 = tk.Checkbutton(conc_select,
                                text = "25.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check8,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(25.0)).grid(row = 1, column = 3, padx = 10, pady = 10)
        conc_9= tk.Checkbutton(conc_select,
                                text = "40.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check9,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(40.0)).grid(row = 2, column = 0, padx = 10, pady = 10)
        conc_10 = tk.Checkbutton(conc_select,
                                text = "50.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check10,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(50.0)).grid(row = 2, column = 1, padx = 10, pady = 10)
        conc_11 = tk.Checkbutton(conc_select,
                                text = "100.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check11,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(100.0)).grid(row = 2, column = 2, padx = 10, pady = 10)
        conc_12 = tk.Checkbutton(conc_select,
                                text = "200.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check12,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(200.0)).grid(row = 2, column = 3, padx = 10, pady = 10)
        conc_13 = tk.Checkbutton(conc_select,
                                text = "400.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check13,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(400.0)).grid(row = 3, column = 0, padx = 10, pady = 10)
        conc_14 = tk.Checkbutton(conc_select,
                                text = "800.0 ppm",
                                font = ("Arial", 15),
                                bd = (15),
                                variable = check14,
                                onvalue = 1,
                                offvalue = 0,
                                height = 2,
                                width = 10,
                                command = lambda: standards.append(800.0)).grid(row = 3, column = 1, padx = 10, pady = 10)
        standards_label = tk.Label(conc_select,
                                   text = "Choose Concentrations",
                                   font = ("Arial", 15)).grid(row = 4, columnspan = 4)
        clear_button = tk.Button(conc_select,
                                 text = "Clear Selection",
                                 font = ("Arial", 15),
                                 command = lambda: [standards.clear()]).grid(row = 5,
                                                                             column =1,
                                                                             padx = 10,
                                                                             pady = 10)
        conc_button = tk.Button(conc_select,
                                text = "Accept STD concentrations:",
                                font = ("Arial", 15),
                                command = lambda: print(standards)).grid(row =5,
                                                                       column = 2,
                                                                       padx = 10,
                                                                       pady = 10)


icp_gui = GUI.ICP_standards()
