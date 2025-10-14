from db import engine

try:
    connection = engine.connect()
    print("✅ Successfully connected to PostgreSQL database!")
    connection.close()
except Exception as e:
    print("❌ Connection failed:", e)
