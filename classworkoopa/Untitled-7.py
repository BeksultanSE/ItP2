class Name:
    def __init__(self, fname, lname):
        fname = fname.capitalize()
        lname = lname.capitalize()
        self.fname = fname
        self.lname = lname
        self.fullname = f'{fname} {lname}'
        self.initials = f'{fname[0]}.{lname[0]}'
    def __str__(self):
        return f'name={self.fname}\nsurname={self.lname}\n{self.fullname}\n{self.initials}\n'
a1 = Name("john", "SMITH")
print(a1.__str__())