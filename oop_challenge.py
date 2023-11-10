# Python Object-Oriented Programming
# Classes and Instances

class Apprentice:

    def __init__(self, first, last, language):
        self.first = first
        self.last = last
        self.language = language
        self.cohort = first + ' ' + last + ': ' + language

    def fullname(self):
        return '{} {}'.format(self.first, self.last)



app_1 = Apprentice('Meagan', 'Hollingsworth', 'Python')
app_2 = Apprentice('Daniel', 'Guerrero', 'Go')
app_3 = Apprentice('Aaron', 'Sanchez', 'Go')

print(app_1.language)
print(app_2.cohort)

print(Apprentice.fullname(app_3))