import string

class Sztring:

    def __init__(self, s1):
        self.st=s1

    def __str__(self):
        return "Az alap string: {} ".format(self.st)

    def setstring(self):
        self.st = input("adjon meg valami szöveget: ")
        return self

    def stringup(self):
        return self.st.upper()

    def stringlow(self):
        return self.st.lower()

    def capital(self):
        return string.capwords(self.st)


c="valami"
print(Sztring(c))
print(Sztring.setstring(Sztring))
print(Sztring.stringup(Sztring))
print(Sztring.stringlow(Sztring))
print(Sztring.capital(Sztring))

