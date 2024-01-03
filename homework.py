class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.rate_hw(self, course, grade)
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.calculate_avg_grade()}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}''')

    def calculate_avg_grade(self):
        total_grades = sum(sum(course_grades) for course_grades in self.grades.values())
        total_assignments = sum(len(course_grades) for course_grades in self.grades.values())
        return round(total_grades / total_assignments, 1) if total_assignments > 0 else 0

    def __lt__(self, other):
        return self.calculate_avg_grade() < other.calculate_avg_grade()

    def __le__(self, other):
        return self.calculate_avg_grade() <= other.calculate_avg_grade()

    def __eq__(self, other):
        return self.calculate_avg_grade() == other.calculate_avg_grade()

    def __ne__(self, other):
        return self.calculate_avg_grade() != other.calculate_avg_grade()

    def __gt__(self, other):
        return self.calculate_avg_grade() > other.calculate_avg_grade()

    def __ge__(self, other):
        return self.calculate_avg_grade() >= other.calculate_avg_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}'''


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    def calculate_avg_lecture_grade(self):
        if self.lecture_grades:
            total_grade = sum(sum(grades) for grades in self.lecture_grades.values())
            total_count = sum(len(grades) for grades in self.lecture_grades.values())
            return total_grade / total_count
        else:
            return 0

    def __str__(self):
        return f'''Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.calculate_avg_lecture_grade()}'''

    def __lt__(self, other):
        return self.calculate_avg_lecture_grade() < other.calculate_avg_lecture_grade()

    def __le__(self, other):
        return self.calculate_avg_lecture_grade() <= other.calculate_avg_lecture_grade()

    def __eq__(self, other):
        return self.calculate_avg_lecture_grade() == other.calculate_avg_lecture_grade()

    def __ne__(self, other):
        return self.calculate_avg_lecture_grade() != other.calculate_avg_lecture_grade()

    def __gt__(self, other):
        return self.calculate_avg_lecture_grade() > other.calculate_avg_lecture_grade()

    def __ge__(self, other):
        return self.calculate_avg_lecture_grade() >= other.calculate_avg_lecture_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'''Имя: {self.name} 
Фамилия: {self.surname}'''


def calculate_avg_hw_grade(students, course):
    total_grade = sum(sum(student.grades[course]) for student in students if course in student.grades)
    total_assignments = sum(len(student.grades[course]) for student in students if course in student.grades)
    return round(total_grade / total_assignments, 1) if total_assignments > 0 else 0


def calculate_avg_lecture_grade(lecturers, course):
    total_grade = sum(sum(lecturer.lecture_grades[course]) for lecturer in lecturers if hasattr(lecturer, 'lecture_grades') and course in lecturer.lecture_grades)
    total_count = sum(len(lecturer.lecture_grades[course]) for lecturer in lecturers if hasattr(lecturer, 'lecture_grades') and course in lecturer.lecture_grades)
    return round(total_grade / total_count, 1) if total_count > 0 else 0


student1 = Student('Roman', 'Fedotov', 'male')
student2 = Student('Julia', 'Gordeeva', 'female')

lecturer1 = Lecturer('Ruoy', 'Eman')
lecturer2 = Lecturer('Some', 'Buddy')

reviewer1 = Reviewer('Emed', 'Brown')
reviewer2 = Reviewer('Marty', 'Mcfly')

student1.courses_in_progress.append('Python')
student2.courses_in_progress.append('Python')

lecturer1.courses_attached.append('Python')
lecturer2.courses_attached.append('Python')

reviewer1.courses_attached.append('Python')
reviewer2.courses_attached.append('Python')

reviewer1.rate_hw_student(student1, 'Python', 9)
reviewer1.rate_hw_student(student2, 'Python', 7)

lecturer1.rate_hw(student1, 'Python', 10)
lecturer1.rate_hw(student2, 'Python', 5)

lecturer1.lecture_grades['Python'] = [5, 8, 7]
lecturer2.lecture_grades['Python'] = [10, 9, 4]

print(student1)
print(student2)

print(lecturer1)
print(lecturer2)

print(reviewer1)
print(reviewer2)

python_avg_hw_grade = calculate_avg_hw_grade([student1, student2], 'Python')
print(f'Средняя оценка за домашние задания: {python_avg_hw_grade}')

python_lecturers = [lecturer1, lecturer2]
python_avg_lecture_grade = calculate_avg_lecture_grade(python_lecturers, 'Python')
print(f'Средняя оценка за лекции: {python_avg_lecture_grade}')