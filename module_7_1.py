from pprint import pprint
class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.get_products()

    def get_products(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'r')
        _file = file.read()
        file.close()
        return _file

    def add(self, *products):
        for i in products:
            _file = self.get_products()
            if i.name in _file:
                print(f'Продукт {i.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(i.__str__())
                file.write('\n')
                file.close()

s1 = Shop('products.txt')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())


