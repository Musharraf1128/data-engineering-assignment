import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="internship_db",
    user="admin",
    password="admin123"
)

cur = conn.cursor()
cur.execute("SELECT version();")

print("Connected to PostgreSQL:")
print(cur.fetchone())

cur.close()
conn.close()
