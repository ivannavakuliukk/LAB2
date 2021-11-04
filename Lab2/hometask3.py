def average_grade(list):
    sum = 0
    for i in list:
        sum += i
    return round(sum/len(list), 2)


def take_second(elem):
    return elem[1]


class Student:
    def __init__(self, name, surname, record_book, number, grades):
        self.name = name
        self.surname = surname
        self.record_book = record_book
        self.number = number
        self.grades = grades
        self.average = average_grade(grades)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        if not len(name):
            raise ValueError
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError
        if not len(surname):
            raise ValueError
        self._surname = surname

    @property
    def record_book(self):
        return self._record_book

    @record_book.setter
    def record_book(self, record_book):
        if not isinstance(record_book, int):
            raise TypeError
        if record_book < 0:
            raise ValueError
        self._record_book = record_book

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if not isinstance(number, int):
            raise TypeError
        if number < 0:
            raise ValueError
        self._number = number

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, grades):
        if not all(isinstance(grade, int) for grade in grades):
            raise TypeError
        if not all(0 < grade <= 5 for grade in grades):
            raise ValueError
        self._grades = grades


class Group:
    def __init__(self):
        self.students = list()
        self.grades = list()

    @property
    def students(self):
        return self._students

    @students.setter
    def students(self, students):
        if not all(isinstance(student, Student) for student in students):
            raise TypeError
        if len(students) > 20:
            raise ValueError
        self._students = students

    def sort(self):
        for student in self.students:
            self.grades.append((student, student.average))
        self.grades.sort(key=take_second, reverse=True)

    def print(self):
        for student in self.grades[0:5]:
            print(student[0].name, student[0].surname, student[1])


first=Student('Fedir','Petrenko',123, 9,{5,2,3})
second=Student('Alex','Ivanov',124, 8,{1,2,4})
third=Student('Irina','Kazanishena',125, 7,{1,2,5})
fourth=Student('Ivanna','Vakuliuk',126, 6,{1,3,3})
fifth=Student('Ivan','Petruk',127, 5,{5,4,4})
sixth=Student('Vasia','Derliuk',128, 3,{1,2,3})
group=Group()
group.students=(first,second,third,fourth,fifth,sixth)
group.sort()
group.print()