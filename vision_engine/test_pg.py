from db_postgres import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT current_database();")
print("Connected to:", cur.fetchone())

cur.close()
conn.close()
