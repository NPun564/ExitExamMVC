from Model.Food import FoodModel
from Model.Electronics import ElectronicsModel
from Model.Clothes import ClothingModel

class InventoryController:
    def __init__(self):
        self.food_model = FoodModel()
        self.electronics_model = ElectronicsModel()
        self.clothing_model = ClothingModel()

    # เพิ่มสินค้าลงใน Model ตามประเภทสินค้าที่ได้รับ
    def add_product(self, product_id, category, expiration_date, condition):
        if category == "อาหาร":
            # กรอกวันหมดอายุเฉพาะสินค้าอาหาร
            if not expiration_date:
                return "กรุณากรอกวันหมดอายุสำหรับสินค้าอาหาร"
            return self.food_model.add_product(product_id, category, expiration_date, condition)
        
        elif category == "อิเล็กทรอนิกส์":
            # สินค้าอิเล็กทรอนิกส์ไม่ต้องกรอกวันหมดอายุ
            if expiration_date:
                expiration_date = ""  # ลบวันหมดอายุออกหากเป็นสินค้าอิเล็กทรอนิกส์
            return self.electronics_model.add_product(product_id, category, expiration_date, condition)  # ส่ง condition ไปด้วย
        
        elif category == "เสื้อผ้า":
            # สินค้าเสื้อผ้าไม่ต้องกรอกวันหมดอายุ
            if expiration_date:
                expiration_date = ""  # ลบวันหมดอายุออกหากเป็นสินค้าเสื้อผ้า
            return self.clothing_model.add_product(product_id, category, expiration_date, condition)  # ส่ง condition ไปด้วย
        
        else:
            return "ประเภทสินค้ายังไม่ได้รับการกำหนด"
