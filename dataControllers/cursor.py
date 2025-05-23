"""
This file will be used to control the cursor of the sql database.
"""
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database Credentials (Use environment variables)
DB_NAME = os.getenv("DB_NAME", "ERPDB")
USER = os.getenv("DB_USER", "root")
PASSWORD = os.getenv("DB_PASSWORD", "root")
HOST = os.getenv("DB_HOST", "localhost")
PORT = os.getenv("DB_PORT", "3306")

cursor = None
connection = None

connection = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    port=PORT,
    database=DB_NAME
)

connection.autocommit = True

cursor = connection.cursor(dictionary=True)