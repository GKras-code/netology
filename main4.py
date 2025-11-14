class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        list_grades = []
        for course, grade in self.grades.items():
            list_grades += grade
        
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {sum(list_grades)/len(list_grades)}\nКурсы в процессе изучения: {",".join(self.courses_in_progress)}\nЗавершенные курсы: {",".join(self.finished_courses)}'

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):        
        pass
     
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        list_grades = []
        for course in self.courses_attached:
            list_grades += self.grades.get(course, [])
        
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum(list_grades)/len(list_grades)}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


some_lecturer = Lecturer('John', 'Doe')
some_lecturer.courses_attached += ['Python', 'Git']

some_lecturer2 = Lecturer('Some', 'Buddy')
some_lecturer2.courses_attached += ['Python', 'Java']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_student2 = Student('Bill', 'Gates', 'your_gender')
some_student2.courses_in_progress += ['Python', 'Java']
some_student2.finished_courses += ['Основы программирования']

some_reviewer = Reviewer('Sam', 'Wilson')
some_reviewer.courses_attached += ['Python', 'Git']

some_reviewer2 = Reviewer('Emily', 'Davis')
some_reviewer2.courses_attached += ['Python', 'Java']

some_student.rate_lecturer(some_lecturer, 'Python', 8)
some_student.rate_lecturer(some_lecturer, 'Python', 9)
some_student2.rate_lecturer(some_lecturer2, 'Python', 7)
some_student2.rate_lecturer(some_lecturer2, 'Java', 8)

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 9)
some_reviewer2.rate_hw(some_student2, 'Python', 8)
some_reviewer2.rate_hw(some_student2, 'Java', 9)

def average_grade_for_course(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades += student.grades[course]
    return sum(total_grades) / len(total_grades) if total_grades else 0

def average_grade_for_lecturers(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += lecturer.grades[course]
    return sum(total_grades) / len(total_grades) if total_grades else 0



print(some_reviewer)
print(some_reviewer2)
print(some_lecturer)
print(some_lecturer2)
print(some_student)
print(some_student2)
pass