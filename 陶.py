class People(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
    def info(self):
        print(self.name,self.sex)

class Man(People):
    pass

p1 = Man("tao","nan")
p1.info()