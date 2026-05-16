import mysql.connector

conn = mysql.connector.connect(
    host="139.162.60.69",
    port=3306,
    user="user1",
    password="",
    database="expense_tracker"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM expenses;")

rows = cursor.fetchall()

for row in rows:
    print(row)

print()

cursor.execute("SELECT SUM(amount) FROM expenses")
result = cursor.fetchone()

print("Total expense for May 2026:", result[0])

conn.close()
