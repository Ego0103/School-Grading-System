import mysql.connector
import bcrypt
from tkinter import messagebox


class Accounts:
    #Connection to database
    @staticmethod
    def create_db_connection():
        return mysql.connector.connect(
            host="localhost",
            user="root",    
            password="",    
            database="Accounts"
        )
    #Creation of database if not exists
    @staticmethod
    def data():
        conn = Accounts.create_db_connection()  
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS Accounts")

        cursor.execute("USE Accounts")
       
        query = """CREATE TABLE IF NOT EXISTS users (username VARCHAR(255) UNIQUE,password VARCHAR(255), KEY (username))"""
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()

    #Registration Setup
    @staticmethod
    def register_user(usern_input,pw_input):
        username = usern_input
        password = pw_input

        conn = Accounts.create_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            messagebox.showinfo("Error","Username already exists!")
            cursor.close()
            conn.close() 

        #Its the bcrypt that encrypt the password for security 
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
        messagebox.showinfo("Success","Registration Success!")
        conn.commit()

        cursor.close()
        conn.close()
        return  
    #Login user
    @staticmethod
    def login_user(usern_input,passw_input):
        username = usern_input
        password = passw_input
        #Connection to database
        conn = Accounts.create_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if not user:
            cursor.close()
            conn.close()
            return False  

        hashed_password = user[1]
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            cursor.close()
            conn.close()
            return True
        else:
            cursor.close()
            conn.close()

Accounts.data()
