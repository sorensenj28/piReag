import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk

def get_recipe_lines():
    with open("piReagText.txt", mode = "r") as file:
        recipe_lines = file.readlines()
        return recipe_lines

def rins_liqu_click(recipe_lines):
    rins_liqu_recipe = recipe_lines[0:2]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, rins_liqu_recipe)

def nitr_buff_click(recipe_lines):
    nitr_buff_recipe = recipe_lines[3:20]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, nitr_buff_recipe)

def nitr_colo_click(recipe_lines):
    nitr_colo_recipe = recipe_lines[21:32]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, nitr_colo_recipe)

def phos_ffd6_click(recipe_lines):
    ffd6_recipe = recipe_lines[33:38]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, ffd6_recipe)

def phos_sulf_click(recipe_lines):
    sulf_recipe = recipe_lines[39:50]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, sulf_recipe)

def phos_hept_click(recipe_lines):
    hept_recipe = recipe_lines[51:64]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, hept_recipe)

def lplu_stock_click(recipe_lines):
    lplu_stock_recipe = recipe_lines[65:68]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, lplu_stock_recipe)

def phos_lplu_click(recipe_lines):
    lplu_recipe = recipe_lines[69:80]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, lplu_recipe)

def ammo_buff_click(recipe_lines):
    ammo_buff_recipe = recipe_lines[81:101]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, ammo_buff_recipe)

def ammo_sali_click(recipe_lines):
    sali_recipe = recipe_lines[102:113]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, sali_recipe)

def ammo_nitr_click(recipe_lines):
    nitr_recipe = recipe_lines[114:123]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, nitr_recipe)

def ammo_dich_click(recipe_lines):
    dich_recipe = recipe_lines[124:133]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, dich_recipe)

def std1_click(recipe_lines):
    std1_recipe = recipe_lines[134:138]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std1_recipe)

def std2_click(recipe_lines):
    std2_recipe = recipe_lines[139:143]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std2_recipe)

def std3_click(recipe_lines):
    std3_recipe = recipe_lines[144:148]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std3_recipe)

def std4_click(recipe_lines):
    std4_recipe = recipe_lines[149:153]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std4_recipe)

def std5_click(recipe_lines):
    std5_recipe = recipe_lines[154:158]
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std5_recipe)

# Initialize tkinter
root = tk.Tk()
root.title("Reagents & Standards Cookbooks By John")
root.geometry("1024x600")
root.resizable(width = False, height = False)
recipes = get_recipe_lines()

# Style

# Add Scrollable Text Box
text = st.ScrolledText(root, width = 65, height = 6, font = ("arial", 10))
text.grid(row = 0, column = 0, columnspan = 5, padx = 10, pady =10)

# Skalar San++ Labels
cfa_label = ttk.Label(root, text = "Skalar San ++ CFA Reagents")
nitr_label = ttk.Label(root, text = "Nitrate/Nitrite Channel")
phos_label = ttk.Label(root, text = "Phosphate Channel")
ammo_label = ttk.Label(root, text = "Ammonium Channel")
cfa_label.grid(row = 1, column = 0, columnspan = 4)
nitr_label.grid(row = 3, column = 0, columnspan =4)
phos_label.grid(row = 5, column = 0, columnspan = 4)
ammo_label.grid(row = 7, column = 0, columnspan = 4)

# Create Buttons for San++ Reagents
rins_liqu = ttk.Button(root, text = "Rinsing Liquid", command = lambda: rins_liqu_click(recipes))
nitr_buff = ttk.Button(root, text = "Nitrate/Nitrite Buffer", command = lambda: nitr_buff_click(recipes))
nitr_colo = ttk.Button(root, text = "Nitrate/Nitrite Color Reagent", command = lambda: nitr_colo_click(recipes))
phos_ffd6 = ttk.Button(root, text = "FFD6",command = lambda: phos_ffd6_click(recipes))
phos_sulf = ttk.Button(root, text = "Sulfuric Acid", command = lambda: phos_sulf_click(recipes))
phos_hept = ttk.Button(root, text = "Ammonium Heptamolybdate", command = lambda: phos_hept_click(recipes))
phos_lpst = ttk.Button(root, text = "Potassium Antimony Stock", command = lambda: lplu_stock_click(recipes))
phos_lplu = ttk.Button(root, text = "L+ Ascorbic Acid", command = lambda: phos_lplu_click(recipes))
ammo_buff = ttk.Button(root, text = "Ammonia: Buffer", command = lambda: ammo_buff_click(recipes))
ammo_sali = ttk.Button(root, text = "Sodium Salicyalite", command = lambda: ammo_sali_click(recipes))
ammo_nitr = ttk.Button(root, text = "Sodium Nitroprusside", command = lambda: ammo_nitr_click(recipes))
ammo_dich = ttk.Button(root, text = "Sodium Dichlorocyanurite", command = lambda: ammo_dich_click(recipes))

# Create Blanks to make columns equal for San++
blank1 = ttk.Label(root, text = "").grid(row = 2, column = 0)
blank2 = ttk.Label(root, text = "").grid(row = 2, column = 1)
blank3 = ttk.Label(root, text = "").grid(row = 4, column = 0)
blank4 = ttk.Label(root, text = "").grid(row = 4, column = 3)

# Assign San ++ Grid Positions
rins_liqu.grid(row = 2, column = 2, ipady = 10, ipadx = 10)
nitr_buff.grid(row = 4, column = 1, ipady = 10, ipadx = 10)
nitr_colo.grid(row = 4, column = 2, ipady = 10, ipadx = 10)
phos_ffd6.grid(row = 6, column = 0, ipady = 10, ipadx = 10)
phos_sulf.grid(row = 6, column = 1, ipady = 10, ipadx = 10)
phos_hept.grid(row = 6, column = 2, ipady = 10, ipadx = 10)
phos_lpst.grid(row = 6, column = 3, ipady = 10, ipadx = 10)
phos_lplu.grid(row = 6, column = 4, ipady = 10, ipadx = 10)
ammo_buff.grid(row = 8, column = 0, ipady = 10, ipadx = 10)
ammo_sali.grid(row = 8, column = 1, ipady = 10, ipadx = 10)
ammo_nitr.grid(row = 8, column = 2, ipady = 10, ipadx = 10)
ammo_dich.grid(row = 8, column = 3, ipady = 10, ipadx = 10)

# Create Labels for Skalar San ++ Standards
standard_label = ttk.Label(root, text = "Skalar San ++ CFA Standards")

# Assign Standard Labels to Grid Positions
standard_label.grid(row = 9, column = 0, columnspan = 4)

# Create Buttons for San++ Standards
std1 = ttk.Button(root, text = "Standard 1: 0.25 (ppm)", command = lambda: std1_click(recipes))
std2 = ttk.Button(root, text = "Standard 2: 0.25 (ppm)", command = lambda: std2_click(recipes))
std3 = ttk.Button(root, text = "Standard 3: 1.0 (ppm)", command = lambda: std3_click(recipes))
std4 = ttk.Button(root, text = "Standard 4: 2.0 (ppm)", command = lambda: std4_click(recipes))
std5 = ttk.Button(root, text = "Standard 5: 4.0 (ppm)", command = lambda: std5_click(recipes))

# Assign Button to Grid Positions
std1.grid(row = 10, column = 0, ipady = 10, ipadx = 10)
std2.grid(row = 10, column = 1, ipady = 10, ipadx = 10)
std3.grid(row = 10, column = 2, ipady = 10, ipadx = 10)
std4.grid(row = 10, column = 3, ipady = 10, ipadx = 10)
std5.grid(row = 10, column = 4, ipady = 10, ipadx = 10)

# create loop for gui
root.mainloop()
