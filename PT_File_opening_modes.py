#Домашнее задание по теме "Режимы открытия файлов"

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def add(self, *products):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                existing_products = set(line.strip() for line in file)
        except FileNotFoundError:
            # Если файл не существует, создаем его и инициализируем пустое множество
            existing_products = set()

        for product in products:
            product_str = str(product)
            if product_str not in existing_products:
                with open(self.__file_name, 'a', encoding='utf-8') as file:
                    file.write(product_str + '\n')
            else:
                print(f"Продукт {product.name} уже есть в магазине")

    def get_products(self):
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                products = file.read()
            return products

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')

p2 = Product('Spaghetti', 3.4, 'Groceries')

p3 = Product('Potato', 5.5, 'Vegetables')



print(p2) # __str__



s1.add(p1, p2, p3)



print(s1.get_products())