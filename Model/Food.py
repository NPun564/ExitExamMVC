import csv
from datetime import datetime

class FoodModel:
    """ เก็บข้อมูลประเภทสินค้าในไฟล์ FoodStock"""
    def __init__(self, db_file="FoodStock.csv"):
        self.db_file = db_file
        """เรียกใช้ฟังก์ชัน load_data() เพื่อโหลดข้อมูลจากไฟล์ CSV เข้ามาเก็บในตัวแปร self.data """
        self.load_data()

    def load_data(self):
        """ โหลดข้อมูลสินค้าอาหารจากไฟล์ CSV """
        try:
            with open(self.db_file, mode='r', newline='', encoding='utf-8') as file:
                """อ่านไฟล์ CSV และแปลงข้อมูลแต่ละแถวให้เป็น dictionary ที่เก็บข้อมูลของแต่ละสินค้า """
                reader = csv.DictReader(file)
                self.data = list(reader)
            """ถ้าไม่พบในไฟล์ CSV จะตั้งค่าตัวแปร self.data เป็น [] """
        except FileNotFoundError:
            self.data = []

    def save_data(self):
        """ บันทึกข้อมูลสินค้าอาหารลงในไฟล์ CSV """
        with open(self.db_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["product_id", "category", "expiration_date", "condition"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)

    def add_product(self, product_id, category, expiration_date, condition):
        """ เพิ่มสินค้าอาหารใหม่ """
        if len(product_id) != 6 or product_id[0] == '0' or any(p['product_id'] == product_id for p in self.data):
            return "รหัสสินค้าไม่ถูกต้อง หรือซ้ำ"
        
        # ตรวจสอบวันหมดอายุสำหรับอาหาร
        try:
            # แปลงวันหมดอายุที่กรอกมาเป็น datetime object
            expiration_date = datetime.strptime(expiration_date, '%d/%m/%Y')
        except ValueError:
            return "รูปแบบวันหมดอายุไม่ถูกต้อง กรุณากรอกในรูปแบบ วัน/เดือน/ปี"

        today = datetime.today()  # วันปัจจุบัน
        if expiration_date < today:
            return "หมดอายุแล้ว! ไม่สามารถเพิ่มสินค้าได้"

        self.data.append({
            "product_id": product_id,
            "category": category,
            "expiration_date": expiration_date.strftime('%d/%m/%Y'),  # แปลงกลับเป็น string เพื่อบันทึกใน CSV
            "condition": condition
        })
        self.save_data()
        return "บันทึกสินค้าอาหารเรียบร้อยแล้ว"
