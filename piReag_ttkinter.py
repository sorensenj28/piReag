import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk

def nitr_buff_click():
    nitr_buff_recipe = "    Ammonium Chloride: 50 g\n\
    Ammonium Hydroxide: 7.2 mL\n\
    per L"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, nitr_buff_recipe)

def nitr_colo_click():
    nitr_colo_recipe = "    Hydrochloric Acid 32%: 100 mL\n\
    N-(1Naphthyl)ethylenediamine dihydrochloride: 0.5 g\n\
    per L"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, nitr_colo_recipe)

def phos_ffd6_click():
    ffd6_recipe = "    2 mL FFD6 per L"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, ffd6_recipe)

def phos_sulf_click():
    sulf_recipe = "    40 mL Sulfuric Acid\n\
    2 mL FFD5\n\
    per L"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, sulf_recipe)

def phos_hept_click():
    hept_recipe = "    40 mL Sulfuric Acid\n\
    4.8 g Ammonium Heptamolybdate\n\
    2 mL FFD6\n\
    per L"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, hept_recipe)

def phos_lplu_click():
    lplu_recipe = "    18 g L+ Ascorbic Acid\n\
    20 mL Stock Sol'n\n\
    per L"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, lplu_recipe)

def ammo_buff_click():
    ammo_buff_recipe = "    44 g Potassium Sodium Tartate\n\
    24 g Sodium Citrate Dihydrate\n\
    6 mL 32% hydrochloric acid or 10 mL 6N hydrochloric acid\n\
    per L"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, ammo_buff_recipe)

def ammo_sali_click():
    sali_recipe = "    25 g Sodium Hydroxide\n\
    80 g Sodium Salicyalite\n\
    per L"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, sali_recipe)

def ammo_nitr_click():
    nitr_recipe = "    1.0 g Sodium Nitroprusside\n\
    per L"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, nitr_recipe)

def ammo_dich_click():
    dich_recipe = "    2.0 g Sodium Dichlorocyanurite\n\
    per L"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, dich_recipe)

def std1_click():
    std1_recipe = "    250 uL of 100 ppm Nitrate/nitrite Stock Standard\n\
    25 uL of 1000 ppm Phosphate Stock Standard\n\
    25 uL of 1000 ppm Ammonia Stock Standard"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std1_recipe)

def std2_click():
    std2_recipe = "    750 uL of 100 ppm Nitrate/nitrite Stock Standard\n\
    75 uL of 1000 ppm Phosphate Stock Standard\n\
    75 uL of 1000 ppm Ammonia Stock Standard"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std2_recipe)

def std3_click():
    std3_recipe = "    1000 uL of 100 ppm Nitrate/nitrite Stock Standard\n\
    100 uL of 1000 ppm Phosphate Stock Standard\n\
    100 uL of 1000 ppm Ammonia Stock Standard"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std3_recipe)

def std4_click():
    std4_recipe = "    2000 uL of 100 ppm Nitrate/nitrite Stock Standard\n\
    200 uL of 1000 ppm Phosphate Stock Standard\n\
    200 uL of 1000 ppm Ammonia Stock Standard"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std4_recipe)

def std5_click():
    std5_recipe = "    4000 uL of 100 ppm Nitrate/nitrite Stock Standard\n\
    400 uL of 1000 ppm Phosphate Stock Standard\n\
    400 uL of 1000 ppm Ammonia Stock Standard"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std5_recipe)

# Initialize tkinter
root = tk.Tk()
root.title("Reagents & Standards Cookbooks\n By John")
text = st.ScrolledText(root, width = 65, height = 5, font = ("arial", 10))
text.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady =10)

# Skalar San++ Labels
cfa_label = ttk.Label(root, text = "Skalar San ++ CFA Reagents")
nitr_label = ttk.Label(root, text = "Nitrate/Nitrite Channel")
phos_label = ttk.Label(root, text = "Phosphate Channel")
ammo_label = ttk.Label(root, text = "Ammonium Channel")
cfa_label.grid(row = 1, column = 0, columnspan = 4)
nitr_label.grid(row = 2, column = 0, columnspan =4)
phos_label.grid(row = 4, column = 0, columnspan = 4)
ammo_label.grid(row = 6, column = 0, columnspan = 4)

# Create Buttons for San++ Reagents
nitr_buff = ttk.Button(root, text = "Nitrate/Nitrite Buffer", command = nitr_buff_click)
nitr_colo = ttk.Button(root, text = "Nitrate/Nitrite Color Reagent", command = nitr_colo_click)
phos_ffd6 = ttk.Button(root, text = "FFD6",command = phos_ffd6_click)
phos_sulf = ttk.Button(root, text = "Sulfuric Acid", command = phos_sulf_click)
phos_hept = ttk.Button(root, text = "Ammonium Heptamolybdate", command = phos_hept_click)
phos_lplu = ttk.Button(root, text = "L+ Ascorbic Acid", command = phos_lplu_click)
ammo_buff = ttk.Button(root, text = "Ammonia: Buffer", command = ammo_buff_click)
ammo_sali = ttk.Button(root, text = "Sodium Salicyalite", command = ammo_sali_click)
ammo_nitr = ttk.Button(root, text = "Sodium Nitroprusside", command = ammo_nitr_click)
ammo_dich = ttk.Button(root, text = "Sodium Dichlorocyanurite", command = ammo_dich_click)

# Create Blanks to make columns equal for San++
blank1 = ttk.Label(root, text = "").grid(row = 3, column = 0)
blank2 = ttk.Label(root, text = "").grid(row = 3, column = 3)

# Assign San ++ Grid Positions
nitr_buff.grid(row = 3, column = 1)
nitr_colo.grid(row = 3, column = 2)
phos_ffd6.grid(row = 5, column = 0)
phos_sulf.grid(row = 5, column = 1)
phos_hept.grid(row = 5, column = 2)
phos_lplu.grid(row = 5, column = 3)
ammo_buff.grid(row = 7, column = 0)
ammo_sali.grid(row = 7, column = 1)
ammo_nitr.grid(row = 7, column = 2)
ammo_dich.grid(row = 7, column = 3)

# Create Labels for Skalar San ++ Standards
standard_label = ttk.Label(root, text = "Skalar San ++ CFA Standards")

# Assign Standard Labels to Grid Positions
standard_label.grid(row = 8, column = 0, columnspan = 4)

# Create Buttons for San++ Standards
std1 = ttk.Button(root, text = "Standard 1: 0.25 (ppm)", command = std1_click)
std2 = ttk.Button(root, text = "Standard 2: 0.25 (ppm)", command = std2_click)
std3 = ttk.Button(root, text = "Standard 3: 1.0 (ppm)", command = std3_click)
std4 = ttk.Button(root, text = "Standard 4: 2.0 (ppm)", command = std4_click)
std5 = ttk.Button(root, text = "Standard 5: 4.0 (ppm)", command = std5_click)

# Assign Button to Grid Positions
std1.grid(row = 9, column = 0)
std2.grid(row = 9, column = 1)
std3.grid(row = 9, column = 2)
std4.grid(row = 9, column = 3)
std5.grid(row = 9, column = 4)

# create loop for gui
root.mainloop()
