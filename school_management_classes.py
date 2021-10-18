class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname


class Teacher(Person):
    def __init__(self, name: str, surname: str, subject_taught: str):
        super().__init__(name, surname)
        self.subject_taught = subject_taught


class Student(Person):
    def __init__(self, name: str, surname: str, age: int):
        super().__init__(name, surname)
        self.age = age


class Course:
    def __init__(self, subject: str, max_students: int, teacher: Teacher):
        self.subject = subject
        self.max_students = max_students
        self.teacher = teacher
        self.students_enrolled = []
        self.verify_teacher_knowledge()

    def enroll_older_student(self, st: Student):
        if len(self.students_enrolled) < self.max_students:
            if st.age > 9:
                self.students_enrolled.append(st)
            else:
                print(
                    f"Student {st.name} {st.surname} ma za mało lat by uczestniczyć w kursie {self.subject}")
        else:
            print(f"Jest już maksymalna ilość studentów na kursie {self.subject}")

    def verify_teacher_knowledge(self):
        if self.teacher.subject_taught == self.subject:
            print("Kompetencje odpowiadające przedmiotowi.")
        else:
            print("UWAGA! Kompetencje rozbieżne.")


if __name__ == '__main__':
    st1 = Student("Adam", "Nowak", 12)
    st2 = Student("Krzysztof", "Kowalski", 10)
    st3 = Student("Prymus", "Doprzodu", 13)
    te1 = Teacher("Sokrates", "Pierwszy", "Mathematic")
    math_course = Course("Mathematic", 2, te1)

    print(math_course.students_enrolled)

    math_course.enroll_older_student(st1)
    math_course.enroll_older_student(st2)
    math_course.enroll_older_student(st3)

    for student in math_course.students_enrolled:
        print(student.name, student.surname)
