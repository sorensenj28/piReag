#!/usr/bin/env python3
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk

def get_recipe_lines():
    with open("piForm.txt", mode = "r") as file:
        recipe_lines = file.readlines()
        return recipe_lines

def tc_click(recipe_lines):
    tc_recipe = recipe_lines[0:10]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, tc_recipe)

def ic_click(recipe_lines):
    ic_recipe = recipe_lines[10:22]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, ic_recipe)

def tn_click(recipe_lines):
    tn_recipe = recipe_lines[22:34]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, tn_recipe)

# Initialize tkinter
root = tk.Tk()
root.title("piFormacs By John")
root.geometry("1024x600")
root.resizable(width = False, height = False)
recipes = get_recipe_lines()

# Add Scrollable Text Box
text = st.ScrolledText(root, width = 65, height = 6, font = ("arial", 17))
text.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady =10)

# Skalar Formacs TOC Labels
form_label = ttk.Label(root, text = "Skalar Formacs TOC Standards")
tc_label = ttk.Label(root, text = "Total Carbon Stock Standard")
ic_label = ttk.Label(root, text = "Inorganic Carbon Stock Standard")
tN_label = ttk.Label(root, text = "Total Nitrogen Stock Standard")
form_label.grid(row = 1, column = 0, columnspan = 4)
tc_label.grid(row = 2, column = 1)
ic_label.grid(row = 2, column = 2)
tN_label.grid(row = 2, column =3)


# Create Buttons for Formacs Stock Standards
tc = ttk.Button(root, text = "TC 1000 mg C/L", command = lambda: tc_click(recipes))
ic = ttk.Button(root, text = "IC 1000 mg C/L", command = lambda: ic_click(recipes))
tn = ttk.Button(root, text = "TN 1000 mg N/L", command = lambda: tn_click(recipes))

# Assign Button Positions
tc.grid(row = 3, column = 1, ipady = 10, ipadx = 10)
ic.grid(row = 3, column = 2, ipady = 10, ipadx = 10)
tn.grid(row = 3, column = 3, ipady = 10, ipadx = 10)

# create loop for gui
root.mainloop()
