class Product:
    def __init__(self, price, size, color):
        self.price = price
        self.size = size
        self.color = color

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, int):
            raise TypeError
        if price < 0:
            raise ValueError
        self._price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not isinstance(size, str):
            raise TypeError
        if not len(size):
            raise ValueError
        self._size = size

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError
        if not len(color):
            raise ValueError
        self._color = color


class Customer:
    def __init__(self, surname, name, patronymic, number):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.number = number


class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, products):
        if not all(isinstance(product, Product) for product in products):
            raise TypeError
        self._products = products

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError
        self._customer = customer

    def price_sum(self):
        sum = 0
        for product in self.products:
            sum += product.price
        return sum


products = [Product(10, 'S', "red"), Product(20, 'M', "blue")]
customer = Customer("Vakuliuk", "Ivanna", "Volodymyrivna", "0950456578")
order = Order(customer, products)
print(order.price_sum())