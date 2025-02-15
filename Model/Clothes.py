import csv

class ClothingModel:
    """ เก็บข้อมูลประเภทสินค้าในไฟล์ ClothesStock"""
    def __init__(self, db_file="ClothesStock.csv"): 
        self.db_file = db_file
        """เรียกใช้ฟังก์ชัน load_data() เพื่อโหลดข้อมูลจากไฟล์ CSV เข้ามาเก็บในตัวแปร self.data """
        self.load_data() 

    def load_data(self):
        """ โหลดข้อมูลสินค้าเสื้อผ้าจากไฟล์ CSV """
        try:
            with open(self.db_file, mode='r', newline='', encoding='utf-8') as file:
                """อ่านไฟล์ CSV และแปลงข้อมูลแต่ละแถวให้เป็น dictionary ที่เก็บข้อมูลของแต่ละสินค้า """
                reader = csv.DictReader(file)
                self.data = list(reader)
            """ถ้าไม่พบในไฟล์ CSV จะตั้งค่าตัวแปร self.data เป็น [] """
        except FileNotFoundError:
            self.data = []

    def save_data(self):
        """ บันทึกข้อมูลสินค้าเสื้อผ้าลงในไฟล์ CSV """
        with open(self.db_file, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ["product_id", "category", "condition"]  # ไม่ต้องมี expiration_date สำหรับเสื้อผ้า
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.data)

    def add_product(self, product_id, category, expiration_date, condition):
        """ เพิ่มสินค้าเสื้อผ้าใหม่ """
        if len(product_id) != 6 or product_id[0] == '0' or any(p['product_id'] == product_id for p in self.data):
            return "รหัสสินค้าไม่ถูกต้อง หรือซ้ำ"

        # ตรวจสอบเงื่อนไขสำหรับสินค้าเสื้อผ้า
        if condition == "เสียหาย":
            return "ไม่รับสินค้าที่เสียหาย"
        
        self.data.append({
            "product_id": product_id,
            "category": category,
            "condition": condition
        })
        self.save_data()
        return "บันทึกสินค้าเสื้อผ้าเรียบร้อยแล้ว"
