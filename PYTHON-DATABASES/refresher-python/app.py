import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import the ttk module for Combobox
from dbhelpers import *

class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management App")
        self.root.geometry("600x600")  # Set the geometry size to 600x600
        self.root.config(bg="lightblue")  # Set background color to light blue

        self.initialize_gui()

    def initialize_gui(self):
        # Create a frame with light blue background to contain all widgets
        self.frame = tk.Frame(self.root, bg="lightblue")
        self.frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)  # Add padding around the frame

        self.id_label = tk.Label(self.frame, text="ID Number", bg="lightblue")
        self.id_label.pack(pady=5)

        self.id_entry = tk.Entry(self.frame, width=40)
        self.id_entry.pack(pady=5)

        self.lastname_label = tk.Label(self.frame, text="Last Name", bg="lightblue")
        self.lastname_label.pack(pady=5)

        self.lastname_entry = tk.Entry(self.frame, width=40)
        self.lastname_entry.pack(pady=5)

        self.firstname_label = tk.Label(self.frame, text="First Name", bg="lightblue")
        self.firstname_label.pack(pady=5)

        self.firstname_entry = tk.Entry(self.frame, width=40)
        self.firstname_entry.pack(pady=5)

        self.course_label = tk.Label(self.frame, text="Course", bg="lightblue")
        self.course_label.pack(pady=5)

        # List of courses for the dropdown menu
        self.courses = ['BSIT', 'BSIS', 'BSCS', 'BSCPE', 'BSBA']
        
        # Create a Combobox for the course selection
        self.course_combobox = ttk.Combobox(self.frame, values=self.courses, width=37)
        self.course_combobox.pack(pady=5)

        self.level_label = tk.Label(self.frame, text="Level", bg="lightblue")
        self.level_label.pack(pady=5)

        self.level_entry = tk.Entry(self.frame, width=40)
        self.level_entry.pack(pady=5)

        # Adjust the button widths and heights
        button_config = {'width': 25, 'height': 2}

        self.add_button = tk.Button(self.frame, text="Add Student", command=self.add_student, **button_config)
        self.add_button.pack(pady=5)

        self.update_button = tk.Button(self.frame, text="Update Student", command=self.update_student, **button_config)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Student", command=self.delete_student, **button_config)
        self.delete_button.pack(pady=5)

        self.find_button = tk.Button(self.frame, text="Find Student", command=self.find_student, **button_config)
        self.find_button.pack(pady=5)

        self.display_button = tk.Button(self.frame, text="Display Students", command=self.display_students, **button_config)
        self.display_button.pack(pady=5)

        self.clear_button = tk.Button(self.frame, text="Clear Fields", command=self.clear_fields, **button_config)
        self.clear_button.pack(pady=5)

    def clear_fields(self):
        self.id_entry.delete(0, tk.END)
        self.lastname_entry.delete(0, tk.END)
        self.firstname_entry.delete(0, tk.END)
        self.course_combobox.set('')  # Clear the selection in Combobox
        self.level_entry.delete(0, tk.END)

    def add_student(self):
        idno = self.id_entry.get()
        lastname = self.lastname_entry.get()
        firstname = self.firstname_entry.get()
        course = self.course_combobox.get()  # Get the selected course from Combobox
        level = self.level_entry.get()

        if idno and lastname and firstname and course and level:
            success = addrecord('student', idno=idno, lastname=lastname, firstname=firstname, course=course, level=level)
            if success:
                messagebox.showinfo("Success", "Student added successfully!")
                self.clear_fields()
            else:
                messagebox.showerror("Error", "Failed to add student.")
        else:
            messagebox.showerror("Error", "Please fill in all student information fields.")

    def update_student(self):
        idno = self.id_entry.get()
        lastname = self.lastname_entry.get()
        firstname = self.firstname_entry.get()
        course = self.course_combobox.get()  # Get the selected course from Combobox
        level = self.level_entry.get()

        if idno:
            success = updaterecord('student', idno=idno, lastname=lastname, firstname=firstname, course=course, level=level)
            if success:
                messagebox.showinfo("Success", "Student updated successfully!")
                self.clear_fields()
            else:
                messagebox.showerror("Error", "Failed to update student.")
        else:
            messagebox.showerror("Error", "Please provide the ID Number of the student to update.")

    def delete_student(self):
        idno = self.id_entry.get()
        if idno:
            success = deleterecord("student", idno=idno)
            if success:
                messagebox.showinfo("Success", "Student deleted successfully!")
                self.clear_fields()
            else:
                messagebox.showerror("Error", "Failed to delete student.")
        else:
            messagebox.showerror("Error", "Please provide the ID Number of the student to delete.")

    def find_student(self):
        idno = self.id_entry.get()
        if idno:
            data = getrecord("student", idno=idno)
            if data:
                student_info = f"ID Number: {data[0]['idno']}\nLast Name: {data[0]['lastname']}\nFirst Name: {data[0]['firstname']}\nCourse: {data[0]['course']}\nLevel: {data[0]['level']}"
                messagebox.showinfo("Student Information", student_info)
                self.clear_fields()
            else:
                messagebox.showerror("Error", "Student not found.")
        else:
            messagebox.showerror("Error", "Please provide the ID Number of the student to find.")

    def display_students(self):
        data = getall("student")
        if data:
            students_info = "\n".join([f"ID Number: {item['idno']}, Last Name: {item['lastname']}, First Name: {item['firstname']}, Course: {item['course']}, Level: {item['level']}" for item in data])
            messagebox.showinfo("Students Information", students_info)
        else:
            messagebox.showerror("Error", "No students found in the database.")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()
