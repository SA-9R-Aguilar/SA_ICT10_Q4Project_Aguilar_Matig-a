from pyscript import document, display

#class which contains the object instances to display in the list
class Classmate:
    def __init__(self, name, section, student_type, favorite_subject):
        self.name = name
        self.section = section
        self.type = student_type
        self.favorite_subject = favorite_subject

students = [
    Classmate("Cinnamoroll", "Sanrio", "white puppy", "Cinnamon rolls"),
    Classmate("Arianne", "Ruby", "female student", "Chemistry"),
    Classmate("Caleb", "Ruby", "male student", "Social Studies"),
    Classmate("Jacob", "Ruby", "male student", "Cars"),
    Classmate("Ms. Onofre", "Emerald", "Teacher", "ICT")
]

#retrieves the values from the form in html for use in the class as an object
def classmate_creation(event):
    name = document.getElementById("name").value
    section = document.getElementById("section").value
    student_type = document.getElementById("type").value
    favorite_subject = document.getElementById("favSubject").value

    student = Classmate(name, section, student_type, favorite_subject)
    students.append(student)

    document.getElementById("output").innerText = f"{name} added!"

#displays the list
def introduce(event):
    document.getElementById("studentList").innerHTML = ' '

    output = ""

    for student in students:
        output += f"{student.name} is a {student.type} from {student.section} who loves {student.favorite_subject}.<br><br>"

    document.getElementById("studentList").innerHTML = output

    # for seatwork