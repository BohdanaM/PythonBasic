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
