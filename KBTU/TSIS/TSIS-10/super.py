import psycopg2

DB_NAME = "pp2"
DB_USER = "postgres"
DB_PASS = "Bako-2060"
DB_HOST = "localhost"
DB_PORT = "5432"

# Connect to your postgres DB
try:
    con = psycopg2.connect(
            database = DB_NAME, user = DB_USER,
            password = DB_PASS, host = DB_HOST, port = DB_PORT)
    print("Database connected successfully")
    
except:
    print("Database not connected")