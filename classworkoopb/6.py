class Programmer:
    def __init__(self, salary, work_hours):
        self.salary = salary
        self.work_hours = work_hours

    def __del__(self):
        print(f"oof, {self.salary}, {self.work_hours}")

    @staticmethod
    def compare(p1, p2):
        if p1.salary < p2.salary:
            return p1
        elif p1.salary > p2.salary:
            return p2
        else:
            return p1 if p1.work_hours < p2.work_hours else p2

prog1 = Programmer(50000, 40)
prog2 = Programmer(60000, 35)

better_prog = Programmer.compare(prog1, prog2)
print(f"The better programmer has a salary of {better_prog.salary} and works {better_prog.work_hours} hours.")

del prog1
del prog2
