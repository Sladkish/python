__author__ = 'Михайловский Василий Владимирович'
class Student:
    def __init__(self, student_name, surname, mother_name, father_name, class_room):
        self.student_name = student_name
        self.surname = surname
        self.mother_name = mother_name
        self.father_name = father_name
        self.class_room = class_room


    def full_student_name(self):
        return self.student_name + ' ' + self.surname

    def full_mother_name(self):
        return self.mother_name + ' ' + self.surname

    def full_father_name(self):
        return self.father_name + ' ' + self.surname

    def parents(self):
        print(f"мать: {self.full_mother_name()}, отец: {self.full_father_name()}")
        return

class Teacher:
    def __init__(self, name, surname, teach_lesson , teach_classes):
        self.name = name
        self.surname = surname
        self.teach_lesson = teach_lesson
        self.teach_classes = teach_classes

    def teacher_full_name(self):
        return self.name + ' ' + self.surname




students=[Student("Владимир", "Палий", "Елизавета", "Виктор","5 Б"),
Student("Алексей", "Волков", "Надежда", "Павел","8 Д"),
Student("Арсен", "Маркарян", "Тамара", "Григорий","6 А"),
Student("Александр", "Мякотин", "Виктория", "Вячеслав","6 А"),
Student("Андрей", "Кирпичев", "Светлана", "Сергей","7 В"),
Student("Юлия", "Кравченко", "Галина", "Олег","7 В"),
Student("Евгения", "Панова", "Екатерина", "Александр","7 В")]

teachers=[Teacher("Владимир", "Быстров", "Информатика", ("5 Б","6 А")),
Teacher("Наталья", "Арцыкова", "Математика", ("5 Б","6 А","7 В")),
Teacher("Альберт", "Акопян", "Физкультура", ("5 Б","6 А","7 В","8 Д")),
Teacher("Ирина", "Евграфова", "Литература", ("7 В","8 Д"))]


class_for_student=input(f" Введите номер класса по образцу (например:10 А) для поиска в нем учеников :")
class_for_teacher=input(f" Введите номер класса по образцу (например:10 А) для поиска преподающих в нем учителей :")
name_for_parents=input(f" Введите имя и фамилию ученика для поиска его родителей (например: Иванов Иван) :")
name_for_lesson=input(f" Введите имя и фамилию ученика для поиска предметов которые он изучает (например: Иванов Иван) :")

all_students=[]
classes=[]
students_in_class=[]
find_parents=[]
find_lessons=[]
find_teachers=[]
for student in students:
    classes.append(student.class_room)
    all_students.append(student.full_student_name())

    if student.class_room==class_for_student:
        students_in_class.append(student.full_student_name())

    if student.full_student_name()==name_for_parents:
        find_parents.append(student.full_mother_name())
        find_parents.append(student.full_father_name())

    if student.full_student_name() == name_for_lesson:
        for teacher in teachers:
            if student.class_room in teacher.teach_classes:
                find_lessons.append(teacher.teach_lesson)

for teacher in teachers:
    if class_for_teacher in teacher.teach_classes:
        find_teachers.append(teacher.teacher_full_name())

classes=set(classes)
print(classes)
if class_for_student not in classes:
    print(f"Класса {class_for_student} в школе нет ")
else:
    print(f"список учеников в {class_for_student}  {students_in_class}")

if class_for_teacher not in classes:
    print(f"Класса {class_for_teacher} в школе нет ")
else:
    print(f"в классе  {class_for_teacher} преподают следующие учителя {find_teachers}")

if name_for_parents not in all_students:
    print(f"Ученика {name_for_parents} в школе нет, либо имя введено не верно")
else:
    print(f"ученик {name_for_parents}, его мать: {find_parents[0]}, его отец: {find_parents[1]}")

if name_for_lesson not in all_students:
    print(f"Ученика {name_for_lesson} в школе нет, либо имя введено не верно")
else:
    print(f"ученик {name_for_lesson} изучает следующие предеты: {find_lessons}")





