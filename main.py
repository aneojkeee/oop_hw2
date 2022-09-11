class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Error'

    def average_grade(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        result = (
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}')
        return result


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def average_grade(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_grade() < other.average_grade()

    def __str__(self):
        result = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                  f'Средняя оценка за лекции: {self.average_grade()}')
        return result


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Основы программирования']

worst_student = Student('Ivan', 'Ivanov', 'male')
worst_student.courses_in_progress += ['Python', 'Git']
worst_student.finished_courses += ['Основы программирования']

mvp_lecturer = Lecturer('Garry', 'Osborn')
mvp_lecturer.courses_attached += ['Python']

fail_lecturer = Lecturer('Peter', 'Parker')
fail_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Body', 'Dan')
cool_reviewer.courses_attached += ['Python']

no_cool_reviewer = Reviewer('Eva', 'Om')
no_cool_reviewer.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 6)

cool_reviewer.rate_hw(worst_student, 'Python', 8)
cool_reviewer.rate_hw(worst_student, 'Python', 5)

best_student.rate_lec(mvp_lecturer, 'Python', 10)
worst_student.rate_lec(fail_lecturer, 'Python', 5)

student_list = [best_student, worst_student]
lecturer_list = [mvp_lecturer, fail_lecturer]

students_grades_list = []


def average_student_grade(student_list, course):
    for student in student_list:
        for key, value in student.grades.items():
            if key is course:
                students_grades_list.extend(value)
    result = sum(students_grades_list) / len(students_grades_list)
    print(f'Средний бал по всем студентам курса {course}: {result}')


lecturer_grades_list = []


def average_lecturer_grade(lecturer_list, course):
    for lecturer in lecturer_list:
        for key, value in lecturer.grades.items():
            if key is course:
                lecturer_grades_list.extend(value)
    result = sum(lecturer_grades_list) / len(lecturer_grades_list)
    print(f'Средний бал по всем лекторам курса {course}: {result}')


average_student_grade(student_list, 'Python')
average_lecturer_grade(lecturer_list, 'Python')

print('Наивысшая оценка лектору:', mvp_lecturer.grades)
print('Наивысшая оценка студенту:', best_student.grades)
print('Лучший студент:', best_student)
print('Худший студент:', worst_student)
print('Лучший лектор:', mvp_lecturer)
print('Худший лектор:', fail_lecturer)
print('Лучший ответ:', cool_reviewer)
print('Худший ответ:', no_cool_reviewer)