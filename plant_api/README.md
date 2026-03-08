# 🌱 Plant Database Web Application

## รายละเอียดโปรเจกต์

โปรเจกต์นี้เป็นเว็บแอปพลิเคชันสำหรับแสดง **ฐานข้อมูลพืช (Plant Database)**
พัฒนาโดยใช้ **Python และ FastAPI** พร้อมใช้ **Jinja2 Template** สำหรับแสดงผลหน้าเว็บ และ **HTML / CSS** สำหรับส่วนของ UI

หน้าเว็บจะแสดงรายการพืช เช่น

* รหัสพืช (ID)
* ชื่อพืช (Name)

---

# เทคโนโลยีที่ใช้

* Python
* FastAPI
* Uvicorn
* Jinja2
* HTML
* CSS

---

# โครงสร้างโปรเจกต์

```
project/
│
├── main.py
├── requirements.txt
├── pyproject.toml
├── README.md
│
├── database
│   ├── memory_db.py
│   └── plant_repository.py
│
├── models
│   ├── plant.py
│   ├── tree.py
│   └── flower.py
│
├── services
│
├── templates
│   └── index.html
│
└── static
    └── style.css
```

---

# หลักการออกแบบ (SOLID Principles)

โปรเจกต์นี้ออกแบบโดยใช้แนวคิด **SOLID**

**S – Single Responsibility Principle**
แต่ละไฟล์มีหน้าที่เฉพาะ เช่น

* models → เก็บโครงสร้างข้อมูลพืช
* database → จัดการข้อมูล
* services → business logic

**O – Open/Closed Principle**
ระบบสามารถเพิ่มชนิดพืชใหม่ได้โดยไม่ต้องแก้โค้ดหลัก

**L – Liskov Substitution Principle**
คลาส `Tree` และ `Flower` สามารถใช้แทน `Plant` ได้

**I – Interface Segregation Principle**
Repository ถูกแยกหน้าที่เฉพาะในการเข้าถึงข้อมูล

**D – Dependency Inversion Principle**
Service ทำงานผ่าน abstraction ของ repository

---

# วิธีติดตั้ง

ติดตั้ง library ที่จำเป็น

```
pip install -r requirements.txt
```

---

# วิธีรันโปรแกรม

```
uvicorn main:app --reload
```

---

# วิธีใช้งาน

เปิดเว็บเบราว์เซอร์และเข้าไปที่

```
http://127.0.0.1:8000
```

ระบบจะแสดงหน้า **Plant Database** พร้อมรายการพืชในฐานข้อมูล

---

# ตัวอย่างการทำงาน

หน้าเว็บจะแสดงตารางข้อมูล เช่น

| ID | Name  |
| -- | ----- |
| 1  | Mango |
| 2  | Rose  |
| 3  | Lotus |

---

# ผู้พัฒนา
นายณัฐดนัย ทองสรรค์
รหัสนักศึกษา 68114540184