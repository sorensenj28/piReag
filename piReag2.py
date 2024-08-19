#!/usr/bin/env python3
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk
from tkinter.ttk import *

class window:

    def clear_frame(frame):
        frame.destroy()

    def home_frame():
        home = tk.Frame(root)
        home.pack()
        for i in range(6):
            label = tk.Label(home,
                             text = "").grid(row = i)
        channel = tk.Label(home,
                              text = "Select Channel",
                              font = ("Arial", 20)).grid(row = 6, columnspan = 3, padx = 20, pady = 20)
        nitr_button = tk.Button(home,
                                text = "Nitrate/Nitrite Channel",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home),
                                                   window.nitrate_frame()]).grid(row = 7, column = 0, padx = 20, pady = 20)
        phos_button = tk.Button(home,
                                text = "Phosphate Channel",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home),
                                                   window.phosphate_frame()]).grid(row = 7, column = 1, padx = 20, pady = 20)
        ammo_button = tk.Button(home,
                                text = "Ammonium Channel",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home),
                                                   window.ammonium_frame()]).grid(row = 7, column = 2, padx = 20, pady = 20)
        rins_button = tk.Button(home,
                                text = "Rinsing Liquid",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home),
                                                   window.volume_frame("rinsing")]).grid(row = 8, column = 0, padx = 20, pady = 20)
        stds_button = tk.Button(home,
                                text = "Calibration Standards",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home),
                                                   window.standards_frame()]).grid(row = 8, column = 2, padx = 20, pady = 20)

    def nitrate_frame():
        nitr_frame = tk.Frame(root)
        nitr_frame.pack()
        for i in range(6):
            label = tk.Label(nitr_frame,
                             text = "").grid(row = i)

        nitr_buffer = tk.Button(nitr_frame,
                                text = "Nitrate/Nitrite Buffer",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(nitr_frame),
                                                   window.buffer_volume_frame("nitrate_buffer")]).grid(row = 6, column = 1, padx = 20, pady = 20)
        color_reag = tk.Button(nitr_frame,
                               text = "Color Reagent",
                               font = ("Arial", 18),
                               command = lambda: [window.clear_frame(nitr_frame),
                                                   window.volume_frame("color_reagent")]).grid(row = 6, column = 2, padx = 20, pady = 20)
        home_button = tk.Button(nitr_frame,
                                text = "Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(nitr_frame),
                                                   window.home_frame()]).grid(row = 7, column =0, padx = 20, pady = 20)

    def phosphate_frame():
        phos_frame = tk.Frame(root)
        phos_frame.pack()
        for i in range(6):
            label = tk.Label(phos_frame,
                             text = "").grid(row = i)
        ffd6_button = tk.Button(phos_frame,
                                text = "FFD6 Solution",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(phos_frame),
                                                   window.volume_frame("ffd6")]).grid(row = 6, column = 1, padx = 20, pady = 20)
        sulf_button = tk.Button(phos_frame,
                                text = "Sulfuric Acid Solution",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(phos_frame),
                                                   window.volume_frame("sulfuric_acid")]).grid(row = 6, column = 2, padx = 20, pady = 20)
        hept_button = tk.Button(phos_frame,
                                text = "Ammonium Heptamolybdate",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(phos_frame),
                                                   window.volume_frame("ammonium_heptamolybdate")]).grid(row = 7, column = 1, padx = 20, pady = 20)
        lplus_button = tk.Button(phos_frame,
                                 text = "L+ Ascorbic Acid",
                                 font = ("Arial", 18),
                                 command = lambda: [window.clear_frame(phos_frame),
                                                   window.volume_frame("l_plus_ascorbic")]).grid(row = 7, column = 2, padx = 20, pady = 20)
        home_button = tk.Button(phos_frame,
                                text = "Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(phos_frame),
                                                   window.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)

    def ammonium_frame():
        ammo_frame = tk.Frame(root)
        ammo_frame.pack()
        for i in range(6):
            label = tk.Label(ammo_frame,
                             text = "").grid(row = i)
        ammo_buffer = tk.Button(ammo_frame,
                                text = "Ammonium Buffer",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(ammo_frame),
                                                   window.buffer_volume_frame("ammonium_buffer")]).grid(row = 6, column = 1, padx = 20, pady = 20)
        sali_button = tk.Button(ammo_frame,
                                  text = "Sodium Salicyalite Solution",
                                  font = ("Arial", 18),
                                  command = lambda: [window.clear_frame(ammo_frame),
                                                   window.volume_frame("salicyalite")]).grid(row = 6, column = 2, padx = 20, pady = 20)
        nitro_button = tk.Button(ammo_frame,
                                 text = "Nitroprusside Solution",
                                 font = ("Arial", 18),
                                 command = lambda: [window.clear_frame(ammo_frame),
                                                   window.volume_frame("nitroprusside")]).grid(row = 7, column = 1, padx = 20, pady = 20)
        dichlo_button = tk.Button(ammo_frame,
                                  text = "Dichlorocyanurite Solution",
                                  font = ("Arial", 18),
                                  command = lambda: [window.clear_frame(ammo_frame),
                                                   window.volume_frame("dichlorocyanurite")]).grid(row = 7, column = 2, padx = 20, pady = 20)
        home_button = tk.Button(ammo_frame,
                                text = "Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(ammo_frame),
                                                   window.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)
    def standards_frame():
        std_frame = tk.Frame(root)
        std_frame.pack()
        for i in range(6):
            label = tk.Label(std_frame,
                             text = "").grid(row = 1)
        std1 = tk.Button(std_frame,
                         font = ("Arial", 18),
                         text = "Standard 1",
                         command = lambda: [window.clear_frame(std_frame),
                         window.instruct_frame(recipe.get_recipe("std1", 100))]).grid(row = 6, column = 0, padx = 20, pady = 40)
        std2 = tk.Button(std_frame,
                         text = "Standard 2",
                         font = ("Arial", 18),
                         command = lambda: [window.clear_frame(std_frame),
                         window.instruct_frame(recipe.get_recipe("std2", 100))]).grid(row = 6, column = 1, padx = 20, pady = 40)
        std3 = tk.Button(std_frame,
                         text = "Standard 3",
                         font = ("Arial", 18),
                         command = lambda: [window.clear_frame(std_frame),
                         window.instruct_frame(recipe.get_recipe("std3", 100))]).grid(row = 6, column = 2, padx = 20, pady = 40)
        std4 = tk.Button(std_frame,
                         text = "Standard 4",
                         font = ("Arial", 18),
                         command = lambda: [window.clear_frame(std_frame),
                         window.instruct_frame(recipe.get_recipe("std4", 100))]).grid(row = 7, column = 1, padx = 20, pady = 40)
        std5 = tk.Button(std_frame,
                         text = "Standard 5",
                         font = ("Arial", 18),
                         command = lambda: [window.clear_frame(std_frame),
                         window.instruct_frame(recipe.get_recipe("std5", 100))]).grid(row = 7, column = 2, padx = 20, pady = 40)

        home_button = tk.Button(std_frame,
                                text = "Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(std_frame),
                                                   window.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)

    def buffer_volume_frame(reagent):
        reagent = reagent
        vol_frame = tk.Frame(root)
        vol_frame.pack()
        for i in range(6):
            label = tk.Label(vol_frame,
                             text = "").grid(row = i)
        vol_1 = tk.Button(vol_frame,
                          text = "500 mL",
                          font = ("Arial", 18),
                          command = lambda: [window.clear_frame(vol_frame),
                                             window.instruct_frame(recipe.get_recipe(reagent, 500))]).grid(row = 6, column = 1, padx = 20, pady = 40)
        vol_2 = tk.Button(vol_frame,
                          text = "1,000 mL",
                          font = ("Arial", 18),
                          command = lambda: [window.clear_frame(vol_frame),
                                             window.instruct_frame(recipe.get_recipe(reagent, 1000))]).grid( row = 6, column = 2, padx = 20, pady = 40)
        vol_3 = tk.Button(vol_frame,
                          text = "2,000 mL",
                          font = ("Arial", 18),
                          command = lambda: [window.clear_frame(vol_frame),
                                             window.instruct_frame(recipe.get_recipe(reagent, 2000))]).grid(row = 7, column = 1, padx = 20, pady = 40)

        home_button = tk.Button(vol_frame,
                                text = "Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(vol_frame),
                                                   window.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)

    def volume_frame(reagent):
        reagent = reagent
        vol_frame = tk.Frame(root)
        vol_frame.pack()
        for i in range(6):
            label = tk.Label(vol_frame,
                             text = "").grid(row = i)
        vol_1 = tk.Button(vol_frame,
                          text = "500 mL",
                          font = ("Arial", 18),
                          command = lambda: [window.clear_frame(vol_frame),
                                             window.instruct_frame(recipe.get_recipe(reagent, 500))]).grid(row = 6, column = 1, padx = 20, pady = 40)
        vol_2 = tk.Button(vol_frame,
                          text = "1,000 mL",
                          font = ("Arial", 18),
                          command = lambda: [window.clear_frame(vol_frame),
                                             window.instruct_frame(recipe.get_recipe(reagent, 1000))]).grid( row = 6, column = 2, padx = 20, pady = 40)

        home_button = tk.Button(vol_frame,
                                text = "Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(vol_frame),
                                                   window.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)

    def instruct_frame(recipe):
        inst_frame = tk.Frame(root)
        inst_frame.pack()
        for i in range(4):
            label = tk.Label(inst_frame,
                             text = "").grid(row = i)
        text = tk.Text(inst_frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 18))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(inst_frame,
                                text = "Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(inst_frame),
                                                   window.home_frame()]).grid(row = 5, column = 0, padx = 20, pady = 20)

class recipe:

    def get_recipe(reagent, volume):
        with open("piReagText2.txt", mode = "r") as file:
            recipes = file.readlines()
        if reagent == "nitrate_buffer" and volume == 500:
            recipe = recipes[5:9]
            return recipe
        if reagent == "nitrate_buffer" and volume == 1000:
            recipe = recipes[11:15]
            return recipe
        if reagent == "nitrate_buffer" and volume == 2000:
            recipe = recipes[17:21]
            return recipe
        if reagent == "color_reagent" and volume == 500:
            recipe = recipes[23:28]
            return recipe
        if reagent == "color_reagent" and volume == 1000:
            recipe = recipes[30:35]
            return recipe
        if reagent == "ffd6" and volume == 500:
            recipe = "To 500 mL of Deionized Water add 1 mL of FFD6."
            return recipe
        if reagent == "ffd6" and volume == 1000:
            recipe = "To 1000 mL of Deionized Water add 2 mL of FFD6."
            return recipe
        if reagent == "sulfuric_acid" and volume == 500:
            recipe = recipes[43:47]
            return recipe
        if reagent == "sulfuric_acid" and volume == 1000:
            recipe = recipes[49:53]
            return recipe
        if reagent == "ammonium_heptamolybdate" and volume == 500:
            recipe = recipes[55:60]
            return recipe
        if reagent == "ammonium_heptamolybdate" and volume == 1000:
            recipe = recipes[62:67]
            return recipe
        if reagent == "l_plus_ascorbic" and volume == 500:
            recipe = recipes[74:78]
            return recipe
        if reagent == "l_plus_ascorbic" and volume == 1000:
            recipe = recipes[80:84]
            return recipe
        if reagent == "ammonium_buffer" and volume == 500:
            recipe = recipes[86:91]
            return recipe
        if reagent == "ammonium_buffer" and volume == 1000:
            recipe = recipes[93:98]
            return recipe
        if reagent == "ammonium_buffer" and volume == 2000:
            recipe = recipes[100:105]
            return recipe
        if reagent == "salicyalite" and volume == 500:
            recipe = recipes[107:111]
            return recipe
        if reagent == "salicyalite" and volume == 1000:
            recipe = recipes[113:117]
            return recipe
        if reagent == "nitroprusside" and volume == 500:
            recipe = recipes[119:122]
            return recipe
        if reagent == "nitroprusside" and volume == 1000:
            recipe = recipes[124:127]
            return recipe
        if reagent == "dichlorocyanurite" and volume == 500:
            recipe = recipes[129:132]
            return recipe
        if reagent == "dichlorocyanurite" and volume == 1000:
            recipe = recipes[134:137]
            return recipe
        if reagent == "rinsing" and volume == 500:
            recipe = "Add 1 mL of Sulfuric Acid to 500 mL DI Water."
            return recipe
        if reagent == "rinsing" and volume == 1000:
            recipe = "Add 2 mL of Sulfuric Acid to 1 L of DI Water."
            return recipe
        if reagent == "rinsing" and volume == 2000:
            recipe = "Add 4 mL of Sulfuric Acid to 2 L of DI Water."
            return recipe
        if reagent == "std1":
            recipe = recipes[138:143]
            return recipe
        if reagent == "std2":
            recipe = recipes[144:149]
            return recipe
        if reagent == "std3":
            recipe = recipes[150:155]
            return recipe
        if reagent == "std4":
            recipe = recipes[156:161]
            return recipe
        if reagent == "std5":
            recipe = recipes[162:167]
            return recipe

#  Create root GUI
root = tk.Tk()
root.title("San ++ CFA Cookbook By John")
root.geometry("1024x600")
root.resizable(width = False, height = False)
window.home_frame()


# Loop root window
root.mainloop()
