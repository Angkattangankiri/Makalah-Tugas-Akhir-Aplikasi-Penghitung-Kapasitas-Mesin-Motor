import tkinter as tk
from tkinter import messagebox
import math
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from math import pi

# KELAS
class KapasitasMesinApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Penghitung Kapasitas Mesin")
        self.root.geometry("1366x720")
        
        self.notebook = ttk.Notebook(root)
        
        self.tab1 = tk.Frame(self.notebook)
        self._setup_tab1()

        self.tab2 = tk.Frame(self.notebook)
        self._setup_tab2()

        self.notebook.add(self.tab1, text="Informasi")
        self.notebook.add(self.tab2, text="Kapasitas Mesin")

        self.notebook.pack(expand=True, fill="both")
        
        self.motor_directory = [] 

    def _setup_tab1(self):
        image_path = "d:/TA/photomode_17122020_235104.png"
        img = Image.open(image_path)
        img = img.resize((1366, 720))  
        photo = ImageTk.PhotoImage(img)

        label_image = tk.Label(self.tab1, image=photo)
        label_image.place(x=0, y=0, relwidth=1, relheight=1)  
        label_image.image = photo  

        label_info = tk.Label(self.tab1, text="Selamat datang di aplikasi Penghitung Kapasitas Mesin Motor.", bg="white")
        label_info.pack(pady=20)
        label_info_detail = tk.Label(self.tab1, text="Dibuat dan Didesain oleh Rio Hotasy Parulian Simanjuntak", bg="white")
        label_info_detail.pack(pady=5)
    
    def _setup_tab2(self):

        image_path = "d:\TA\Gaming_5000x3125.jpg"
        img = Image.open(image_path)
        img = img.resize((1366, 720))  
        photo = ImageTk.PhotoImage(img)

        label_image = tk.Label(self.tab2, image=photo)
        label_image.place(x=0, y=0, relwidth=1, relheight=1)  
        label_image.image = photo  
   
        frame_center = tk.Frame(self.tab2)
        frame_center.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)


        frame_center.grid_rowconfigure(0, weight=1)
        frame_center.grid_rowconfigure(1, weight=1)
        frame_center.grid_rowconfigure(2, weight=1)
        frame_center.grid_rowconfigure(3, weight=1)
        frame_center.grid_rowconfigure(4, weight=1)  
        frame_center.grid_columnconfigure(0, weight=1)
        frame_center.grid_columnconfigure(1, weight=3)

  
        self.tab2.grid_rowconfigure(0, weight=1)  
        self.tab2.grid_columnconfigure(0, weight=1)  

   
        self.label_name = tk.Label(frame_center, text="Nama Motor:")
        self.label_name.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.entry_name = tk.Entry(frame_center)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

    
        self.label_diameter = tk.Label(frame_center, text="Diameter Piston (cm):")
        self.label_diameter.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.entry_diameter = tk.Entry(frame_center)
        self.entry_diameter.grid(row=1, column=1, padx=10, pady=5)

    
        self.label_langkah = tk.Label(frame_center, text="Langkah Piston (cm):")
        self.label_langkah.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.entry_langkah = tk.Entry(frame_center)
        self.entry_langkah.grid(row=2, column=1, padx=10, pady=5)

        self.label_silinder = tk.Label(frame_center, text="Jumlah Silinder:")
        self.label_silinder.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.entry_silinder = tk.Entry(frame_center)
        self.entry_silinder.grid(row=3, column=1, padx=10, pady=5)

        self.button_hitung = tk.Button(frame_center, text="Hitung CC", command=self.hitung_cc)
        self.button_hitung.grid(row=4, columnspan=2, pady=10)

        self.button_show_directory = tk.Button(frame_center, text="Tampilkan Direktori Motor", command=self.show_directory)
        self.button_show_directory.grid(row=5, columnspan=2, pady=10)

        self.label_hasil = tk.Label(frame_center, text="Hasil Kapasitas Mesin: -")
        self.label_hasil.grid(row=6, columnspan=2, pady=10)

        self.label_delete = tk.Label(frame_center, text="Hapus Motor dari Direktori:")
        self.label_delete.grid(row=7, column=0, padx=10, pady=5, sticky="e")

        self.motor_name_delete = tk.StringVar()
        self.option_menu_delete = tk.OptionMenu(frame_center, self.motor_name_delete, [])
        self.option_menu_delete.grid(row=7, column=1, padx=10, pady=5)

        self.button_delete = tk.Button(frame_center, text="Hapus Motor", command=self.delete_motor)
        self.button_delete.grid(row=8, columnspan=2, pady=10)



    def hitung_cc(self):
        try:
            motor_name = self.entry_name.get()  
            diameter = float(self.entry_diameter.get())  
            langkah = float(self.entry_langkah.get()) 
            silinder = int(self.entry_silinder.get())  

            radius = diameter / 2
            cc_per_cylinder = pi * (radius ** 2) * langkah  

            total_cc = cc_per_cylinder * silinder

            motor_info = {
                "name": motor_name, 
                "diameter": diameter,
                "langkah": langkah,
                "silinder": silinder,
                "cc": total_cc
            }
            self.motor_directory.append(motor_info)

            self.update_motor_dropdown()

            self.label_hasil.config(text=f"Hasil Kapasitas Mesin: {total_cc:.2f} cc")
        except ValueError:
            self.label_hasil.config(text="Masukkan data yang valid.")

    def show_directory(self):
        if not self.motor_directory:
            self.label_hasil.config(text="Direktori motor kosong.")
            return
        
        directory_text = "Direktori Motor:\n"
        for i, motor in enumerate(self.motor_directory, start=1):
            directory_text += (f"Motor {i} ({motor['name']}) - Diameter: {motor['diameter']} cm, "
                               f"Langkah: {motor['langkah']} cm, "
                               f"Silinder: {motor['silinder']}, "
                               f"CC: {motor['cc']:.2f} cc\n")
        
        self.label_hasil.config(text=directory_text)

    def update_motor_dropdown(self):
        """ Update the OptionMenu with current motor names """
        motor_names = [motor['name'] for motor in self.motor_directory]
        self.motor_name_delete.set('') 
        menu = self.option_menu_delete["menu"]
        menu.delete(0, "end")  
        for name in motor_names:
            menu.add_command(label=name, command=tk._setit(self.motor_name_delete, name))

    def delete_motor(self):
        motor_to_delete = self.motor_name_delete.get()
        if not motor_to_delete:
            messagebox.showwarning("Peringatan", "Pilih motor yang ingin dihapus.")
            return

        for motor in self.motor_directory:
            if motor['name'] == motor_to_delete:
                self.motor_directory.remove(motor)
                self.update_motor_dropdown()  
                messagebox.showinfo("Sukses", f"Motor '{motor_to_delete}' telah dihapus.")
                self.show_directory()  
                return
        
        messagebox.showerror("Error", "Motor tidak ditemukan.")

root = tk.Tk()
app = KapasitasMesinApp(root)
root.mainloop()
