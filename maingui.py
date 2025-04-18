from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
from userdb import Accounts
from Studentsdb import Students

def midterm():

    #CREATE SETUP

    create1 = tkinter.Tk()
    create1.resizable(0,0)
    create1.geometry('+800+300')
    create1.title("Creation Page!")

    values = ["1","2","3","4","5","6","7","8","9","10",]

    midterm_label = tkinter.Label(create1, text="MIDTERM GRADES").grid(row=0,column=0)

    quiz_label = tkinter.Label(create1, text="How many quiz scores to input:").grid(row=1,column=0)
    quiz_combo = ttk.Combobox(create1,values=values,state='readonly')
    quiz_combo.grid(row=1,column=1)
    quiz_combo.set("Select a number")

    activity_label = tkinter.Label(create1,text="How many activity scores to input:").grid(row=2,column=0)
    activity_combo = ttk.Combobox(create1,values=values,state='readonly')
    activity_combo.grid(row=2,column=1)
    activity_combo.set("Select a number")

    project_label = tkinter.Label(create1,text="How many project scores to input:").grid(row=3,column=0)
    project_combo = ttk.Combobox(create1,values=values,state='readonly')
    project_combo.grid(row=3,column=1)
    project_combo.set("Select a number")

    #These are all placeholder for every data that the users inputting
    quiz_combobo = []
    activity_combobo = []
    project_combobo = []

    quiz_list = []
    quiz_max_list = []

    activity_list = []
    activity_max_list = []

    project_list = []
    project_max_list = []

    mid_exam = []

    global midterm_placeholder
    midterm_placeholder = []

    entries = []
    
    #Validatee the entries if its char or a number
    def validate_scores(entries):

        for entry in entries:
            value = entry.get().strip()
        if not value.isdigit():
            return False
        return True
    #Quiz Loop
    def quiz_combobox():
    
        for value in quiz_combobo:
            value.destroy()
        
        quiz_combobo.clear()
        quiz_list.clear()
        quiz_max_list.clear()

        try:
            
            quiz_loop_value = int(quiz_combo.get())

            for i in range(quiz_loop_value):
                quiz_label = tkinter.Label(create1, text=f"Quiz {i+1} Score:")
                quiz_label.grid(row=14+i, column=0)

                quiz_input = tkinter.Entry(create1)
                quiz_input.grid(row=14+i, column=1)

                quiz_max_label = tkinter.Label(create1, text=f"Enter Max Quiz Score for Quiz {i+1}: ")
                quiz_max_label.grid(row=14+i, column=2)

                quiz_max_input = tkinter.Entry(create1)
                quiz_max_input.grid(row=14+i, column=3)

                quiz_combobo.append(quiz_label)
                quiz_combobo.append(quiz_input)
                quiz_combobo.append(quiz_max_label)
                quiz_combobo.append(quiz_max_input)
                quiz_list.append(quiz_input)
                quiz_max_list.append(quiz_max_input)

        except ValueError:
            messagebox.showinfo('Error!', 'Please define a valid positive number for the quizzes.')

    #Activity Loop
    def activity_combobox():

        for value in activity_combobo:
            value.destroy()

        activity_combobo.clear()
        activity_list.clear()
        activity_max_list.clear()

        try:
            activity_loop_value = int(activity_combo.get())
            for i in range(activity_loop_value):
                activity_label = tkinter.Label(create1,text=f"Activity {i+1} Score:")
                activity_label.grid(row=14+i,column=4)

                activity_input = tkinter.Entry(create1)
                activity_input.grid(row=14+i,column=5)

                activity_max_label = tkinter.Label(create1, text=f"Enter max activity Score for activity {i+1}:")
                activity_max_label.grid(row=14+i,column=6)

                activity_max_input = tkinter.Entry(create1)
                activity_max_input.grid(row=14+i,column=7)

                activity_combobo.append(activity_label)
                activity_combobo.append(activity_input)
                activity_combobo.append(activity_max_label)
                activity_combobo.append(activity_max_input)
                activity_list.append(activity_input)
                activity_max_list.append(activity_max_input)


        except ValueError:
            messagebox.showinfo('Error!','Please define how many activity scores to input')
    #Project Loop
    def project_combobox():

        for value in project_combobo:
            value.destroy()

        project_combobo.clear()
        project_list.clear()
        project_max_list.clear()

        try:
            project_loop_value = int(project_combo.get())
            for i in range(project_loop_value):
                project_label = tkinter.Label(create1,text=f"Project {i+1} Score:")
                project_label.grid(row=14+i,column=8)

                project_input = tkinter.Entry(create1)
                project_input.grid(row=14+i,column=9)

                project_max_label = tkinter.Label(create1, text=f"Enter max project score for project {i+1}:")
                project_max_label.grid(row=14+i,column=10)

                project_max_input = tkinter.Entry(create1)
                project_max_input.grid(row=14+i,column=11)

                project_combobo.append(project_label)
                project_combobo.append(project_input)
                project_combobo.append(project_max_label)
                project_combobo.append(project_max_input)
                project_list.append(project_input)
                project_max_list.append(project_max_input)

            #To Stop the bug overstack
            if not mid_exam:

                exam_label = tkinter.Label(create1, text="Exam Score")
                exam_label.grid(row=30, column=0)

                exam_input = tkinter.Entry(create1)
                exam_input.grid(row=30, column=1)

                mid_exam.append(exam_input)

            conf_butt = tkinter.Button(create1, text="Confirm", command=confirm_quiz).grid(row=35,column=11,columnspan=3)

        except ValueError:
            messagebox.showinfo('Error!','Please define how many project scores to input')

    #My Calculator for data inputs and converter for Entry
    def computer():
        try:
       
            quiz_scores = [int(quiz_input.get()) for quiz_input in quiz_list]
            quiz_max_scores = [int(max_input.get()) for max_input in quiz_max_list]

            activity_scores = [int(activity_input.get()) for activity_input in activity_list]
            activity_max_scores = [int(max_input.get()) for max_input in activity_max_list]

            project_scores = [int(project_input.get()) for project_input in project_list]
            project_max_scores = [int(max_input.get()) for max_input in project_max_list]

            if len(mid_exam) > 0:
                exam_score = int(mid_exam[0].get())
            else:
                exam_score = 0

            exam_max_score = 50 

            
            quiz_total = sum(quiz_scores)
            quiz_max_total = sum(quiz_max_scores)
            activity_total = sum(activity_scores)
            activity_max_total = sum(activity_max_scores)
            project_total = sum(project_scores)
            project_max_total = sum(project_max_scores)

            
            quiz_percentage = (quiz_total / quiz_max_total) * 100 * 0.33
            activity_percentage = (activity_total / activity_max_total) * 100 * 0.33
            project_percentage = (project_total / project_max_total) * 100 * 0.34

           
            exampercentage = (exam_score / exam_max_score) * 100
            exam_calculated = exampercentage * 0.4

           
            class_performance = quiz_percentage + activity_percentage + project_percentage
            overall_classperf = class_performance * 0.6

           
            midterm_grade = overall_classperf + exam_calculated
            midterm_placeholder.append(midterm_grade)

            messagebox.showinfo("Success", f"Final Midterm Grade: {midterm_grade:.2f}%")
            create1.withdraw()
            finalterm()

        except ValueError:
            messagebox.showerror("Error", "Please ensure all scores are valid integers.")

    #Validatees if the combobox is not turned as a number
    def confirm_quiz():
    
            if quiz_combo.get() == "Select a number" or activity_combo.get() == "Select a number" or project_combo.get() == "Select a number":
                messagebox.showerror("Validation Error", "Please select a valid number for all categories (quiz, activity, project).")
                return

            all_entries = quiz_combobo + activity_combobo + project_combobo

            for data in all_entries:
                if isinstance(data, tkinter.Entry):
                    value = data.get().strip()
                    if value == "" or not value.isdigit():
                        messagebox.showerror("Validation Error", "All score fields must be filled with valid numeric values!")
                        return
                    
            computer()
    Start_Butt = tkinter.Button(create1,text="Start",command=lambda:[quiz_combobox(),activity_combobox(),project_combobox()] ).grid(row=35,column=0)

    back_butt = tkinter.Button(create1,text="Main Menu",command=lambda: [create1.destroy(), main_menu()]).grid(row=35,column=1)

def finalterm():
    create = tkinter.Tk()
    create.resizable(0, 0)
    create.title("Creation Page!")
    create.geometry('+800+300')

    values = ["1","2","3","4","5","6","7","8","9","10"]

    midterm_label = tkinter.Label(create, text="FINAL-TERM GRADES").grid(row=0,column=0)

    quiz_label = tkinter.Label(create, text="How many quiz scores to input:").grid(row=1,column=0)
    quiz_combo = ttk.Combobox(create,values=values,state='readonly')
    quiz_combo.grid(row=1,column=1)
    quiz_combo.set("Select a number")

    activity_label = tkinter.Label(create,text="How many activity scores to input:").grid(row=2,column=0)
    activity_combo = ttk.Combobox(create,values=values,state='readonly')
    activity_combo.grid(row=2,column=1)
    activity_combo.set("Select a number")

    project_label = tkinter.Label(create,text="How many project scores to input:").grid(row=3,column=0)
    project_combo = ttk.Combobox(create,values=values,state='readonly')
    project_combo.grid(row=3,column=1)
    project_combo.set("Select a number")

    #Same here as midterm these are all placeholder for datas
    fquiz_combobo = []
    factivity_combobo = []
    fproject_combobo = []

    fquiz_list = []
    fquiz_max_list = []

    factivity_list = []
    factivity_max_list = []

    fproject_list = []
    fproject_max_list = []

    final_exam = []
    global final_placeholder
    final_placeholder = []

    entries = []

    def validate_scores(entries):
        for entry in entries:
            value = entry.get().strip()
        if not value.isdigit():
            return False
        return True

    def quiz_combobox():
        for value in fquiz_combobo:
            value.destroy()

        fquiz_combobo.clear()
        fquiz_list.clear()
        fquiz_max_list.clear()

        try:
            quiz_loop_value = int(quiz_combo.get())
            for i in range(quiz_loop_value):
                fquiz_label = tkinter.Label(create,text=f"Quiz {i+1} Score:")
                fquiz_label.grid(row=14+i,column=0)

                fquiz_input = tkinter.Entry(create)
                fquiz_input.grid(row=14+i,column=1)

                fquiz_max_label = tkinter.Label(create,text=f"Enter Max Quiz Score for Quiz {i+1}: ")
                fquiz_max_label.grid(row=14+i,column=2)

                fquiz_max_input = tkinter.Entry(create)
                fquiz_max_input.grid(row=14+i,column=3)

                fquiz_combobo.append(quiz_label)
                fquiz_combobo.append(fquiz_input)
                fquiz_combobo.append(fquiz_max_label)
                fquiz_combobo.append(fquiz_max_input)
                fquiz_list.append(fquiz_input)
                fquiz_max_list.append(fquiz_max_input)

        except ValueError:
            messagebox.showinfo('Error!','Please define how many quiz scores to input')

    def activity_combobox():
        for value in factivity_combobo:
            value.destroy()

        factivity_combobo.clear()
        factivity_list.clear()
        factivity_max_list.clear()

        try:
            activity_loop_value = int(activity_combo.get())
            for i in range(activity_loop_value):
                factivity_label = tkinter.Label(create,text=f"Activity {i+1} Score:")
                factivity_label.grid(row=14+i,column=4)

                factivity_input = tkinter.Entry(create)
                factivity_input.grid(row=14+i,column=5)

                factivity_max_label = tkinter.Label(create, text=f"Enter max activity Score for activity {i+1}:")
                factivity_max_label.grid(row=14+i,column=6)

                factivity_max_input = tkinter.Entry(create)
                factivity_max_input.grid(row=14+i,column=7)

                factivity_combobo.append(factivity_label)
                factivity_combobo.append(factivity_input)
                factivity_combobo.append(factivity_max_label)
                factivity_combobo.append(factivity_max_input)
                factivity_list.append(factivity_input)
                factivity_max_list.append(factivity_max_input)

        except ValueError:
            messagebox.showinfo('Error!','Please define how many activity scores to input')

    def project_combobox():
        for value in fproject_combobo:
            value.destroy()

        fproject_combobo.clear()
        fproject_list.clear()
        fproject_max_list.clear()

        try:
            project_loop_value = int(project_combo.get())
            for i in range(project_loop_value):
                fproject_label = tkinter.Label(create,text=f"Project {i+1} Score:")
                fproject_label.grid(row=14+i,column=8)

                fproject_input = tkinter.Entry(create)
                fproject_input.grid(row=14+i,column=9)

                fproject_max_label = tkinter.Label(create, text=f"Enter max project score for project {i+1}:")
                fproject_max_label.grid(row=14+i,column=10)

                fproject_max_input = tkinter.Entry(create)
                fproject_max_input.grid(row=14+i,column=11)

                fproject_combobo.append(fproject_label)
                fproject_combobo.append(fproject_input)
                fproject_combobo.append(fproject_max_label)
                fproject_combobo.append(fproject_max_input)
                fproject_list.append(fproject_input)
                fproject_max_list.append(fproject_max_input)
                #For Overstacking

            if not final_exam:
                exam_label = tkinter.Label(create, text="Exam Score")
                exam_label.grid(row=30, column=0)

                exam_input = tkinter.Entry(create)
                exam_input.grid(row=30, column=1)

                final_exam.append(exam_input)

            conf_butt = tkinter.Button(create, text="Confirm", command=confirm_quiz).grid(row=35,column=11,columnspan=3)

        except ValueError:
            messagebox.showinfo('Error!','Please define how many project scores to input')

    def computer():
        try:

            quiz_scores = [int(quiz_input.get()) for quiz_input in fquiz_list]
            quiz_max_scores = [int(max_input.get()) for max_input in fquiz_max_list]

            activity_scores = [int(activity_input.get()) for activity_input in factivity_list]
            activity_max_scores = [int(max_input.get()) for max_input in factivity_max_list]

            project_scores = [int(project_input.get()) for project_input in fproject_list]
            project_max_scores = [int(max_input.get()) for max_input in fproject_max_list]

            exam_score = [int(exam_input.get()) for exam_input in final_exam]
            exam_max_score = 50

            if len(final_exam) > 0:
                exam_score = int(final_exam[0].get())
            else:
                exam_score = 0
       
            quiz_total = sum(quiz_scores)
            quiz_max_total = sum(quiz_max_scores)
            activity_total = sum(activity_scores)
            activity_max_total = sum(activity_max_scores)
            project_total = sum(project_scores)
            project_max_total = sum(project_max_scores)

            quiz_percentage = (quiz_total / quiz_max_total) * 100 * 0.33
            activity_percentage = (activity_total / activity_max_total) * 100 * 0.33
            project_percentage = (project_total / project_max_total) * 100 * 0.34

            exampercentage = (exam_score / exam_max_score) * 100
            exam_calculated = exampercentage * 0.4

            class_performance = quiz_percentage + activity_percentage + project_percentage 
            overall_classperf = class_performance * 0.6

            final_term_grade = overall_classperf + exam_calculated
            final_placeholder.append(final_term_grade)

            messagebox.showinfo("Success", f"Final-Term Grade: {final_term_grade:.2f}%")
            create.withdraw()
            stud_info(final_term_grade)

        except ValueError:
            messagebox.showinfo("Error!", "Please ensure all scores are valid integers.")

    def confirm_quiz():
        if quiz_combo.get() == "Select a number" or activity_combo.get() == "Select a number" or project_combo.get() == "Select a number":
            messagebox.showerror("Validation Error", "Please select a valid number for all categories (quiz, activity, project).")
            return

        all_entries = fquiz_combobo + factivity_combobo + fproject_combobo

        for data in all_entries:
            if isinstance(data, tkinter.Entry):
                value = data.get().strip()
                if value == "" or not value.isdigit():
                    messagebox.showerror("Validation Error", "All score fields must be filled with valid numeric values!")
                    return

        computer()
    Start_Butt = tkinter.Button(create,text="Start",command=lambda:[quiz_combobox(),activity_combobox(),project_combobox()] ).grid(row=35,column=0)

    back_butt = tkinter.Button(create,text="Main Menu",command=lambda: [create.destroy(), main_menu()]).grid(row=35,column=1)
#Computes the 2 overall grade to pass the grade to the world computation
def computation(midterm_placeholder, final_placeholder):
    try:
        midterm_grade = midterm_placeholder
        final_grade = final_placeholder
        grade = overall_computation(midterm_grade, final_grade)
        stud_info(grade)

    except Exception as e:
        messagebox.showerror("Error", f"Computation Error: {str(e)}")

#World computation to have the general grade from midterm and final
def overall_computation(avemid, avefinal):
    return (avemid + avefinal) / 2

#passes the datas to studentsdb module 
def passing_process(grade,lname, fname, yrlvl, section, prog, subj):

    try:
        recei = Students()
        recei.students_info(grade, lname, fname, yrlvl, section, prog, subj)
        messagebox.showinfo("Success", "Student information saved successfully!")
        main_menu() 
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


#gather students information and passes to passing_process 
def stud_info(grade):

    stud = tkinter.Tk()
    stud.resizable(0, 0)
    stud.title("Student Information")
    stud.geometry('300x200+800+300')

    lname = tkinter.Label(stud, text="Last Name")
    lname.grid(row=0, column=0)

    lname_input = tkinter.Entry(stud)
    lname_input.grid(row=0, column=1)

    fname = tkinter.Label(stud, text="First Name")
    fname.grid(row=1, column=0)

    fname_input = tkinter.Entry(stud)
    fname_input.grid(row=1, column=1)

    yrlvl = tkinter.Label(stud, text="Year Level")
    yrlvl.grid(row=2, column=0)

    yrlvl_input = tkinter.Entry(stud)
    yrlvl_input.grid(row=2, column=1)

    section = tkinter.Label(stud, text="Section")
    section.grid(row=3, column=0)

    section_input = tkinter.Entry(stud)
    section_input.grid(row=3, column=1)

    prog = tkinter.Label(stud, text="Program")
    prog.grid(row=4, column=0)

    prog_input = tkinter.Entry(stud)
    prog_input.grid(row=4, column=1)

    subj = tkinter.Label(stud, text="Subject")
    subj.grid(row=5, column=0)

    subj_input = tkinter.Entry(stud)
    subj_input.grid(row=5, column=1)

    conf_butt = tkinter.Button(
        stud,
        text="Confirm",
        command=lambda: [
            passing_process(grade, lname_input.get(), fname_input.get(), yrlvl_input.get(), section_input.get(), prog_input.get(), subj_input.get()),
            stud.destroy()
        ]
    )
    conf_butt.grid(row=6, column=1, columnspan=2)


def review():

    #Review SETUP
    students = Students()
    rev = tkinter.Tk()
    rev.resizable(0,0)
    rev.geometry('+800+300')
    rev.title("Review Page")

    prog = tkinter.Label(rev, text="Enter the student's program you want to check [Ex. BSCS, ACT, BSA,..]")
    prog.grid(row=0,column=0)

    prog_ent = tkinter.Entry(rev)
    prog_ent.grid(row=0,column=1)


    listbox = tkinter.Listbox(rev, width=100, height=15)
    listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    #this is a method to show the desired data from database
    def prog_setup():
        results = Students()
        program = prog_ent.get().strip()

        if not program:
            messagebox.showwarning("Input Error", "Please enter a program name.")
            return
        
        results = students.read(program)

        if results:
            listbox.delete(0,tkinter.END)

            for row in results:
                student_info = f"Students_ID: {row[0]}, Subject: {row[1]}, Name: {row[2]}, Section: {row[3]}, Year Level: {row[4]}, Grade: {row[5]}"
                listbox.insert(tkinter.END, student_info)

    review_button = tkinter.Button(rev, text="Review Data", command=prog_setup)
    review_button.grid(row=2, column=0, columnspan=2)

    back_button = tkinter.Button(rev, text="Back",command=lambda:[rev.withdraw(),main_menu()])
    back_button.grid(row=2,column=1,columnspan=2)

def update():
    # Update Setup
    upd = tkinter.Tk()
    upd.resizable(0, 0)
    upd.geometry('+800+300')
    upd.title("Update Page")

    stud_combobo = []

    values = ["Student's Name", "Student's Year Level", "Student's Section", "Student's Subject"]

    stud_label = tkinter.Label(upd, text="Select student's information to update")
    stud_label.grid(row=0, column=0)

    stud_combo = ttk.Combobox(upd, values=values, state="readonly")
    stud_combo.grid(row=0, column=1)
    stud_combo.set("Select here")

    def stud_combobox():
        # Clear previous widgets
        for widget in stud_combobo:
            widget.destroy()
        stud_combobo.clear()

        selected_value = stud_combo.get()

        if selected_value == "Student's Name":
       
            stud_prog = tkinter.Label(upd, text="Enter the student's program")
            stud_prog.grid(row=2, column=0)

            stud_prog_input = tkinter.Entry(upd)
            stud_prog_input.grid(row=2, column=1)
            stud_combobo.append(stud_prog)
            stud_combobo.append(stud_prog_input)

            stud_name = tkinter.Label(upd, text="Enter student's name Ex: (Firstname Lastname)")
            stud_name.grid(row=3, column=0)

            stud_name_input = tkinter.Entry(upd)
            stud_name_input.grid(row=3, column=1)
            stud_combobo.append(stud_name)
            stud_combobo.append(stud_name_input)

            stud_newname = tkinter.Label(upd, text="Enter New Name")
            stud_newname.grid(row=4, column=0)

            stud_newname_input = tkinter.Entry(upd)
            stud_newname_input.grid(row=4, column=1)
            stud_combobo.append(stud_newname)
            stud_combobo.append(stud_newname_input)

            def update_process(stud_prog, stud_name, stud_newname):
                try:
                    edit = Students()
                    edit.updatename(stud_prog, stud_name, stud_newname)
                    messagebox.showinfo("Success", "Student information updated successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

            submit_button = tkinter.Button(upd, text="Submit", command=lambda: [update_process(stud_prog_input.get(), stud_name_input.get(), stud_newname_input.get())])
            submit_button.grid(row=5, column=1)
            stud_combobo.append(submit_button)

        elif selected_value == "Student's Year Level":
  
            stud_prog = tkinter.Label(upd,text="Enter the student's program")
            stud_prog.grid(row=2,column=0)

            stud_prog_input = tkinter.Entry(upd)
            stud_prog_input.grid(row=2, column=1)
            stud_combobo.append(stud_prog)
            stud_combobo.append(stud_prog_input)

            stud_name = tkinter.Label(upd, text="Enter student's name Ex: (Firstname Lastname)")
            stud_name.grid(row=3, column=0)

            stud_name_input = tkinter.Entry(upd)
            stud_name_input.grid(row=3, column=1)
            stud_combobo.append(stud_name)
            stud_combobo.append(stud_name_input)


            stud_yrlvl = tkinter.Label(upd,text="Enter student's new year level")
            stud_yrlvl.grid(row=4,column=0)

            stud_yrlvl_input = tkinter.Entry(upd)
            stud_yrlvl_input.grid(row=4, column=1)
            stud_combobo.append(stud_name)
            stud_combobo.append(stud_yrlvl_input)

            def update_process(stud_prog, stud_name,stud_yrlvl):
                try:
                    edit = Students()
                    edit.updateyearlvl(stud_prog, stud_name,stud_yrlvl)
                    messagebox.showinfo("Success", "Year level updated successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

            submit_button = tkinter.Button(upd, text="Submit", command=lambda: [update_process(stud_prog_input.get(),stud_name_input.get(),stud_yrlvl_input.get())])
            submit_button.grid(row=5, column=1)
            stud_combobo.append(submit_button)

        elif selected_value == "Student's Section":
            stud_prog = tkinter.Label(upd,text="Enter the student's program")
            stud_prog.grid(row=2,column=0)

            stud_prog_input = tkinter.Entry(upd)
            stud_prog_input.grid(row=2, column=1)
            stud_combobo.append(stud_prog)
            stud_combobo.append(stud_prog_input)

            stud_name = tkinter.Label(upd, text="Enter student's name Ex: (Firstname Lastname)")
            stud_name.grid(row=3, column=0)

            stud_name_input = tkinter.Entry(upd)
            stud_name_input.grid(row=3, column=1)
            stud_combobo.append(stud_name)
            stud_combobo.append(stud_name_input)

            stud_newsection = tkinter.Label(upd,text="Enter new section")
            stud_newsection.grid(row=4,column=0)

            stud_newsection_input = tkinter.Entry(upd)
            stud_newsection_input.grid(row=4,column=1)
            stud_combobo.append(stud_newsection)
            stud_combobo.append(stud_newsection_input)

            def update_process(stud_prog,stud_name,stud_newsection):
                try:
                    edit = Students()
                    edit.updatesection(stud_prog,stud_name,stud_newsection)
                    messagebox.showinfo("Success", "Section updated successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

            submit_button = tkinter.Button(upd, text="Submit", command=lambda: [update_process(stud_prog_input.get(),stud_name_input.get(),stud_newsection_input.get())])
            submit_button.grid(row=5, column=1)
            stud_combobo.append(submit_button)

        elif selected_value == "Student's Subject":
       
            stud_prog = tkinter.Label(upd, text="Enter the student's program")
            stud_prog.grid(row=2, column=0)

            stud_prog_input = tkinter.Entry(upd)
            stud_prog_input.grid(row=2, column=1)
            stud_combobo.append(stud_prog)
            stud_combobo.append(stud_prog_input)

            stud_sub = tkinter.Label(upd, text="Enter new subject:")
            stud_sub.grid(row=3, column=0)

            stud_sub_input = tkinter.Entry(upd)
            stud_sub_input.grid(row=3, column=1)
            stud_combobo.append(stud_sub)
            stud_combobo.append(stud_sub_input)

            stud_name = tkinter.Label(upd, text="Enter student's name Ex: (Firstname Lastname)")
            stud_name.grid(row=4, column=0)

            stud_name_input = tkinter.Entry(upd)
            stud_name_input.grid(row=4, column=1)
            stud_combobo.append(stud_name)
            stud_combobo.append(stud_name_input)

            def update_process(stud_prog, stud_sub, stud_name):
                try:
                    edit = Students()
                    edit.updatesubject(stud_prog, stud_sub, stud_name)
                    messagebox.showinfo("Success", "Student subject updated successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

            submit_button = tkinter.Button(upd, text="Submit", command=lambda: [update_process(stud_prog_input.get(), stud_sub_input.get(), stud_name_input.get())])
            submit_button.grid(row=5, column=1)
            stud_combobo.append(submit_button)

        else:
            messagebox.showerror("Error", "Please select a valid option from the combobox!")

   
    start_butt = tkinter.Button(upd, text="Start", command=stud_combobox)
    start_butt.grid(row=6, column=0)


    back_butt = tkinter.Button(upd, text="Main Menu", command=lambda: [upd.withdraw(), main_menu()])
    back_butt.grid(row=6, column=1)

def erase():
    # Delete Setup
    delete_window = tkinter.Tk()
    delete_window.resizable(0, 0)
    delete_window.geometry('+800+300')
    delete_window.title("Delete Page")

    
    del_stud_label = tkinter.Label(delete_window, text="Enter the student's program: [Ex. BSCS, ACT, BSA]")
    del_stud_label.grid(row=0, column=0)

    del_stud_input = tkinter.Entry(delete_window)
    del_stud_input.grid(row=0, column=1)

    
    stud_name_label = tkinter.Label(delete_window, text="Enter student's name to delete record")
    stud_name_label.grid(row=1, column=0)

    stud_name_input = tkinter.Entry(delete_window)
    stud_name_input.grid(row=1, column=1)

    
    def validate_entries():
        try:
            deli = Students()
            deli.delete

            program = del_stud_input.get().strip().upper()  
            name = stud_name_input.get().strip().capitalize()  

            if not program:
                raise ValueError("Program field cannot be blank or whitespace.")
            if not name:
                raise ValueError("Student name field cannot be blank or whitespace.")
            deli.delete(program, name)
            main_menu()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    
    delete_button = tkinter.Button(delete_window, text="Delete", command=validate_entries)
    delete_button.grid(row=2, column=1)

    back_button = tkinter.Button(delete_window,text="Back",command=lambda: [delete_window.withdraw(),main_menu()])
    back_button.grid(row=2,column=0)



def main_menu():
    menu = tkinter.Tk()
    menu.resizable(0,0)
    menu.geometry('+800+300')
    menu.title("Main Menu")

    option1 = tkinter.Label(menu, text="Create Student's Data").grid(row=0,column=0)
    option1 = tkinter.Button(menu, text="Create",command=lambda: [menu.destroy(), midterm()]).grid(row=0,column=3,padx=50,ipadx=4)
    
    option2 = tkinter.Label(menu, text="Review Student's Data").grid(row=1,column=0)
    option2 = tkinter.Button(menu, text="Review",command=lambda: [menu.destroy(), review()]).grid(row=1,column=3,padx=50,ipadx=3)

    option3 = tkinter.Label(menu, text="Update Student's Data").grid(row=2,column=0)
    option3 = tkinter.Button(menu, text="Update",command=lambda: [menu.destroy(), update()]).grid(row=2,column=3,padx=50,ipadx=3)

    option4 = tkinter.Label(menu, text="Delete Student's Data").grid(row=3,column=0)
    option4 = tkinter.Button(menu, text="Delete",command=lambda: [menu.destroy(), erase()]).grid(row=3,column=3,padx=50,ipadx=6)

#My Register Method

def register():
    
    register = tkinter.Tk()
    register.resizable(0,0)
    register.geometry('+800+300')
    register.title("Registration Page")

    user_reg = tkinter.Label(register, text="Enter Username").grid(row=0,column=0)
    user_text = tkinter.Entry(register)
    user_text.grid(row=0,column=1)

    pass_reg = tkinter.Label(register, text="Enter Password").grid(row=1,column=0)
    pass_text = tkinter.Entry(register)
    pass_text.grid(row=1,column=1)

    #My Register Setup
    def register_setup():
        try:
            user = user_text.get()
            passw = pass_text.get()

            if not user.strip():
                raise ValueError("Please enter your username")
            if not passw.strip():
                raise ValueError("Please enter your password")
            if Accounts.register_user(user,passw):
                messagebox.showinfo("Success", "Registration successful!")
                startup()


        except ValueError as e:
            messagebox.showerror("Error", str(e))

    confirm_butt = tkinter.Button(register,text="Confirm",command=register_setup).grid(row=3,column=1)
    return_butt = tkinter.Button(register,text="Back",command=lambda: [register.destroy(), startup()] ).grid(row=3,column=0,ipadx=10)

    
#My Startup
def startup():

    root = tkinter.Tk()

    root.title("Grade Management")
    root.geometry('+800+300')
    root.resizable(0,0)

    intro = tkinter.Label(root, text="Welcome to Grade Management System").grid(row=0,column=1, sticky="nsew")

    user_label = tkinter.Label(root, text="Username").grid(row=1, column=0)
    login_text = tkinter.Entry(root)
    login_text.grid(row=1,column=1)
    
    pass_label = tkinter.Label(root,text="Password").grid(row=2, column=0)
    pass_text = tkinter.Entry(root,show="*")
    pass_text.grid(row=2,column=1)
    
    
    #My login setup
    def login_setup():
        username = login_text.get()
        password = pass_text.get()

        if not username or not password:
            messagebox.showinfo("Error", "Please fill in all fields.")
            return

        if Accounts.login_user(username, password):
            root.destroy()
            main_menu()  
        else:
            messagebox.showinfo("Error", "User not found!.")
            
    login_butt = tkinter.Button(root, text="Login",command=login_setup).grid(row=1,column=3,ipadx=6)
    reg_butt = tkinter.Button(root,text="Register",command=lambda: [root.destroy(), register()]).grid(row=2,column=3)

    root.mainloop()

startup()

