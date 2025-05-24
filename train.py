# นำเข้า YOLO จากไลบรารี ultralytics สำหรับการฝึกโมเดล
from ultralytics import YOLO

# โหลดโมเดล YOLO ที่ชื่อ "yolo11n.pt"
model = YOLO("yolo11n.pt")

# ฝึกโมเดลด้วยข้อมูลที่กำหนดในไฟล์ "datasets\data.yaml"
train_results = model.train(
    data="datasets\data.yaml",  # ไฟล์กำหนดข้อมูลการฝึก เช่น path ของ dataset และ class
    epochs=100,    # จำนวนรอบ (epochs) ที่จะฝึกโมเดล
    imgsz=640,    # ขนาดของภาพ (image size) ที่ใช้ในการฝึก
    device="0",   # ใช้ GPU หมายเลข 0 สำหรับการฝึก (ถ้ามี GPU)
)

# ประเมินผลโมเดลหลังการฝึก
# ทำการวัดผล (validation) เพื่อดูประสิทธิภาพของโมเดล เช่น mAP, precision, recall
metrics = model.val()