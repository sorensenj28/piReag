#!/usr/bin/env python3
import tkinter as tk
import tkinter.scrolledtext as st
from tkinter import ttk
from tkinter.ttk import *

class window():
    def clear_frame(frame):
        frame.destroy()

class main_window():
    def piLab_home():
        home = tk.Frame(root)
        home.pack()
        for i in range(6):
                label = tk.Label(home,
                                text = "").grid(row = i)
        extracts = tk.Button(home,
                             text = "Extractant Recipes",
                             font = ("Arial", 20),
                             command = lambda: [window.clear_frame(home),
                                                procedure_selection.extracts_click()]).grid(row = 7, column = 1, padx = 20, pady = 20)

        instruments = tk.Button(home,
                                text = "Instrumentation",
                                font = ("Arial", 20),
                                command = lambda: [window.clear_frame(home),
                                                   procedure_selection.instruments_click()]).grid(row = 7, column = 3, padx = 20, pady = 20)
        protocols = tk.Button(home,
                              text = "Protocols",
                              font = ("Arial", 20),
                              ).grid(row = 8, column = 2, padx = 20, pady = 20)
class procedure_selection():
    def extracts_click():
        extract_frame = tk.Frame(root)
        extract_frame.pack()
        for i in range(6):
                label = tk.Label(extract_frame,
                                text = "").grid(row = i)
        m3 = tk.Button(extract_frame,
                       text = "Mehlich 3",
                       font = ("Arial", 20),
                       command = lambda: [window.clear_frame(extract_frame),
                                          procedure_selection.m3_click()]).grid(row = 7, column = 0, padx = 20, pady = 20)
        h3a = tk.Button(extract_frame,
                        text = "H3A: Haney 3 Acids",
                        font = ("Arial", 20),
                        command = lambda: [window.clear_frame(extract_frame),
                                           procedure_selection.h3a_click()]).grid(row = 7, column = 2, padx = 20, pady = 20)
        olsen = tk.Button(extract_frame,
                          text = "Olsen P",
                          font = ("Arial", 20),
                          command = lambda: [window.clear_frame(extract_frame),
                                             procedure_selection.olsen_click()]).grid(row = 8, column = 0, padx = 20, pady = 20)
        kcl = tk.Button(extract_frame,
                        text = "KCl: Potassium Chloride",
                        font = ("Arial", 20),
                        command = lambda: [window.clear_frame(extract_frame),
                                           procedure_selection.kcl_click()]).grid(row = 8, column = 2, padx = 20, pady = 20)
        piLab_home = tk.Button(extract_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [window.clear_frame(extract_frame),
                                            main_window.piLab_home()]).grid(row = 9, column = 0, padx = 20, pady = 20)

    def instruments_click():
        instrument_frame = tk.Frame(root)
        instrument_frame.pack()
        for i in range(6):
            label = tk.Label(instrument_frame,
                             text = "").grid(row = i)
        icp = tk.Button(instrument_frame,
                        text = "ICP-OES",
                        font = ("Arial", 25),
                        command = lambda: [window.clear_frame(instrument_frame),
                                           icp_cookbook.icp_home_frame()]).grid(row = 7, column = 0, padx = 20, pady = 20)
        cfa = tk.Button(instrument_frame,
                        text = "Skalar San ++",
                        font = ("Arial", 25),
                        command = lambda: [window.clear_frame(instrument_frame),
                                           skalar_cookbook.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)
        piLab_home = tk.Button(instrument_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [window.clear_frame(instrument_frame),
                                            main_window.piLab_home()]).grid(row = 9, column = 0, padx = 20, pady = 20)
    def m3_click():
        m3_frame = tk.Frame(root)
        m3_frame.pack()
        for i in range(6):
            label = tk.Label(m3_frame,
                             text = "").grid(row = i)
        stock = tk.Button(m3_frame,
                          text = "M3 Stock Solution",
                          font = ("Arial", 20),
                          command = lambda: [window.clear_frame(m3_frame),
                                             protocols.m3_stock_click(protocols.open_protocols())]).grid(row = 7, column = 1, padx = 20, pady = 20)
        m3_1L = tk.Button(m3_frame,
                          text = "M3 Solution 1 L",
                          font = ("Arial", 20),
                          command = lambda: [window.clear_frame(m3_frame),
                                             protocols.m3_1L_click(protocols.open_protocols())]).grid(row = 7, column = 3, padx = 20, pady = 20)
        m3_2L = tk.Button(m3_frame,
                          text = "M3 Solution 2 L",
                          font = ("Arial", 20),
                          command = lambda: [window.clear_frame(m3_frame),
                                             protocols.m3_2L_click(protocols.open_protocols())]).grid(row = 8, column =2, padx = 20, pady = 20)
        piLab_home = tk.Button(m3_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [window.clear_frame(m3_frame),
                                            main_window.piLab_home()]).grid(row = 9, column = 0, padx = 20, pady = 20)

    def h3a_click():
        h3a_frame = tk.Frame(root)
        h3a_frame.pack()
        for i in range(6):
            label = tk.Label(h3a_frame,
                             text = "").grid(row = i)
        h3a_1L = tk.Button(h3a_frame,
                           text = "H3A 1 L",
                           font = ("Arial", 20),
                           command = lambda: [window.clear_frame(h3a_frame),
                                              protocols.h3a_1L_click(protocols.open_protocols())]).grid(row = 7, column = 1, padx = 20, pady = 20)
        h3a_2L = tk.Button(h3a_frame,
                           text = "H3A 2 L",
                           font = ("Arial", 20),
                           command = lambda: [window.clear_frame(h3a_frame),
                                              protocols.h3a_2L_click(protocols.open_protocols())]).grid(row = 7, column = 2, padx = 20, pady = 20)
        piLab_home = tk.Button(h3a_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [window.clear_frame(h3a_frame),
                                            main_window.piLab_home()]).grid(row = 8, column = 0, padx = 20, pady = 20)

    def olsen_click():
        olsen_frame = tk.Frame(root)
        olsen_frame.pack()
        for i in range(6):
            label = tk.Label(olsen_frame,
                             text = "").grid(row = i)
        olsen_1L = tk.Button(olsen_frame,
                             text = "Olsen P 1 L",
                             font = ("Arial", 20),
                             command = lambda: [window.clear_frame(olsen_frame),
                                                protocols.olsen_1L_click(protocols.open_protocols())]).grid(row = 7, column = 1, padx = 20, pady = 20)
        olsen_2L = tk.Button(olsen_frame,
                             text = "Olsen P 2 L",
                             font = ("Arial", 20),
                             command = lambda: [window.clear_frame(olsen_frame),
                                                protocols.olsen_2L_click(protocols.open_protocols())]).grid(row = 7, column = 2, padx = 20, pady = 20)
        piLab_home = tk.Button(olsen_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [window.clear_frame(olsen_frame),
                                            main_window.piLab_home()]).grid(row = 8, column = 0, padx = 20, pady = 20)

    def kcl_click():
        kcl_frame = tk.Frame(root)
        kcl_frame.pack()
        for i in range(6):
            label = tk.Label(kcl_frame,
                             text = "").grid(row = i)
        kcl_1N_1L = tk.Button(kcl_frame,
                              text = "1N KCl 1 L",
                              font = ("Arial", 20),
                              command = lambda: [window.clear_frame(kcl_frame),
                                                 protocols.kcl_1N_1L_click(protocols.open_protocols())]).grid(row = 7, column = 1, padx = 20, pady = 20)
        kcl_1N_2L = tk.Button(kcl_frame,
                              text = "1N KCl 2 L",
                              font = ("Arial", 20),
                              command = lambda: [window.clear_frame(kcl_frame),
                                                 protocols.kcl_1N_2L_click(protocols.open_protocols())]).grid(row = 7, column =2, padx = 20, pady = 20)
        kcl_2N_1L = tk.Button(kcl_frame,
                              text = "2N KCl 1 L",
                              font = ("Arial", 20),
                              command = lambda: [window.clear_frame(kcl_frame),
                                                 protocols.kcl_2N_1L_click(protocols.open_protocols())]).grid(row = 8, column =1, padx = 20, pady = 20)
        kcl_2N_2L = tk.Button(kcl_frame,
                              text = "1N KCl 2 L",
                              font = ("Arial", 20),
                              command = lambda: [window.clear_frame(kcl_frame),
                                                 protocols.kcl_2N_2L_click(protocols.open_protocols())]).grid(row = 8, column =2, padx = 20, pady = 20)
        piLab_home = tk.Button(kcl_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [window.clear_frame(kcl_frame),
                                            main_window.piLab_home()]).grid(row = 9, column = 0, padx = 20, pady = 20)

class protocols:
    def open_protocols():
        with open("protocols.txt", mode = "r") as file:
            proto = file.readlines()
            return proto

    def m3_stock_click(proto):
        frame = tk.Frame(root)
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[2:7]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(frame),
                                                   main_window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
    def m3_1L_click(proto):
        frame = tk.Frame(root)
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[8:17]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(frame),
                                                   main_window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
    def m3_2L_click(proto):
        frame = tk.Frame(root)
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[18:26]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(frame),
                                                   main_window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
    def h3a_1L_click(proto):
        frame = tk.Frame(root)
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[29:36]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(frame),
                                                   main_window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
    def h3a_2L_click(proto):
        frame = tk.Frame(root)
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[37:44]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(frame),
                                                   main_window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)

    def olsen_1L_click(proto):
        frame = tk.Frame(root)
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[47:54]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(frame),
                                                   main_window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)

    def olsen_2L_click(proto):
        frame = tk.Frame(root)
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[55:62]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(frame),
                                                   main_window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
    def kcl_1N_1L_click(proto):
        frame = tk.Frame(root)
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[65:70]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(frame),
                                                   main_window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)

    def kcl_1N_2L_click(proto):
        frame = tk.Frame(root)
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[71:76]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(frame),
                                                   main_window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
    def kcl_2N_1L_click(proto):
        frame = tk.Frame(root)
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[77:82]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(frame),
                                                   main_window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)
    def kcl_2N_2L_click(proto):
        frame = tk.Frame(root)
        frame.pack()
        for i in range(4):
            label = tk.Label(frame,
                             text = "").grid(row = i)
        text = tk.Text(frame,
                       height = 10,
                       width = 40,
                       font = ("Arial", 16))
        text.grid(row = 4, column = 1, columnspan = 2, padx = 20, pady = 35)
        recipe = proto[83:88]
        for line in recipe:
            text.insert(tk.END, line)
        home_button = tk.Button(frame,
                                text = "piLab Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(frame),
                                                   main_window.piLab_home()]).grid(row = 5, column = 0, padx = 20, pady = 20)

class skalar_cookbook():
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
                                                   skalar_cookbook.nitrate_frame()]).grid(row = 7, column = 0, padx = 20, pady = 20)
        phos_button = tk.Button(home,
                                text = "Phosphate Channel",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home),
                                                   skalar_cookbook.phosphate_frame()]).grid(row = 7, column = 1, padx = 20, pady = 20)
        ammo_button = tk.Button(home,
                                text = "Ammonium Channel",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home),
                                                   skalar_cookbook.ammonium_frame()]).grid(row = 7, column = 2, padx = 20, pady = 20)
        rins_button = tk.Button(home,
                                text = "Rinsing Liquid",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home),
                                                   skalar_cookbook.volume_frame("rinsing")]).grid(row = 8, column = 0, padx = 20, pady = 20)
        stds_button = tk.Button(home,
                                text = "Calibration Standards",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home),
                                                   skalar_cookbook.standards_frame()]).grid(row = 8, column = 2, padx = 20, pady = 20)
        piLab_home = tk.Button(home,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [window.clear_frame(home),
                                            main_window.piLab_home()]).grid(row = 9, column = 0, padx = 20, pady = 20)

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
                                                   skalar_cookbook.buffer_volume_frame("nitrate_buffer")]).grid(row = 6, column = 1, padx = 20, pady = 20)
        color_reag = tk.Button(nitr_frame,
                               text = "Color Reagent",
                               font = ("Arial", 18),
                               command = lambda: [window.clear_frame(nitr_frame),
                                                   skalar_cookbook.volume_frame("color_reagent")]).grid(row = 6, column = 2, padx = 20, pady = 20)
        home_button = tk.Button(nitr_frame,
                                text = "Skalar Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(nitr_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 7, column =0, padx = 20, pady = 20)

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
                                                   skalar_cookbook.volume_frame("ffd6")]).grid(row = 6, column = 1, padx = 20, pady = 20)
        sulf_button = tk.Button(phos_frame,
                                text = "Sulfuric Acid Solution",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(phos_frame),
                                                   skalar_cookbook.volume_frame("sulfuric_acid")]).grid(row = 6, column = 2, padx = 20, pady = 20)
        hept_button = tk.Button(phos_frame,
                                text = "Ammonium Heptamolybdate",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(phos_frame),
                                                   skalar_cookbook.volume_frame("ammonium_heptamolybdate")]).grid(row = 7, column = 1, padx = 20, pady = 20)
        lplus_button = tk.Button(phos_frame,
                                 text = "L+ Ascorbic Acid",
                                 font = ("Arial", 18),
                                 command = lambda: [window.clear_frame(phos_frame),
                                                   skalar_cookbook.volume_frame("l_plus_ascorbic")]).grid(row = 7, column = 2, padx = 20, pady = 20)
        home_button = tk.Button(phos_frame,
                                text = "Skalar Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(phos_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)

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
                                                   skalar_cookbook.buffer_volume_frame("ammonium_buffer")]).grid(row = 6, column = 1, padx = 20, pady = 20)
        sali_button = tk.Button(ammo_frame,
                                  text = "Sodium Salicyalite Solution",
                                  font = ("Arial", 18),
                                  command = lambda: [window.clear_frame(ammo_frame),
                                                   skalar_cookbook.volume_frame("salicyalite")]).grid(row = 6, column = 2, padx = 20, pady = 20)
        nitro_button = tk.Button(ammo_frame,
                                 text = "Nitroprusside Solution",
                                 font = ("Arial", 18),
                                 command = lambda: [window.clear_frame(ammo_frame),
                                                   skalar_cookbook.volume_frame("nitroprusside")]).grid(row = 7, column = 1, padx = 20, pady = 20)
        dichlo_button = tk.Button(ammo_frame,
                                  text = "Dichlorocyanurite Solution",
                                  font = ("Arial", 18),
                                  command = lambda: [window.clear_frame(ammo_frame),
                                                   skalar_cookbook.volume_frame("dichlorocyanurite")]).grid(row = 7, column = 2, padx = 20, pady = 20)
        home_button = tk.Button(ammo_frame,
                                text = "Skalar Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(ammo_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)
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
                         skalar_cookbook.instruct_frame(skalar_recipes.get_recipe("std1", 100))]).grid(row = 6, column = 0, padx = 20, pady = 40)
        std2 = tk.Button(std_frame,
                         text = "Standard 2",
                         font = ("Arial", 18),
                         command = lambda: [window.clear_frame(std_frame),
                         skalar_cookbook.instruct_frame(skalar_recipes.get_recipe("std2", 100))]).grid(row = 6, column = 1, padx = 20, pady = 40)
        std3 = tk.Button(std_frame,
                         text = "Standard 3",
                         font = ("Arial", 18),
                         command = lambda: [window.clear_frame(std_frame),
                         skalar_cookbook.instruct_frame(skalar_recipes.get_recipe("std3", 100))]).grid(row = 6, column = 2, padx = 20, pady = 40)
        std4 = tk.Button(std_frame,
                         text = "Standard 4",
                         font = ("Arial", 18),
                         command = lambda: [window.clear_frame(std_frame),
                         skalar_cookbook.instruct_frame(skalar_recipes.get_recipe("std4", 100))]).grid(row = 7, column = 1, padx = 20, pady = 40)
        std5 = tk.Button(std_frame,
                         text = "Standard 5",
                         font = ("Arial", 18),
                         command = lambda: [window.clear_frame(std_frame),
                         skalar_cookbook.instruct_frame(skalar_recipes.get_recipe("std5", 100))]).grid(row = 7, column = 2, padx = 20, pady = 40)

        home_button = tk.Button(std_frame,
                                text = "Skalar Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(std_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)

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
                                             skalar_cookbook.instruct_frame(skalar_recipes.get_recipe(reagent, 500))]).grid(row = 6, column = 1, padx = 20, pady = 40)
        vol_2 = tk.Button(vol_frame,
                          text = "1,000 mL",
                          font = ("Arial", 18),
                          command = lambda: [window.clear_frame(vol_frame),
                                             skalar_cookbook.instruct_frame(skalar_recipes.get_recipe(reagent, 1000))]).grid( row = 6, column = 2, padx = 20, pady = 40)
        vol_3 = tk.Button(vol_frame,
                          text = "2,000 mL",
                          font = ("Arial", 18),
                          command = lambda: [window.clear_frame(vol_frame),
                                             skalar_cookbook.instruct_frame(skalar_recipes.get_recipe(reagent, 2000))]).grid(row = 7, column = 1, padx = 20, pady = 40)

        home_button = tk.Button(vol_frame,
                                text = "Skalar Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(vol_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)

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
                                             skalar_cookbook.instruct_frame(skalar_recipes.get_recipe(reagent, 500))]).grid(row = 6, column = 1, padx = 20, pady = 40)
        vol_2 = tk.Button(vol_frame,
                          text = "1,000 mL",
                          font = ("Arial", 18),
                          command = lambda: [window.clear_frame(vol_frame),
                                             skalar_cookbook.instruct_frame(skalar_recipes.get_recipe(reagent, 1000))]).grid( row = 6, column = 2, padx = 20, pady = 40)

        home_button = tk.Button(vol_frame,
                                text = "Skalar Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(vol_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 8, column = 0, padx = 20, pady = 20)

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
                                text = "Skalar Home",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(inst_frame),
                                                   skalar_cookbook.home_frame()]).grid(row = 5, column = 0, padx = 20, pady = 20)
class skalar_recipes:
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

class icp_cookbook():
    def icp_home_frame():
        home_frame = tk.Frame(root)
        home_frame.pack()
        std4_button = tk.Button(home_frame,
                                text = "Standard 4 Elements and Concentrations",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home_frame),
                                                   icp_cookbook.icp_element_frame()]).grid(row = 1, column = 0, padx = 50, pady = 50)
        std3_button = tk.Button(home_frame,
                                text = "Standard 3 Protocol",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home_frame),
                                                   icp_control.std_3_proto()]).grid(row = 1, column = 1, padx = 50, pady = 50)
        std2_button = tk.Button(home_frame,
                                text = "Standard 2 protocol",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home_frame),
                                                   icp_control.std_2_proto()]).grid(row = 2, column = 0, padx = 50, pady =50)
        std1_button = tk.Button(home_frame,
                                text = "Standard 1 Protocol",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(home_frame),
                                                   icp_control.std_1_proto()]).grid(row = 2, column = 1, padx = 50, pady = 50)
        piLab_home = tk.Button(home_frame,
                         text = "piLab Home",
                         font = ("Arial", 18),
                         command = lambda: [window.clear_frame(home_frame),
                                            main_window.piLab_home()]).grid(row = 3, column = 0, padx = 50, pady = 50)

    def icp_element_frame():
        element_frame = tk.Frame(root)
        element_frame.pack()
        Al_button = tk.Button(element_frame,
                                    text = "Aluminium",
                                    font = ("Arial", 18),
                                    command = lambda: [window.clear_frame(element_frame),
                                                    icp_control.stock_solutions("Aluminium")]).grid(row = 1, column = 0,
                                                            padx = 50, pady = 50)
        Ca_button = tk.Button(element_frame,
                                text = "Calcium",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(element_frame),
                                                icp_control.stock_solutions("Calcium")]).grid(row = 1,
                                                                                        column = 1,
                                                                                        padx = 50,
                                                                                        pady = 50)
        Cu_button = tk.Button(element_frame,
                                text = "Copper",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(element_frame),
                                                icp_control.stock_solutions("Copper")]).grid(row = 1,
                                                                                    column = 2,
                                                                                    padx = 50,
                                                                                    pady = 50)
        Fe_button = tk.Button(element_frame,
                                text = "Iron",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(element_frame),
                                                icp_control.stock_solutions("Iron")]).grid(row = 1,
                                                                                    column = 3,
                                                                                    padx = 50,
                                                                                    pady =50)
        K_button = tk.Button(element_frame,
                                text = "Potassium",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(element_frame),
                                                icp_control.stock_solutions("Potassium")]).grid(row = 2,
                                                                                        column = 1,
                                                                                        padx = 50,
                                                                                        pady = 50)
        Mg_button = tk.Button(element_frame,
                                text = "Magnesium",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(element_frame),
                                                icp_control.stock_solutions("Magnesium")]).grid(row = 2,
                                                                                        column = 2,
                                                                                        padx = 50,
                                                                                        pady = 50)
        Mn_button = tk.Button(element_frame,
                                text = "Manganese",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(element_frame),
                                                icp_control.stock_solutions("Manganese")]).grid(row = 2,
                                                                                        column = 3,
                                                                                        padx = 50,
                                                                                        pady = 50)
        Na_Button = tk.Button(element_frame,
                                text = "Sodium",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(element_frame),
                                                icp_control.stock_solutions("Sodium")]).grid(row = 3,
                                                                                    column = 0,
                                                                                    padx = 50,
                                                                                    pady = 50)
        P_button = tk.Button(element_frame,
                                text = "Phosphorus",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(element_frame),
                                                icp_control.stock_solutions("Phosphorus")]).grid(row = 3,
                                                                                        column = 1,
                                                                                        padx = 50,
                                                                                        pady = 50)
        S_button = tk.Button(element_frame,
                                text = "Sulfur",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(element_frame),
                                                icp_control.stock_solutions("Sulfur")]).grid(row = 3,
                                                                                    column = 2,
                                                                                    padx = 50,
                                                                                    pady = 50)
        Zn_button = tk.Button(element_frame,
                                text = "Zinc",
                                font = ("Arial", 18),
                                command = lambda: [window.clear_frame(element_frame),
                                                icp_control.stock_solutions("Zinc")]).grid(row = 3,
                                                                                    column = 3,
                                                                                    padx = 50,
                                                                                    pady = 50)
        piLab_home = tk.Button(element_frame,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [window.clear_frame(element_frame),
                                            main_window.piLab_home()]).grid(row = 4, column = 0, padx = 20, pady = 20)
        icp_home = tk.Button(element_frame,
                             text = "ICP Home",
                             font = ("Arial", 20),
                             command = lambda: [window.clear_frame(element_frame),
                                                icp_cookbook.icp_home_frame()]).grid(row = 4, column = 1, padx = 20, pady = 20)

class icp_control:
    def std_3_proto():
        proto = protocols.open_protocols()
        std_3 = tk.Frame(root)
        std_3.pack()
        text = tk.Text(std_3,
                       height = 6,
                       width = 50,
                       font = ("Arial", 18))
        text.grid(row = 0, column = 0, padx = 20, pady =20)
        for line in proto[90:94]:
            text.insert(tk.END, line)
        piLab_home = tk.Button(std_3,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [window.clear_frame(std_3),
                                            main_window.piLab_home()]).grid(row = 1, column = 0, padx = 20, pady = 20)
        icp_home = tk.Button(std_3,
                             text = "ICP Home",
                             font = ("Arial", 20),
                             command = lambda: [window.clear_frame(std_3),
                                                icp_cookbook.icp_home_frame()]).grid(row = 1, column = 2, padx = 20, pady = 20)

    def std_2_proto():
        proto = protocols.open_protocols()
        std_2 = tk.Frame(root)
        std_2.pack()
        text = tk.Text(std_2,
                       height = 6,
                       width = 50,
                       font = ("Arial", 18))
        text.grid(row = 0, column = 0, padx = 20, pady =20)
        for line in proto[95:99]:
            text.insert(tk.END, line)
        piLab_home = tk.Button(std_2,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [window.clear_frame(std_2),
                                            main_window.piLab_home()]).grid(row = 1, column = 0, padx = 20, pady = 20)
        icp_home = tk.Button(std_2,
                             text = "ICP Home",
                             font = ("Arial", 20),
                             command = lambda: [window.clear_frame(std_2),
                                                icp_cookbook.icp_home_frame()]).grid(row = 1, column = 2, padx = 20, pady = 20)

    def std_1_proto():
        proto = protocols.open_protocols()
        std_1 = tk.Frame(root)
        std_1.pack()
        text = tk.Text(std_1,
                       height = 6,
                       width = 50,
                       font = ("Arial", 18))
        text.grid(row = 0, column = 0, padx = 20, pady =20)
        for line in proto[100:104]:
            text.insert(tk.END, line)
        piLab_home = tk.Button(std_1,
                         text = "piLab Home",
                         font = ("Arial", 20),
                         command = lambda: [window.clear_frame(std_1),
                                            main_window.piLab_home()]).grid(row = 1, column = 0, padx = 20, pady = 20)
        icp_home = tk.Button(std_1,
                             text = "ICP Home",
                             font = ("Arial", 20),
                             command = lambda: [window.clear_frame(std_1),
                                                icp_cookbook.icp_home_frame()]).grid(row = 1, column = 2, padx = 20, pady = 20)

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
                             command = lambda: [window.clear_frame(stock_select),
                                                icp_control.desired_conc(1000, element)]).grid(row = 1,
                                                                              column = 0,
                                                                              pady = 20)
        ppm_10000 = tk.Button(stock_select,
                             font = ("Arial", 18),
                             text = "10,000 ppm " + element,
                             command = lambda: [window.clear_frame(stock_select),
                                                icp_control.desired_conc(10000, element),]).grid(row = 2,
                                                                              column = 0,
                                                                              pady = 20)
        home_button = tk.Button(stock_select,
                                font = ("Arial", 18),
                                text = "ICP Home",
                                command = lambda: [window.clear_frame(stock_select),
                                    icp_cookbook.icp_home_frame()]).grid(row = 3,
                                                                     column = 0,
                                                                     pady = 20)

    def desired_conc(stock_conc, element):
        element = element
        stock_conc = stock_conc
        conc_frame = tk.Frame(root)
        conc_frame.pack()
        concentrations = []
        conc_label = tk.Label(conc_frame,
                              text = "Select the desired concentration For Standard 4",
                              font = ("Arial", 18)).grid(row = 0, columnspan = 5)
        # conc_1 = tk.Button(conc_frame,
        #                   text = "0.25 ppm",
        #                   font = ("Arial", 15),
        #                   command = lambda: [concentrations.append(0.25),
        #                                      text.insert(tk.END, "0.25 ppm" + "\n")]).grid(row = 1, column = 0, padx = 25, pady = 20)
        # conc_2 = tk.Button(conc_frame,
        #                   text = "0.50 ppm",
        #                   font = ("Arial", 15),
        #                   command = lambda: [concentrations.append(0.50),
        #                                     text.insert(tk.END, "0.50 ppm" + "\n")]).grid(row = 1, column = 1, padx = 25, pady = 20)
        # conc_3 = tk.Button(conc_frame,
        #                   text = "1.0 ppm",
        #                   font = ("Arial", 15),
        #                   command = lambda: [concentrations.append(1.0),
        #                                      text.insert(tk.END, "1.0 ppm" + "\n")]).grid(row = 1, column = 2, padx = 25, pady = 20)
        # conc_4 = tk.Button(conc_frame,
        #                   text = "2.5 ppm",
        #                   font = ("Arial", 15),
        #                   command = lambda: [concentrations.append(2.5),
        #                                      text.insert(tk.END, "2.5 ppm" + "\n")]).grid(row = 1, column = 3, padx = 25, pady = 20)
        # conc_5 = tk.Button(conc_frame,
        #                   text = "5.0 ppm",
        #                   font = ("Arial", 15),
        #                   command = lambda: [concentrations.append(5.0),
        #                                      text.insert(tk.END, "5.0 ppm" + "\n")]).grid(row = 1, column = 4, padx = 25, pady = 20)
        conc_6 = tk.Button(conc_frame,
                           text = "10.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(10.0),
                                              text.insert(tk.END, "10.0 ppm" + "\n")]).grid(row = 2, column = 0, padx = 25, pady = 20)
        conc_7 = tk.Button(conc_frame,
                           text = "20.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(20.0),
                                              text.insert(tk.END, "20.0 ppm" + "\n")]).grid(row = 2, column = 2, padx = 25, pady = 20)
        # conc_8 = tk.Button(conc_frame,
        #                   text = "25.0 ppm",
        #                   font = ("Arial", 15),
        #                   command = lambda: [concentrations.append(25.0),
        #                                      text.insert(tk.END, "25.0 ppm" + "\n")]).grid(row = 2, column = 2, padx = 25, pady = 20)
        conc_9 = tk.Button(conc_frame,
                           text = "40.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(40.0),
                                              text.insert(tk.END, "40.0 ppm" + "\n")]).grid(row = 2, column = 4, padx = 25, pady = 20)
        # conc_10 = tk.Button(conc_frame,
        #                   text = "50.0 ppm",
        #                   font = ("Arial", 15),
        #                   command = lambda: [concentrations.append(50.0),
        #                                      text.insert(tk.END, "50.0 ppm" + "\n")]).grid(row = 2, column = 4, padx = 25, pady = 20)
        conc_11 = tk.Button(conc_frame,
                           text = "100.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(100.0),
                                              text.insert(tk.END, "100.0 ppm" + "\n")]).grid(row = 3, column = 0, padx = 25, pady = 20)
        # conc_12 = tk.Button(conc_frame,
        #                   text = "200.0 ppm",
        #                   font = ("Arial", 15),
        #                   command = lambda: [concentrations.append(200.0),
        #                                      text.insert(tk.END, "200.0 ppm" + "\n")]).grid(row = 3, column = 1, padx = 25, pady = 20)
        # conc_13 = tk.Button(conc_frame,
        #                   text = "400.0 ppm",
        #                   font = ("Arial", 15),
        #                   command = lambda: [concentrations.append(400.0),
        #                                      text.insert(tk.END, "400.0 ppm" + "\n")]).grid(row = 3, column = 2, padx = 25, pady = 20)
        conc_14 = tk.Button(conc_frame,
                           text = "800.0 ppm",
                           font = ("Arial", 15),
                           command = lambda: [concentrations.append(800.0),
                                              text.insert(tk.END, "800.0 ppm" + "\n")]).grid(row = 3, column = 4, padx = 25, pady = 20)
        blank_1 = tk.Label(conc_frame,
                            text = "",
                            font = ("Arial", 15)).grid(row = 2, column = 1, padx = 25, pady = 20)
        blank_2 = tk.Label(conc_frame,
                            text = "",
                            font = ("Arial", 15)).grid(row = 2, column = 3, padx = 25, pady = 20)
        blank_3 = tk.Label(conc_frame,
                            text = "",
                            font = ("Arial", 15)).grid(row = 3, column = 1, padx = 25, pady = 20)
        blank_4 = tk.Label(conc_frame,
                            text = "",
                            font = ("Arial", 15)).grid(row = 3, column = 2, padx = 25, pady = 20)
        blank_5 = tk.Label(conc_frame,
                            text = "",
                            font = ("Arial", 15)).grid(row = 3, column = 3, padx = 25, pady = 20)
        text = tk.Text(conc_frame,
                       height = 5,
                       width = 40,
                       font = ("Arial", 18))
        text.grid(row = 4, columnspan = 5, padx = 25, pady = 15)

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
                                command = lambda: [window.clear_frame(conc_frame),
                                                   icp_control.std_instructions(icp_math.calculate_conc(stock_conc, concentrations), element)]).grid(row =5,
                                                                                         column = 2,
                                                                                         padx = 10,
                                                                                         pady = 10)
        home_button = tk.Button(conc_frame,
                                font = ("Arial", 18),
                                text = "ICP Home",
                                command = lambda: [window.clear_frame(conc_frame),
                                    icp_cookbook.icp_home_frame()]).grid(row = 5,
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
                                text = "ICP Home",
                                command = lambda: [window.clear_frame(instruct_frame),
                                    icp_cookbook.icp_home_frame()])
        home_button.pack(padx = 25, pady = 30)

class icp_math:
    def calculate_conc(stock_concentrations, final_concentrations):
        stock = stock_concentrations
        final = final_concentrations
        std_lst = []
        for i in range(len(final_concentrations)):
            std = (final[i] * 250) / stock * 1000
            std_lst.append(std)
        return std_lst


# Create root GUI
root = tk.Tk()
root.title("piLab By John Sorensen")
root.geometry("1024x600")
root.resizable(width = False, height = False)
main_window.piLab_home()


# Loop root window
root.mainloop()
