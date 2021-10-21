def average_grade(list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)

def take_second(elem):
    return elem[1]


class STUDENT:
    def __init__(self, name, surname, record_book, number, grades):
        self.name = name
        self.surname = surname
        self.record_book = record_book
        self.number = number
        self.grades = grades
        self.average = average_grade(grades)


class GROUP:
    def __init__(self):
        self.students = list()
        self.grades = list()

    def sort(self):
        for student in self.students:
            self.grades.append((student, student.average))
        self.grades.sort(key=take_second, reverse=True)

    def print(self):
        for student in self.grades[0:5]:
            print(student[0].name, student[0].surname, student[1])


first=STUDENT('Fedir','Petrenko',123, 9,{5,2,3})
second=STUDENT('Alex','Ivanov',124, 8,{1,2,4})
third=STUDENT('Irina','Kazanishena',125, 7,{1,2,5})
fourth=STUDENT('Ivanna','Vakuliuk',126, 6,{1,3,3})
fifth=STUDENT('Ivan','Petruk',127, 5,{5,4,4})
sixth=STUDENT('Vasia','Derliuk',128, 3,{1,2,3})
group=GROUP()
group.students=(first,second,third,fourth,fifth,sixth)
group.sort()
group.print()