# นำเข้า YOLO จากไลบรารี ultralytics สำหรับการวิเคราะห์
from ultralytics import YOLO
# นำเข้า tkinter สำหรับการสร้าง GUI
from tkinter import*
# นำเข้า askopenfilename จาก tkinter.filedialog สำหรับการเลือกไฟล์
from tkinter.filedialog import*

# โหลดโมเดล YOLO โดยใช้ไฟล์โมเดลที่ชื่อ "best.pt"
model = YOLO("best.pt")

# สร้างหน้าต่างหลักของ GUI โดยใช้ tkinter
root = Tk()
root.title("Lung abnormality screening program") # ตั้งชื่อหน้าต่าง
root.geometry("400x350") # กำหนดขนาดหน้าต่างเป็น 400x350 พิกเซล
root.resizable(False,False) # ปิดการปรับขนาดหน้าต่าง
root.config(background="#F2D3BA") # ตั้งค่าพื้นหลังของหน้าต่างเป็นสี #F2D3BA
root.option_add('*font','tahoma 10 bold') # ตั้งค่า font เริ่มต้นของ GUI เป็น Tahoma ขนาด 10 ตัวหนา


# ฟังก์ชันสำหรับวิเคราะห์ภาพจาก path ที่ผู้ใช้ป้อนเอง
def analyze():
    path = txt.get() # รับค่า path จาก Entry widget จากช่องข้อความที่ผู้ใช้ป้อน
    path = str(path) # แปลง path ให้เป็น string
    results = model(path)   # ใช้โมเดล YOLO วิเคราะห์ภาพที่ path ที่ผู้ใช้ป้อน
    # แสดงผลลัพธ์การวิเคราะห์
    results[0].show()


# ฟังก์ชันสำหรับวิเคราะห์ภาพจาก path ที่ผู้ใช้เลือกจากโฟลเดอร์
def analyzeauto():
    path = askopenfilename() # เปิดหน้าต่างให้ผู้ใช้เลือกไฟล์ และเก็บ path ของไฟล์ที่เลือก
    # แสดง path ของไฟล์ที่เลือกในหน้าต่าง GUI
    L4 = Label(root,text=path,bg="#F2D3BA",font=('Tahoma',10))
    L4.place(x=100,y=300) # วาง Label ที่ตำแหน่ง (100, 300)
    path = str(path) # แปลง path ให้เป็น string
    results = model(path)   # ใช้โมเดล YOLO วิเคราะห์ภาพที่ path ที่ผู้ใช้เลือก
    results[0].show() # แสดงผลลัพธ์การวิเคราะห์

# สร้าง Label สำหรับแสดงข้อความ "Select file to analysis"
L1 = Label(root,text="Select file to analysis",bg="#F2D3BA",font=('Tahoma',20)) 
L1.place(x=85,y=25) # วาง Label ที่ตำแหน่ง (85, 25)

# สร้าง Label สำหรับแสดงข้อความ "Insert path by manual"
L2 = Label(root,text="Insert path by manual",bg="#F2D3BA",font=('Tahoma',10))
L2.place(x=100,y=75) # วาง Label ที่ตำแหน่ง (100, 75)

# สร้างตัวแปร StringVar สำหรับเก็บข้อความที่ผู้ใช้ป้อนในช่องข้อความ
txt=StringVar()

# สร้างช่องข้อความ (Entry) ให้ผู้ใช้ป้อน path ของไฟล์
TXT1 = Entry(root,textvariable=txt,font=20) 
TXT1.place(x=100,y=100)  # วางช่องข้อความที่ตำแหน่ง (100, 100)

# สร้างปุ่ม Analyze สำหรับวิเคราะห์ภาพจาก path ที่ผู้ใช้ป้อนเอง
# โดยใช้ฟังก์ชัน analyze
# ปุ่มนี้จะเรียกใช้ฟังก์ชัน analyze เมื่อคลิก
BTN1 = Button(root,text="Analyze",bg="#C6D9BB",font=('Tahoma',13),command=analyze)
BTN1.place(x=175,y=150) # วางปุ่มที่ตำแหน่ง (175, 150)

# สร้าง Label สำหรับแสดงข้อความ "Insert path from folder"
L3 = Label(root,text="Insert path from folder",bg="#F2D3BA",font=('Tahoma',10))
L3.place(x=100,y=210) # วาง Label ที่ตำแหน่ง (100, 210)


# สร้างปุ่ม Analyze สำหรับวิเคราะห์ภาพจาก path ที่ผู้ใช้เลือกจากโฟลเดอร์
# โดยใช้ฟังก์ชัน analyzeauto
# ปุ่มนี้จะเปิดหน้าต่างให้ผู้ใช้เลือกไฟล์และวิเคราะห์ภาพที่เลือก
BTN2 = Button(root,text="Analyze",bg="#C6D9BB",font=('Tahoma',13),command=analyzeauto) 
BTN2.place(x=175,y=250) # วางปุ่มที่ตำแหน่ง (175, 250)

# เริ่มต้น loop ของ GUI เพื่อให้โปรแกรมทำงานและรอรับคำสั่งจากผู้ใช้
root.mainloop()


