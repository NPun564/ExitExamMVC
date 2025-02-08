from View import InventoryView
import tkinter as tk

def main():
    root = tk.Tk()
    app = InventoryView(root)
    root.mainloop()  # เรียกใช้ root.mainloop() ที่นี่เพื่อเริ่ม GUI

if __name__ == "__main__":
    main()
