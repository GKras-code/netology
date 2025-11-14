class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades += grades
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg = self.average_grade()
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg:.1f}\n'
                f'Курсы в процессе изучения: {in_progress}\n'
                f'Завершенные курсы: {finished}')
    
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        all_grades = []
        for grades in self.grades.values():
            all_grades += grades
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg = self.average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg:.1f}')

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)



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


student1 = Student('Ольга', 'Алёхина', 'Ж')
student2 = Student('Иван', 'Петров', 'М')
student1.courses_in_progress += ['Python', 'Java']
student2.courses_in_progress += ['Python', 'C++']
student1.finished_courses += ['Введение в программирование']
student2.finished_courses += ['Основы программирования']

lecturer1 = Lecturer('Иван', 'Иванов')
lecturer2 = Lecturer('Мария', 'Сидорова')
lecturer1.courses_attached += ['Python', 'C++']
lecturer2.courses_attached += ['Python', 'Java']

reviewer1 = Reviewer('Пётр', 'Петров')
reviewer2 = Reviewer('Елена', 'Кузнецова')
reviewer1.courses_attached += ['Python', 'C++']
reviewer2.courses_attached += ['Python', 'Java']

reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Java', 10)
reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'C++', 7)

student1.rate_lecture(lecturer1, 'Python', 7)
student1.rate_lecture(lecturer1, 'Python', 8)
student2.rate_lecture(lecturer1, 'C++', 9)
student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'Java', 8)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

print('student1 > student2:', student1 > student2)
print('lecturer1 < lecturer2:', lecturer1 < lecturer2)

print(f'Средняя оценка за домашние задания по курсу Python: {average_grade_for_course([student1, student2], "Python")}')
print(f'Средняя оценка за лекции по курсу Python: {average_grade_for_lecturers([lecturer1, lecturer2], "Python")}')
 
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
 
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
 
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
 
# print(best_student.grades)


# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# print(isinstance(lecturer, Mentor)) # True
# print(isinstance(reviewer, Mentor)) # True
# print(lecturer.courses_attached)    # []
# print(reviewer.courses_attached)    # []


# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# student = Student('Алёхина', 'Ольга', 'Ж')
 
# student.courses_in_progress += ['Python', 'Java']
# lecturer.courses_attached += ['Python', 'C++']
# reviewer.courses_attached += ['Python', 'C++']
 
# print(student.rate_lecture(lecturer, 'Python', 7))   # None
# print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
# print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
# print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка
 
# print(lecturer.grades)  # {'Python': [7]}  


# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# student = Student('Алёхина', 'Ольга', 'Ж')

# student.courses_in_progress += ['Python', 'Java']
# student.finished_courses += ['Введение в программирование']
# lecturer.courses_attached += ['Python', 'C++']
# reviewer.courses_attached += ['Python', 'C++']

# student.rate_lecture(lecturer, 'Python', 7)
# student.rate_lecture(lecturer, 'Python', 8)
# reviewer.rate_hw(student, 'Python', 9)
# reviewer.rate_hw(student, 'Java', 10)

# print(student)
# print(lecturer)
# print(reviewer)