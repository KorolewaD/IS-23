# Создайте класс "Товар" с атрибутами "название", "цена" и "количество". Напишите
# метод, который выводит информацию о товаре в формате "Название: название,
# Цена: цена, Количество: кол-во".
class Product:
    name = str()
    price = float()
    quantity = int()
    def set_inf(self, name, price, quantity):
        if type(name) == str and type(price) in (float, int) and type(quantity) == int:
            self.name = name
            self.price = price
            self.quantity = quantity
        else:
            print('Введите правильные значения')
    def get_inf(self):
        print(f'Название: {self.name}, Цена: {self.price}, Количество: {self.quantity}')
t = Product()
t.set_inf('Чипсы', 139, 15)
t.get_inf()