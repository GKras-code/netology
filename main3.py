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
        
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {sum(list_grades)/len(list_grades)}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        list_grades = []
        for course, grade in self.grades.items():
            list_grades += grade
        return sum(list_grades) / len(list_grades) if list_grades else 0

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()            

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()        

    def __ne__(self, other):
        if isinstance(other, Student):
            return self.average_grade() != other.average_grade()       


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
        
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {sum(list_grades)/len(list_grades)}')

    def average_grade(self):
        list_grades = []
        for course in self.courses_attached:
            list_grades += self.grades.get(course, [])
        return sum(list_grades) / len(list_grades) if list_grades else 0

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()    

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()        

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() != other.average_grade()

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

# Пример использования
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']  # Добавляем курс лектору

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python'] + ['Git']
some_student.finished_courses += ['Введение в программирование']

some_student.rate_lecturer(some_lecturer, 'Python', 8)  # Студент выставляет оценку лектору
some_student.rate_lecturer(some_lecturer, 'Python', 5)  # Студент выставляет оценку лектору

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

print(some_reviewer)
print(some_lecturer)
print(some_student)

# Сравнение студентов
another_student = Student('Another', 'Student', 'gender')
another_student.courses_in_progress += ['Python']
some_reviewer.rate_hw(another_student, 'Python', 5)
some_reviewer.rate_hw(another_student, 'Python', 7)

print(f'{some_student > another_student}')
print(f'{some_student < another_student}')

# Сравнение лекторов
another_lecturer = Lecturer('Another', 'Lecturer')
another_lecturer.courses_attached += ['Python']
some_student.rate_lecturer(another_lecturer, 'Python', 9)
some_student.rate_lecturer(another_lecturer, 'Python', 7)

print(f'{some_lecturer > another_lecturer}')
print(f'{some_lecturer < another_lecturer}')