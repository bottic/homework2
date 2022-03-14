def mean_grade(dict):
    sum = 0
    count = 0
    for i in dict.values():
        if i != None:
            for grade in i:
                sum += grade
                count += 1
    mean = sum / count
    return mean

def mean_grade_course(list_students, course):
    sum = 0
    count = 0
    for i in list_students:
        for x in  i.grades[course]:
            sum += x
            count += 1
    mean = sum / count
    return mean

def mean_greade_lecturer(list_lecturer, course):
    sum = 0
    count = 0
    for i in list_lecturer:
        for x in i.grades[course]:
            sum += x
            count += 1
    mean = sum/count
    return mean



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        text = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка: {mean_grade(self.grades)} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}"
        return text

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.course_attached and lecturer.course_attached in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return mean_grade(self.grades) < mean_grade(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        text = f"Имя: {self.name} \nФамилия: {self.surname} "
        return text


class Lecturer(Mentor):
    def __init__(self, name, surname, courses):
        self.name = name
        self.surname = surname
        self.grades = {}
        self.course_attached = courses

    def __str__(self):
        text = f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка: {mean_grade(self.grades)} "
        return text

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return mean_grade(self.grades) < mean_grade(other.grades)

class Reviewer(Mentor):
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




best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student1 = Student('a', 'b', 'your_gender')
best_student1.courses_in_progress += ['Python']
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor1 = Reviewer('S','B')
cool_mentor1.courses_attached += ['Python', 'Git']
Lecturer1 = Lecturer('sose', 'beby', 'Python')
Lecturer2 = Lecturer('sose1', 'beby1', 'Python')
best_student.rate_lecturer(Lecturer1,'Python',9)
best_student.rate_lecturer(Lecturer1,'Python',1)
best_student.rate_lecturer(Lecturer2,'Python',3)
best_student.rate_lecturer(Lecturer2,'Python',1)
# Reviewer1 = Reviewer('Some','Buddy')
# Reviewer1.courses_attached.append('Python')
cool_mentor.rate_hw(best_student,'Python', 7)
cool_mentor.rate_hw(best_student,'Python', 8)
cool_mentor.rate_hw(best_student1,'Python', 9)
cool_mentor.rate_hw(best_student1,'Python', 10)

print(best_student)
print()
print(best_student1)
print()
print(Lecturer1)
print()
print(Lecturer2)
print()
print(cool_mentor)
print()
print(cool_mentor1)
print()
print(mean_greade_lecturer([Lecturer1,Lecturer2], 'Python'))
print()
print(mean_grade_course([best_student,best_student1], 'Python'))
