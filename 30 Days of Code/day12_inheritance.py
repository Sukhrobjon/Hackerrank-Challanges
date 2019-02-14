class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)


class Student(Person):
    
    """
        firstName - A string denoting the Person's first name.
        lastName - A string denoting the Person's last name.
        id - An integer denoting the Person's ID number.
        scores - An array of integers denoting the Person's test scores.
    """
    def __init__(self, firstName, lastName, idNumber, score_grade=None):
        super().__init__(firstName, lastName, idNumber)
        if score_grade is None:
            self.score_grade = []
        else:
            self.score_grade = score_grade

    

    def calculate(self):
        """
            Return: A character denoting the grade.
        """
        average = sum(self.score_grade)/len(self.score_grade)
        if 90 <= average <= 100:
            return 'O'
        elif 80 <= average < 90:
            return 'E'
        elif 70 <= average < 80:
            return 'A'
        elif 55 <= average < 70:
            return 'P'
        elif 40 <= average < 55:
            return 'D'
        else:
            return 'T'
        
