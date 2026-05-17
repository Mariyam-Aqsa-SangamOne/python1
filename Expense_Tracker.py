import os
import mysql.connector

db_password = os.getenv("DB_PASSWORD")

conn = mysql.connector.connect(
    host="139.162.60.69",
    port=3306,
    user="user1",
    password=db_password,
    database="expense_tracker"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM expenses")
rows = cursor.fetchall()

print("Expense Table Records:")
for row in rows:
    print(row)

cursor.execute("SELECT SUM(amount) FROM expenses")
result = cursor.fetchone()

print("Total expense for May 2026:", result[0])

conn.close()
