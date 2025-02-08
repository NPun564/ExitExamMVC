import tkinter as tk
from tkinter import messagebox
from Controller import InventoryController

class InventoryView:
    def __init__(self, root):
        self.controller = InventoryController()
        self.root = root
        self.root.title("ระบบนำเข้าข้อมูลคลังสินค้า")

        # กำหนดขนาดหน้าต่าง
        self.root.geometry('400x400')  # ขนาดหน้าต่าง

        # เพิ่ม label และช่องกรอกข้อมูลและปรับขนาดตัวอักษร
        tk.Label(root, text="รหัสสินค้า:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=10)
        self.product_id_entry = tk.Entry(root, font=("Arial", 14), width=20)  # ขยายช่องกรอกข้อมูล
        self.product_id_entry.grid(row=0, column=1, padx=10, pady=10)

        # เลือกประเภทสินค้า
        tk.Label(root, text="ประเภทสินค้า:", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=10)
        self.category_var = tk.StringVar()
        self.category_menu = tk.OptionMenu(root, self.category_var, "อาหาร", "อิเล็กทรอนิกส์", "เสื้อผ้า", command=self.show_expiration_field)
        self.category_menu.config(font=("Arial", 14))
        self.category_menu.grid(row=1, column=1, padx=10, pady=10)

        # ช่องวันหมดอายุ (สำหรับอาหาร)
        self.exp_date_label = tk.Label(root, text="วันหมดอายุ :", font=("Arial", 14))
        self.exp_date_label.grid(row=2, column=0, padx=10, pady=10)
        self.exp_date_entry = tk.Entry(root, font=("Arial", 14), width=20)
        
        # ช่องกรอกสภาพสินค้า (ใช้ OptionMenu)
        tk.Label(root, text="สภาพสินค้า:", font=("Arial", 14)).grid(row=3, column=0, padx=10, pady=10)
        self.condition_var = tk.StringVar()
        self.condition_menu = tk.OptionMenu(root, self.condition_var, "ปกติ", "เสียหาย", "ต้องตรวจสอบเพิ่ม")
        self.condition_menu.config(font=("Arial", 14))
        self.condition_menu.grid(row=3, column=1, padx=10, pady=10)

        # เพิ่มปุ่มและขยายขนาดของปุ่ม
        self.add_button = tk.Button(root, text="เพิ่มสินค้า", font=("Arial", 14), width=20, height=2, command=self.add_product)
        self.add_button.grid(row=4, columnspan=2, pady=20)

        # เรียกใช้ฟังก์ชันเพื่อตรวจสอบว่าแสดงช่องไหน
        self.show_expiration_field(self.category_var.get())

    def show_expiration_field(self, category):
        """ แสดง/ซ่อนช่องกรอกวันหมดอายุ """
        if category == "อาหาร":
            self.exp_date_label.grid(row=2, column=0, padx=10, pady=10)
            self.exp_date_entry.grid(row=2, column=1, padx=10, pady=10)
        else:
            self.exp_date_label.grid_forget()
            self.exp_date_entry.grid_forget()

    def add_product(self):
        # รับข้อมูลจากฟอร์ม
        product_id = self.product_id_entry.get()
        category = self.category_var.get()
        exp_date = self.exp_date_entry.get() if category == "อาหาร" else ""  # รับวันหมดอายุเฉพาะถ้าเป็นอาหาร
        condition = self.condition_var.get()

        # ตรวจสอบข้อมูลก่อนส่งไปยัง controller
        if not product_id or not category or not condition:
            messagebox.showwarning("ข้อมูลไม่ครบ", "กรุณากรอกข้อมูลให้ครบถ้วน รหัสสินค้า, ประเภทสินค้า, สภาพสินค้า")
            return

        # ส่งข้อมูลไปยัง controller
        result = self.controller.add_product(product_id, category, exp_date, condition)

        # แสดงผลลัพธ์
        messagebox.showinfo("ผลลัพธ์", result)
