class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"first_name: {self.first_name}, last_name: {self.last_name}, gender: {self.gender}, age: {self.age}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, record_book: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupOverError("Can't add more than 10 students to the group")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        if not self.group:
            return f"Number: {self.number}\nNo students in the group."

        all_students = "\n".join(str(student) for student in self.group)
        return f"Number: {self.number}\n{all_students}"


class GroupOverError(Exception):
    def __init__(self, message):
        self.message = message

    def get_exception_message(self):
        return self.message


st1 = [
    Student("Male", 30, "Steve", "Jobs", "AN1"),
    Student("Female", 22, "Jane", "Doe", "AN2"),
    Student("Male", 25, "John", "Smith", "AN3"),
    Student("Female", 28, "Alice", "Johnson", "AN4"),
    Student("Male", 32, "Bob", "Brown", "AN5"),
    Student("Female", 27, "Carol", "Davis", "AN6"),
    Student("Male", 29, "Dave", "Wilson", "AN7"),
    Student("Female", 24, "Eve", "Taylor", "AN8"),
    Student("Male", 26, "Frank", "Miller", "AN9"),
    Student("Female", 31, "Grace", "Moore", "AN10"),
    Student("Male", 27, "Grag", "Moor", "AN11"),
]

gr = Group("PD1")

# Try to add students and handle exceptions
for stud in st1:
    try:
        gr.add_student(stud)
    except GroupOverError as e:
        print(e)

print(gr)
