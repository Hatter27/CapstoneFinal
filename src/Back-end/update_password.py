import sqlite3
from werkzeug.security import generate_password_hash

conn = sqlite3.connect('medicine_inventory.db')
cursor = conn.cursor()

# Kuhanin lahat ng users na hindi pa naka-hash
cursor.execute("SELECT id, password FROM users")
users = cursor.fetchall()

for user in users:
    user_id, plain_password = user
    if not plain_password.startswith("pbkdf2:sha256"):  # Check kung plain text
        hashed_password = generate_password_hash(plain_password)  # Hash password
        cursor.execute("UPDATE users SET password = ? WHERE id = ?", (hashed_password, user_id))

conn.commit()
conn.close()

print("✅ Lahat ng passwords na-update na sa hashed version!")