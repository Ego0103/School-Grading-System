from tkinter import messagebox
import mysql.connector
#Connection to database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="students_grade"
)
cursor = mydb.cursor()

class Students:

    grade_convertion = {
    100: 1, 79: 2.75,
    99: 1, 78: 2.75,
    98: 1, 77: 3,
    97: 1, 76: 3,
    96: 1, 75: 3,
    95: 1.25, 74: 5,
    94: 1.25, 73: 5,
    93: 1.5, 72: 5,
    92: 1.5, 71: 5,
    91: 1.5, 70: 5,
    90: 1.75, 69: 5,
    89: 1.75, 68: 5,
    88: 1.75, 67: 5,
    87: 2, 66: 5,
    86: 2, 65: 5,
    85: 2, 64: 5,
    84: 2.25, 63: 5,
    83: 2.25, 62: 5,
    82: 2.50, 61: 5, 
    81: 2.50, 60: 5,
    80: 2.50, 59: 5,

    }
    #Setup variables
    def __init__(self):
        self.stud_name = ""
        self.yearlvl = ""
        self.section = ""
        self.program = ""
        self.subject = ""
    #Create Startup
    def students_info(self, grade, lname_input, fname_input, yrlvl_input, section_input, prog_input, subj_input):
        create_db = "CREATE DATABASE IF NOT EXISTS students_grade"
        cursor.execute(create_db)

        use_db = "USE students_grade"
        cursor.execute(use_db)

        lastname = lname_input.capitalize()
        firstname = fname_input.capitalize()
        self.yearlvl = yrlvl_input.capitalize()
        self.section = section_input.upper()
        self.program = prog_input.upper()
        self.subject = subj_input.upper()
        self.stud_name = f"{lastname} {firstname}"

        create_table = f"""CREATE TABLE IF NOT EXISTS {self.program} (Students_ID INT NOT NULL AUTO_INCREMENT,Subject VARCHAR(255),Name VARCHAR(255),Section VARCHAR(255),Year_Level VARCHAR(255),Grade DECIMAL(5,2),PRIMARY KEY (Students_ID))"""
        cursor.execute(create_table)
        mydb.commit()

        gpa = self.convert_to_gpa(grade)

        insert_query = f"INSERT INTO {self.program} (Subject, Name, Section, Year_Level, Grade) VALUES (%s, %s, %s, %s, %s)"
        data = (self.subject, self.stud_name, self.section, self.yearlvl, gpa)
        cursor.execute(insert_query, data)
        mydb.commit()
        student_id = cursor.lastrowid
        
        return student_id
    #From grade to gpa convertion uses grade_convertion dictionary
    def convert_to_gpa(self, grade):
        for grade_placeholder, gpa in sorted(Students.grade_convertion.items(), reverse=True):
            if grade >= grade_placeholder:
                return gpa
        return 5.00
    
    #The Review Setup
    def read(self, program):
        try:
            
            query = f"SELECT * FROM {program}"
            cursor.execute(query)
            results = cursor.fetchall()

            if not results:
                messagebox.showinfo("No Data", "No data found for this program.")
                return None
            
            return results

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            return None
        
    #Update the Year Level 
    @staticmethod
    def updateyearlvl(stud_prog, stud_name,stud_yrlvl):
     
        program = stud_prog.upper()
        name = stud_name.capitalize()
        new_yearlvl = stud_yrlvl.capitalize()
        update_query = f"UPDATE {program} SET Year_Level = %s WHERE Name = %s"
        cursor.execute(update_query, (new_yearlvl, name))
        mydb.commit()

    #Update The section
    @staticmethod
    def updatesection(stud_prog,stud_name,stud_newsection):
     
        program = stud_prog.upper()
        name = stud_name.capitalize()
        new_section = stud_newsection.upper()
        update_query = f"UPDATE {program} SET Section = %s WHERE Name = %s"
        cursor.execute(update_query, (new_section, name))
        mydb.commit()

    #update fullname
    @staticmethod
    def updatename(stud_prog,stud_name,stud_newname):
     
        program = stud_prog.upper()
        old_name = stud_name.capitalize()
        new_name = stud_newname.capitalize()
        update_query = f"UPDATE {program} SET Name = %s WHERE Name = %s"
        cursor.execute(update_query, (new_name, old_name))
        mydb.commit()
    #update subject
    @staticmethod
    def updatesubject(stud_prog,stud_sub,stud_name):
        try:
            program = stud_prog.upper()
            name = stud_name.capitalize()
            new_subject = stud_sub.upper()
            update_query = f"UPDATE {program} SET Subject = %s WHERE Name = %s"
            cursor.execute(update_query, (new_subject, name))
            mydb.commit()

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")

    @staticmethod
    #The Delete Setup
    def delete(del_stud_input,stud_name_input):
     
        try:    #Checks if the input of the user is valid
            if not del_stud_input.isidentifier():
                raise ValueError(f"Invalid program name: {del_stud_input}. It must only contain letters, numbers, or underscores.")

            delete_query = f"DELETE FROM {del_stud_input} WHERE Name = %s"
            cursor.execute(delete_query, (stud_name_input,))
            mydb.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Success", f"Record for {stud_name_input} in {del_stud_input} deleted successfully.")
            else:
                messagebox.showwarning("Not Found", f"No record found for {stud_name_input} in {del_stud_input}.")

        except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")
