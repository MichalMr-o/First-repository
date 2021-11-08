import csv
import requests
import datetime


class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


class Teacher(Person):
    def __init__(self, name: str, surname: str, subject_taught: str):
        super().__init__(name, surname)
        self.subject_taught = subject_taught


class Student(Person):
    def __init__(self, name: str, surname: str, age: int = None, date_of_birth: str = None):
        super().__init__(name, surname)
        self.age = age
        self.date_of_birth = date_of_birth
        if (self.date_of_birth is not None) and (self.age is None):
            self.calculate_age(self.date_of_birth)

    def calculate_age(self, date_of_birth):
        actual_year = datetime.date.today().year
        self.age = actual_year - int(date_of_birth[0:4])


class Course:
    def __init__(self, subject: str, max_students: int, teacher: Teacher):
        self.subject = subject
        self.max_students = max_students
        self.teacher = teacher
        self.students_enrolled = []
        self.verify_teacher_knowledge()
        self.students_list = None

    def enroll_older_student(self, st: Student):
        if len(self.students_enrolled) < self.max_students:
            if st.age > 23:
                self.students_enrolled.append(st)
            else:
                print(
                    f"Student {st.name} {st.surname} ma za mało lat by uczestniczyć w kursie {self.subject}")
        else:
            print(f"Jest już maksymalna ilość studentów na kursie {self.subject}")

    def get_students_from_file(self, file_csv="students_list.csv"):
        self.students_list = []
        with open(file_csv, encoding="utf-8") as file:
            reader = csv.reader(file)
            for line in reader:
                self.students_list.append(Student(line[0], line[1], int(line[2])))
        return self.students_list

    def verify_teacher_knowledge(self):
        if self.teacher.subject_taught == self.subject:
            print("Kompetencje odpowiadające przedmiotowi.")
        else:
            print("UWAGA! Kompetencje rozbieżne.")

    def get_random_virtual_students_from_api(self, size: int =30):
        self.students_list = []
        r = requests.get(f"https://random-data-api.com/api/users/random_user?size={size}")
        if r.status_code == 200:
            print('Dane zostaly pobrane')
            data = r.json()
            for user in data:
                self.students_list.append(
                    Student(user['first_name'], user['last_name'], date_of_birth=user['date_of_birth']))
            return self.students_list

    def enroll_older_students_from_list(self):
        for st in self.students_list:
            self.enroll_older_student(st)


if __name__ == '__main__':
    # st1 = Student("Adam", "Nowak", 12)
    # st2 = Student("Krzysztof", "Kowalski", 10)
    # st3 = Student("Prymus", "Doprzodu", 13)
    te1 = Teacher("Pitagoras", "Pierwszy", "Mathematic")
    math_course = Course("Mathematic", 15, te1)
    #
    # print(math_course.students_enrolled)
    #
    # math_course.enroll_older_student(st1)
    # math_course.enroll_older_student(st2)
    # math_course.enroll_older_student(st3)

    # math_course.enroll_students_from_file()
    #
    # for student in math_course.students_list:
    #     print(student.name, student.surname, student.age)

    # math_course.get_random_virtual_student_from_api()

    # for student in math_course.students_enrolled:
    #     print(student.name, student.surname, student.age)
    math_course.get_random_virtual_students_from_api()
    math_course.enroll_older_students_from_list()

    for st in math_course.students_enrolled:
        print(st.name, st.surname, st.age)
    # for student in math_course.students_list:
    #     print(student.name, student.surname, student.age)
