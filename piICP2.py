#!/usr/bin/env python3
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk
from tkinter.ttk import *

class window:
    def new_window():
        window = tk.Tk()
        window.title = "ICP Standards Cookbook by John"
        window.geometry = ("1024x600")
        window.resizeable(width = False, height = False)

    def clear_window(frame):
        frame.destroy()

    def home_frame():
        element_frame = tk.Frame(root)
        element_frame.pack()
        Al_button = tk.Button(element_frame,
                                    text = "Aluminium",
                                    font = ("Arial", 18),
                                    command = lambda: [window.clear_window(element_frame),
                                                    control.stock_solutions("Aluminium")]).grid(row = 1, column = 0,
                                                            padx = 50, pady = 50)
        Ca_button = tk.Button(element_frame,
                                text = "Calcium",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_window(element_frame),
                                                control.stock_solutions("Calcium")]).grid(row = 1,
                                                                                        column = 1,
                                                                                        padx = 50,
                                                                                        pady = 50)
        Cu_button = tk.Button(element_frame,
                                text = "Copper",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_window(element_frame),
                                                control.stock_solutions("Copper")]).grid(row = 1,
                                                                                    column = 2,
                                                                                    padx = 50,
                                                                                    pady = 50)
        Fe_button = tk.Button(element_frame,
                                text = "Iron",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_window(element_frame),
                                                control.stock_solutions("Iron")]).grid(row = 1,
                                                                                    column = 3,
                                                                                    padx = 50,
                                                                                    pady =50)
        K_button = tk.Button(element_frame,
                                text = "Potassium",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_window(element_frame),
                                                control.stock_solutions("Potassium")]).grid(row = 2,
                                                                                        column = 1,
                                                                                        padx = 50,
                                                                                        pady = 50)
        Mg_button = tk.Button(element_frame,
                                text = "Magnesium",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_window(element_frame),
                                                control.stock_solutions("Magnesium")]).grid(row = 2,
                                                                                        column = 2,
                                                                                        padx = 50,
                                                                                        pady = 50)
        Mn_button = tk.Button(element_frame,
                                text = "Manganese",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_window(element_frame),
                                                control.stock_solutions("Manganese")]).grid(row = 2,
                                                                                        column = 3,
                                                                                        padx = 50,
                                                                                        pady = 50)
        Na_Button = tk.Button(element_frame,
                                text = "Sodium",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_window(element_frame),
                                                control.stock_solutions("Sodium")]).grid(row = 3,
                                                                                    column = 0,
                                                                                    padx = 50,
                                                                                    pady = 50)
        P_button = tk.Button(element_frame,
                                text = "Phosphorus",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_window(element_frame),
                                                control.stock_solutions("Phosphorus")]).grid(row = 3,
                                                                                        column = 1,
                                                                                        padx = 50,
                                                                                        pady = 50)
        S_button = tk.Button(element_frame,
                                text = "Sulfur",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_window(element_frame),
                                                control.stock_solutions("Sulfur")]).grid(row = 3,
                                                                                    column = 2,
                                                                                    padx = 50,
                                                                                    pady = 50)
        Zn_button = tk.Button(element_frame,
                                text = "Zinc",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_window(element_frame),
                                                control.stock_solutions("Zinc")]).grid(row = 3,
                                                                                    column = 3,
                                                                                    padx = 50,
                                                                                    pady = 50)

class control:
    def stock_solutions(element):
        element = element
        stock_select = tk.Frame(root)
        stock_select.pack()
        choose_label = tk.Label(stock_select,
                                text = "Choose " + element + " Stock Standard",
                                font = ("Arial", 25)).grid(row = 0, column =0, columnspan = 5)
        ppm_1000 = tk.Button(stock_select,
                             font = ("Arial", 18),
                             text = "1,000 ppm " + element,
                             command = lambda: [window.clear_window(stock_select),
                                                control.desired_conc(1000, element)]).grid(row = 1,
                                                                              column = 0,
                                                                              pady = 20)
        ppm_10000 = tk.Button(stock_select,
                             font = ("Arial", 18),
                             text = "10,000 ppm " + element,
                             command = lambda: [window.clear_window(stock_select),
                                                control.desired_conc(10000, element),]).grid(row = 2,
                                                                              column = 0,
                                                                              pady = 20)
        home_button = tk.Button(stock_select,
                                font = ("Arial", 18),
                                text = "Home",
                                command = lambda: [window.clear_window(stock_select),
                                    window.home_frame()]).grid(row = 3,
                                                                     column = 0,
                                                                     pady = 20)

    def desired_conc(stock_conc, element):
        element = element
        stock_conc = stock_conc
        conc_frame = tk.Frame(root)
        conc_frame.pack()
        concentrations = []
        conc_label = tk.Label(conc_frame,
                              text = "Select the 4 desired concentrations",
                              font = ("Arial", 18)).grid(row = 0, columnspan = 5)
        conc_1 = tk.Button(conc_frame,
                           text = "0.25 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(0.25),
                                              text.insert(tk.END, "0.25 ppm" + "\n")]).grid(row = 1, column = 0, padx = 25, pady = 30)
        conc_2 = tk.Button(conc_frame,
                           text = "0.50 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(0.50),
                                              text.insert(tk.END, "0.50 ppm" + "\n")]).grid(row = 1, column = 1, padx = 25, pady = 30)
        conc_3 = tk.Button(conc_frame,
                           text = "1.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(1.0),
                                              text.insert(tk.END, "1.0 ppm" + "\n")]).grid(row = 1, column = 2, padx = 25, pady = 30)
        conc_4 = tk.Button(conc_frame,
                           text = "2.5 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(2.5),
                                              text.insert(tk.END, "2.5 ppm" + "\n")]).grid(row = 1, column = 3, padx = 25, pady = 30)
        conc_5 = tk.Button(conc_frame,
                           text = "5.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(5.0),
                                              text.insert(tk.END, "5.0 ppm" + "\n")]).grid(row = 1, column = 4, padx = 25, pady = 30)
        conc_6 = tk.Button(conc_frame,
                           text = "10.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(10.0),
                                              text.insert(tk.END, "10.0 ppm" + "\n")]).grid(row = 2, column = 0, padx = 25, pady = 30)
        conc_7 = tk.Button(conc_frame,
                           text = "20.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(20.0),
                                              text.insert(tk.END, "20.0 ppm" + "\n")]).grid(row = 2, column = 1, padx = 25, pady = 30)
        conc_8 = tk.Button(conc_frame,
                           text = "25.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(25.0),
                                              text.insert(tk.END, "25.0 ppm" + "\n")]).grid(row = 2, column = 2, padx = 25, pady = 30)
        conc_9 = tk.Button(conc_frame,
                           text = "40.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(40.0),
                                              text.insert(tk.END, "40.0 ppm" + "\n")]).grid(row = 2, column = 3, padx = 25, pady = 30)
        conc_10 = tk.Button(conc_frame,
                           text = "50.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(50.0),
                                              text.insert(tk.END, "50.0 ppm" + "\n")]).grid(row = 2, column = 4, padx = 25, pady = 30)
        conc_11 = tk.Button(conc_frame,
                           text = "100.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(100.0),
                                              text.insert(tk.END, "100.0 ppm" + "\n")]).grid(row = 3, column = 0, padx = 25, pady = 30)
        conc_12 = tk.Button(conc_frame,
                           text = "200.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(200.0),
                                              text.insert(tk.END, "200.0 ppm" + "\n")]).grid(row = 3, column = 1, padx = 25, pady = 30)
        conc_13 = tk.Button(conc_frame,
                           text = "400.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(400.0),
                                              text.insert(tk.END, "400.0 ppm" + "\n")]).grid(row = 3, column = 2, padx = 25, pady = 30)
        conc_14 = tk.Button(conc_frame,
                           text = "800.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(800.0),
                                              text.insert(tk.END, "800.0 ppm" + "\n")]).grid(row = 3, column = 3, padx = 25, pady = 30)
        text = tk.Text(conc_frame,
                       height = 4,
                       width = 40,
                       font = ("Arial", 18))
        text.grid(row = 4, columnspan = 5, padx = 25, pady = 30)
        clear_button = tk.Button(conc_frame,
                                 text = "Clear Selection",
                                 font = ("Arial", 18),
                                 command = lambda: [concentrations.clear(),
                                                    text.delete("1.0", "end")]).grid(row = 5,
                                                                             column =1,
                                                                             padx = 10,
                                                                             pady = 10)
        conc_button = tk.Button(conc_frame,
                                text = "Accept STD concentrations:",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_window(conc_frame),
                                                   control.std_instructions(math.calculate_conc(stock_conc, concentrations), element)]).grid(row =5,
                                                                                         column = 2,
                                                                                         padx = 10,
                                                                                         pady = 10)
        home_button = tk.Button(conc_frame,
                                font = ("Arial", 18),
                                text = "Home",
                                command = lambda: [window.clear_window(conc_frame),
                                    window.home_frame()]).grid(row = 5,
                                                                     column = 0,
                                                                     pady = 20)

    def std_instructions(concentrations, element):
        instruct_frame = tk.Frame(root)
        instruct_frame.pack()
        text = tk.Text(instruct_frame,
                           height = 10,
                           width = 50,
                           font = ("Arial", 18))
        text.pack(padx = 25, pady = 30)
        for std in concentrations:
            text.insert(tk.END, str(std) + " uL " + " or " + str(std / 1000) + ' mL ' + "of " + element + "\n")

        home_button = tk.Button(instruct_frame,
                                font = ("Arial", 18),
                                text = "Home",
                                command = lambda: [window.clear_window(instruct_frame),
                                    window.home_frame()])
        home_button.pack(padx = 25, pady = 30)

class math:

    def calculate_conc(stock_concentrations, final_concentrations):
        stock = stock_concentrations
        final = final_concentrations
        std1 = (final[0]*250) / stock *1000
        std2 = (final[1]*250) / stock *1000
        std3 = (final[2]*250) / stock *1000
        std4 = (final[3]*250) / stock *1000
        std_lst = [std1, std2, std3, std4]
        return std_lst


# Create root GUI
root = tk.Tk()
root.title("ICP Standard cookbook By John")
root.geometry("1024x600")
root.resizable(width = False, height = False)
window.home_frame()


# Loop root window
root.mainloop()
