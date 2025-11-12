# University Management System based on OOP


import streamlit as st


# Base class : student , teacher
class person:
    def __init__(self, branch: str, name: str) -> None:
        self.branch = branch
        self.name = name


    # help to display the object in better formatting
    def __str__(self) -> str:
        return f"Name: {self.name} | Branch: {self.branch}"
   
# Child1 class: student
class student(person):
    def __init__(self, rollno, name, branch):
        super().__init__(branch, name)
        self.rollno = rollno


    def __str__(self) -> str:
        return f"{super().__str__()} | Rollno : {self.rollno}"
   
# Child2 class: teacher
class teacher(person):
    def __init__(self, subject, name, branch):
        super().__init__(branch, name)
        self.subject = subject


    def __str__(self) -> str:
        return f"{super().__str__()} | Subject : {self.subject}"


class college:
    def __init__(self, cname: str):
        self.cname = cname
        self.students = []
        self.teachers = []


    def add_student(self, s: student):
        self.students.append(s)


    def add_teacher(self, t: teacher):
        self.teachers.append(t)


# This function is used to find a college out of list of colleges.
# if we don't find that particular college then return None.
def find_college(cname):
    return next((c for c in st.session_state.colleges if c.cname == cname), None)





# Front-end development
st.set_page_config(page_title="University Management System", layout = "wide")


st.title("Unversity Management")


if "colleges" not in st.session_state:
    st.session_state.colleges = []


menu_choice = st.sidebar.radio(
    "Select Action",
    (
        "Create New College",
        "Add New Student",
        "Add New Teacher",
        "Display students",
        "Display teachers",
        "Display colleges"
    )
)


# create new college
if menu_choice == "Create New College":
    cname = st.text_input("Enter the New college Name")
    if st.button("SUBMIT"):
        if not cname:
            st.error("Please insert some college name: that is empty")
        elif find_college(cname):
            st.warning("College already Exist")
        else:
            st.session_state.colleges.append(college(cname))
            st.success("Successfully created college")
           


elif menu_choice == "Add New Student":
    if not st.session_state.colleges:
        st.info("Please first create a college")
    else:
        clgname = st.selectbox("Choose College", [c.cname for c in st.session_state.colleges])


        roll = st.text_input("Roll Number")
        sname = st.text_input("Student Name")
        branch = st.text_input("Branch")


        if st.button("SUBMIT STUDENT RECORD"):
            if not(roll and sname and branch):
                st.error("All information is mandatory: don't leave empty cell")
            else:
                clg = find_college(clgname)
                obj = student(roll,sname, branch)
                clg.add_student(obj)
                st.success("Student added successfully")


elif menu_choice == "Add New Teacher":
    if not st.session_state.colleges:
        st.info("Please first create a college")
    else:
        clgname = st.selectbox("Choose College", [c.cname for c in st.session_state.colleges])


        subject = st.text_input("Enter Subject")
        tname = st.text_input("Teacher Name")
        branch = st.text_input("Branch")


        if st.button("SUBMIT TEACHER RECORD"):
            if not(subject and tname and branch):
                st.error("All information is mandatory: don't leave empty cell")
            else:
                clg = find_college(clgname)
                obj = student(subject,tname, branch)
                clg.add_teacher(obj)
                st.success("Teacher added successfully")


elif menu_choice == "Display students":
    if not st.session_state.colleges:
        st.info("Please first create a college")
    else:
        clgname = st.selectbox("Choose College", [c.cname for c in st.session_state.colleges])


        st.subheader(f"Students in {clgname}")
        if st.button("DISPLAY"):
            clg = find_college(clgname)
            for i, s in enumerate(clg.students, 1):
                st.write(f"{i} : {s}")
        else:
            st.warning("No Student found")


elif menu_choice == "Display teachers":
    if not st.session_state.colleges:
        st.info("Please first create a college")
    else:
        clgname = st.selectbox("Choose College", [c.cname for c in st.session_state.colleges])


        st.subheader(f"Teachers in {clgname}")
        if st.button("DISPLAY"):
            clg = find_college(clgname)
            for i, t in enumerate(clg.teachers, 1):
                st.write(f"{i} : {t}")
        else:
            st.warning("No teacher found")

elif menu_choice == "Display colleges":
    st.subheader("All Colleges List")
    if not st.session_state.colleges:
        st.warning("No college added yet")
    else:
        for i, c in enumerate(st.session_state.colleges, 1):
            st.write(f"{i} : {c.cname}")  
