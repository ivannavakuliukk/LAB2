class Product:
    def __init__(self, price, size, color):
        self.price = price
        self.size = size
        self.color = color

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
    def price_sum(self):
        sum = 0
        for product in self.products:
            sum += product.price
        return sum
    def get(self):
        return f"Customer:{customer}"
products = [Product(10, 'S', "red"), Product(20, 'M', "blue")]
customer = Customer("Vakuliuk", "Ivanna", "Volodymyrivna", "0950456578")
order = Order(customer, products)
print(order.price_sum())