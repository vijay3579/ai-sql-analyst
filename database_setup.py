import sqlite3
import pandas as pd

conn=sqlite3.connect("hospital.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients(
	patient_id INTEGER PRIMARY KEY,
	name TEXT,
	age INTEGER,
	gender TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS encounters(
	encounter_id INTEGER PRIMARY KEY,
	patient_id INTEGER,
	hospital TEXT,
	department TEXT,
	admission_date TEXT,
	FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS billing (
    bill_id INTEGER PRIMARY KEY,
    encounter_id INTEGER,
    amount REAL,
    FOREIGN KEY(encounter_id) REFERENCES encounters(encounter_id)
)
""")

patients_data = [
    (1,"John Doe",45,"M"),
    (2,"Jane Smith",34,"F"),
    (3,"Mike Johnson",60,"M"),
    (4,"Emily Davis",29,"F"),
    (5,"Robert Brown",50,"M")
]

encounters_data = [
    (1,1,"Mercy Hospital","Cardiology","2024-01-10"),
    (2,2,"City Medical Center","Neurology","2024-02-05"),
    (3,3,"Mercy Hospital","Orthopedics","2024-03-12"),
    (4,4,"North Regional","Cardiology","2024-04-20"),
    (5,5,"City Medical Center","Emergency","2024-05-18")
]

billing_data = [
    (1,1,1200),
    (2,2,800),
    (3,3,1500),
    (4,4,700),
    (5,5,500)
]

cursor.executemany("INSERT OR REPLACE INTO patients VALUES (?,?,?,?)",patients_data)
cursor.executemany("INSERT OR REPLACE INTO encounters VALUES (?,?,?,?,?)",encounters_data)
cursor.executemany("INSERT OR REPLACE INTO billing VALUES (?,?,?)",billing_data)

conn.commit()
conn.close()

print("Database created successfully.")