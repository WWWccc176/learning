class Teacher:
    def __init__(self, name, subject, age, height, weight, repu):
        self.name = name
        self.subject = subject
        self.age = age
        self.height = height
        self.weight = weight
        self.repu = repu
        
    #getter
    def getname(self):
        print(self.name)

teacher1 = Teacher("SunZhe", "Maths", 211, 175, 65, 100)

teacher1.getname()
