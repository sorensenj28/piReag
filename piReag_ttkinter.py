import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk

def rins_liqu_click():
    rins_liqu_recipe = "    1 L:\n\
    Add 2 mL of concentrated Sulfuric Acid to 1 L of Deionized Water"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, rins_liqu_recipe)

def nitr_buff_click():
    nitr_buff_recipe = "    500 mL:\n\
    Fill a 500 mL volumetric flask half full with Deionized Water\n\
    Add 25 g of Ammonium Chloride]\n\
    Add 3.6 mL of Ammonium Hydroxide\n\
    Dilute to mark.\n\
    \n\
    1 L:\n\
    Fill a 1000 mL volumetric flask half full with Deionized Water\n\
    Add 50 g of Ammonium Chloride\n\
    Add 7.2 mL of Ammonium Hydroxide\n\
    Dilute to mark.\n\
    \n\
    2 L:\n\
    Fill a 2000 mL volumetric flask half full with Deionized Water\n\
    Add 100 g of Ammonium chloride\n\
    Add 14.4 of Ammonium Hydroxide\n\
    Dilute to mark."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, nitr_buff_recipe)

def nitr_colo_click():
    nitr_colo_recipe = "    500 mL:\n\
    Fill a 500 mL volumetric flask half full with Deionized Water\n\
    Add 50 mL of 32% Hydrochloric Acid\n\
    Add 0.25 g of N-(1Naphtyl)ethylenediamine dihydrochloride\n\
    Dilute to mark.\n\
    \n\
    1 L:\n\
    Fill a 1000 mL volumetric flask half full with Deionized Water\n\
    Add 100 mL of 32% Hydrochloric Acid\n\
    Add 0.5 g of N-(1Naphthyl)ethylenediamine dihydrochloride\n\
    Dilute to mark."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, nitr_colo_recipe)

def phos_ffd6_click():
    ffd6_recipe = "    500 mL:\n\
    To 500 mL of Deionized Water add 1 mL of FFD6.\n\
    \n\
    1 L:\n\
    To 1000 mL of Deionized Water add 2 mL of FFD6."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, ffd6_recipe)

def phos_sulf_click():
    sulf_recipe = "    500 mL:\n\
    Fill a 500 mL volumetric flask half full with Deionized Water\n\
    Add 20 mL of concentrated Sulfuric Acid\n\
    Dilute to mark, and pour into bottle\n\
    Add 1 mL of FFD6 to bottle\n\
    \n\
    1 L:\n\
    Fill a 500 mL volumetric flask half full with Deionized Water\n\
    Add 40 mL of concentrated Sulfuric Acid\n\
    Dilute to mark, and pour into bottle\n\
    Add 2 mL of FFD6 to bottle."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, sulf_recipe)

def phos_hept_click():
    hept_recipe = "    500 mL:\n\
    Fill a 500 mL volumetric flask half full with Deionized Water\n\
    Add 20 mL of concentrated Sulfuric Acid\n\
    Add 2.4 g of Ammonium Heptamolybdate\n\
    Dilute to mark, and pour into bottle\n\
    Add 1 mL of FFD6 to bottle.\n\
    \n\
    1 L:\n\
    Fill a 1000 mL volumetric flask half full with Deionized Water\n\
    Add 40 mL of concentrated Sulfuric Acid\n\
    Add 4.8 g of Ammonium Heptamolybdate\n\
    Dilute to mark, and pour into bottle\n\
    Add 2 mL of FFD6 to bottle."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, hept_recipe)

def lplu_stock_click():
    lplu_stock_recipe = "    Fill a 100 mL volumetric flask half way with Deionized Water\n\
    Add 300 mg of Potassium Antimony Oxide Tartate\n\
    Dilute to mark"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, lplu_stock_recipe)

def phos_lplu_click():
    lplu_recipe = "    500 mL:\n\
    Fill a 500 mL volumetric flask half full with Deionized Water\n\
    Add 9 g of L+ Ascorbic Acid\n\
    Add 10 mL  of Stock Solution\n\
    Dilute to mark.\n\
    \n\
    1 L:\n\
    Fill a 1000 mL volumetric flask half full with Deionized Water\n\
    Add 18 g of L+ Ascorbic Acid\n\
    Add 20 mL of Stock Solution\n\
    Dilute to mark."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, lplu_recipe)

def ammo_buff_click():
    ammo_buff_recipe = "    500 mL:\n\
    Fill a 500 mL volumetric flask half full with Deionized Water\n\
    Add 16.5 g of Potassium Sodium Tartate\n\
    Add 12 g of Sodium Citrate Dihydrate\n\
    Add 3 mL of 32% Hydrochloric Acid or 5 mL of 6N Hydrocloric Acid\n\
    Dilute to mark\n\
    \n\
    1 L:\n\
    Fill a 1000 mL volumetric flask half full with Deionized Water\n\
    Add 33 g of Potassium Sodium Tartate\n\
    Add 24 g of Sodium Citrate Dihydrate\n\
    Add 6 mL 32% Hydrochloric Acid or 10 mL of 6N Hydrochloric Acid\n\
    Dilute to mark\n\
    \n\
    2 L:\n\
    Fill a 2000 mL volumetric flask half full with Deionized Water\n\
    Add 66 g of Potassium Sodium Tartate\n\
    Add 48 g of Sodium Citrate Dihydrate\n\
    Add 12 mL of 32% Hydrochloric Acid or 20 mL of 6N Hydrochloric Acid\n\
    Dilute to mark"
    text.delete("1.0", "end")
    text.insert(tk.INSERT, ammo_buff_recipe)

def ammo_sali_click():
    sali_recipe = "    500 mL:\n\
    Fill a 500 mL volumetric flask half full with Deionized Water\n\
    Add 12.5 g of Sodium Hydroxide\n\
    Add 40 g Sodium Salicylite\n\
    Dilute to mark.\n\
    \n\
    1 L:\n\
    Fill a 1000 mL volumetric flask half full with Deionized Water\n\
    Add 25 g of Sodium Hydroxide\n\
    Add 80 g of Sodium Salicyalite\n\
    Dilute to mark."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, sali_recipe)

def ammo_nitr_click():
    nitr_recipe = "    500 mL:\n\
    Fill a 500 mL volumetric flask half full with Deionized Water\n\
    Add 0.5 g of Sodium Nitroprusside\n\
    Dilute to mark.\n\
    \n\
    1 L:\n\
    Fill a 1000 mL volumetric flask half full with Deionized Water\n\
    Add 1.0 g of Sodium Nitroprusside\n\
    Dilute to mark."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, nitr_recipe)

def ammo_dich_click():
    dich_recipe = "    500 mL:\n\
    Fill a 500 mL volumteric Flask half full with Deionized Water\n\
    Add 1.0 g of Sodium Dichlorocyanurite\n\
    Dilute to mark.\n\
    \n\
    1 L:\n\
    Fill a 1000 mL volumetric flask half full with Deionized Water\n\
    Add 2.0 g of Sodium Dichlorocyanurite\n\
    Dilute to mark."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, dich_recipe)

def std1_click():
    std1_recipe = "    250 uL of 100 ppm Nitrate/nitrite Stock Standard\n\
    25 uL of 1000 ppm Phosphate Stock Standard\n\
    25 uL of 1000 ppm Ammonia Stock Standard\n\
    Dilute to 100 mL for final 0.25 ppm."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std1_recipe)

def std2_click():
    std2_recipe = "    750 uL of 100 ppm Nitrate/nitrite Stock Standard\n\
    75 uL of 1000 ppm Phosphate Stock Standard\n\
    75 uL of 1000 ppm Ammonia Stock Standard\n\
    Dilute to 100 mL for final 0.75 ppm."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std2_recipe)

def std3_click():
    std3_recipe = "    1000 uL of 100 ppm Nitrate/nitrite Stock Standard\n\
    100 uL of 1000 ppm Phosphate Stock Standard\n\
    100 uL of 1000 ppm Ammonia Stock Standard\n\
    Dilute to 100 mL for final 1.0 ppm."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std3_recipe)

def std4_click():
    std4_recipe = "    2000 uL of 100 ppm Nitrate/nitrite Stock Standard\n\
    200 uL of 1000 ppm Phosphate Stock Standard\n\
    200 uL of 1000 ppm Ammonia Stock Standard\n\
    Dilute to 100 mL for final 2.0 ppm."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std4_recipe)

def std5_click():
    std5_recipe = "    4000 uL of 100 ppm Nitrate/nitrite Stock Standard\n\
    400 uL of 1000 ppm Phosphate Stock Standard\n\
    400 uL of 1000 ppm Ammonia Stock Standard\n\
    Dilute to 100 mL for final 4.0 ppm."
    text.delete("1.0", "end")
    text.insert(tk.INSERT, std5_recipe)

# Initialize tkinter
root = tk.Tk()
root.title("Reagents & Standards Cookbooks By John")

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
rins_liqu = ttk.Button(root, text = "Rinsing Liquid", command = rins_liqu_click)
nitr_buff = ttk.Button(root, text = "Nitrate/Nitrite Buffer", command = nitr_buff_click)
nitr_colo = ttk.Button(root, text = "Nitrate/Nitrite Color Reagent", command = nitr_colo_click)
phos_ffd6 = ttk.Button(root, text = "FFD6",command = phos_ffd6_click)
phos_sulf = ttk.Button(root, text = "Sulfuric Acid", command = phos_sulf_click)
phos_hept = ttk.Button(root, text = "Ammonium Heptamolybdate", command = phos_hept_click)
phos_lpst = ttk.Button(root, text = "Potassium Antimony Stock", command = lplu_stock_click)
phos_lplu = ttk.Button(root, text = "L+ Ascorbic Acid", command = phos_lplu_click)
ammo_buff = ttk.Button(root, text = "Ammonia: Buffer", command = ammo_buff_click)
ammo_sali = ttk.Button(root, text = "Sodium Salicyalite", command = ammo_sali_click)
ammo_nitr = ttk.Button(root, text = "Sodium Nitroprusside", command = ammo_nitr_click)
ammo_dich = ttk.Button(root, text = "Sodium Dichlorocyanurite", command = ammo_dich_click)

# Create Blanks to make columns equal for San++
blank1 = ttk.Label(root, text = "").grid(row = 2, column = 0)
blank2 = ttk.Label(root, text = "").grid(row = 2, column = 1)
blank3 = ttk.Label(root, text = "").grid(row = 4, column = 0)
blank4 = ttk.Label(root, text = "").grid(row = 4, column = 3)

# Assign San ++ Grid Positions
rins_liqu.grid(row = 2, column = 2)
nitr_buff.grid(row = 4, column = 1)
nitr_colo.grid(row = 4, column = 2)
phos_ffd6.grid(row = 6, column = 0)
phos_sulf.grid(row = 6, column = 1)
phos_hept.grid(row = 6, column = 2)
phos_lpst.grid(row = 6, column = 3)
phos_lplu.grid(row = 6, column = 4)
ammo_buff.grid(row = 8, column = 0)
ammo_sali.grid(row = 8, column = 1)
ammo_nitr.grid(row = 8, column = 2)
ammo_dich.grid(row = 8, column = 3)

# Create Labels for Skalar San ++ Standards
standard_label = ttk.Label(root, text = "Skalar San ++ CFA Standards")

# Assign Standard Labels to Grid Positions
standard_label.grid(row = 9, column = 0, columnspan = 4)

# Create Buttons for San++ Standards
std1 = ttk.Button(root, text = "Standard 1: 0.25 (ppm)", command = std1_click)
std2 = ttk.Button(root, text = "Standard 2: 0.25 (ppm)", command = std2_click)
std3 = ttk.Button(root, text = "Standard 3: 1.0 (ppm)", command = std3_click)
std4 = ttk.Button(root, text = "Standard 4: 2.0 (ppm)", command = std4_click)
std5 = ttk.Button(root, text = "Standard 5: 4.0 (ppm)", command = std5_click)

# Assign Button to Grid Positions
std1.grid(row = 10, column = 0)
std2.grid(row = 10, column = 1)
std3.grid(row = 10, column = 2)
std4.grid(row = 10, column = 3)
std5.grid(row = 10, column = 4)

# create loop for gui
root.mainloop()
