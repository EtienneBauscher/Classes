"""'student.py' is a program that computes the following:
    1. The average score of a student's grades.
    2. It tests whether a student is a male or a female.
The program utilises a class called Student
The class hosts various fucntions for the computation of the needed outcomes.
"""


class Student(object):
    """class 'Student' hosts the following variables:
            a. age - for the student's age
            b. name - for the name of the student.
            c. gender - for the gender of the student
            d. grades - for the grades of the student
        """

    # initialise the class through the constructor
    def __init__(self, age, name, gender, grades):
        self.age = age
        self.name = name
        self.gender = gender
        self.grades = grades

    def compute_average(self):
        """this function calculates the average of the student's scores"""
        # utilise the class variables in the list to compute
        average = sum(
            self.grades)/len(self.grades)
        print("The average for student " +
              str(self.name) + " is " + str(average))  # print the results

    def check_if_male(self):
        """'check_if_male()' checks whether a student is male or not and
        prints "True" if yes and "False" if no"""
        # use a conditional to check if the gender is male
        if self.gender == "Male":
            print("True")
        else:
            print("False")


# three students
MIKE = Student(20, "Philani Sithole", "Male", [64, 65])
SARAH = Student(19, "Sarah Jones", "Female", [82, 58])
ETIENNE = Student(43, "Etienne Bauscher", "Male", [99, 99])


# run a couple of checks on the newly added check_if_male() method
ETIENNE.check_if_male()
ETIENNE.compute_average()
SARAH.check_if_male()
MIKE.check_if_male()
# create a new list
# run a for loop through the list calling the functions
NEWLIST = [ETIENNE, SARAH, MIKE]
for i in NEWLIST:
    Student.check_if_male(i)
    Student.compute_average(i)
