class Human: # Создаем класс
    def __init__(self, full_name, mother, father): # Указываем атрибуты класса
        self.full_name = full_name
        self.mother = mother
        self.father = father

    def speak(self): # Создаем 1 метод для класса
        return "I can speak"

    def work(self): # Создаем 2й метод для класса
        return 'I can work'

class Man(Human): # Создаем подкласс Man
    def __init__(self, full_name, mother, father, wife): # Указываем атрибуты подкласса
        super().__init__(full_name, mother, father) # Указываем какие атрибуты наследуем от суперкласса
        self.wife = wife # Указываем атрибут только для подкласса

    def work(self): # модифицируем метод для подкласса
        return 'I can work HARD'

man1 = Man('Ivan Ivanov', 'Maria', 'Petr', 'Natalia') # Создаем образец подкласса Man


print(man1.__dict__)
print(man1.work())

class Woman(Human): # Создаем подкласс Woman
    def __init__(self, full_name, mother, father, husband, __childfen): # Создаем приватный атрибут __childfen
        super().__init__(full_name, mother, father)
        self.husband = husband
        self.__children = __childfen

    def work(self):
        return "Mother always works HARD"

    def get_children(self): # Создаем метод для доступа к приватному атрибуту __childfen
        return f'I have {self.__children} children'

    def set_children(self, newChild): # Создаем метод для изменения приватного атрибута __childfen
        self.__children = newChild

woman1 = Woman('Anna Ivanova', 'Sofia', 'Alex', 'Ivan', "No") # Создаем образец подкласса Woman

print(woman1.__dict__)
print(woman1.husband)
print(woman1.work())
print(woman1.speak())
# print(woman1.__children) # Пытаемся распечатать приватный атрибут __childfen
print("_________Get function for __children___________")
print(woman1.get_children())
woman1.set_children('2')
print("_________Get function for __children (changed)___________")
print(woman1.get_children())


