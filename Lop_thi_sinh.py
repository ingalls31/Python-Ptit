import datetime


class student:
    def __init__(self, name, d, a, b, c):
        self.name = name 
        dt = datetime.datetime.strptime(d, "%d/%m/%Y")
        self.d = dt.strftime("%d/%m/%Y")
        self.s = a + b + c

a = student(input(), input(), float(input()), float(input()), float(input()))

print(a.name, a.d, "{:.1f}".format(a.s))
