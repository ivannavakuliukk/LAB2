class Binary_tree:

    def __init__(self, code = 1, price = 50):
        self.code = code
        self.price = price
        self.left = 0
        self.right = 0

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        if not isinstance(code, int):
            raise TypeError
        if code < 0:
            raise ValueError
        self._code = code

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

    def add(self, code, price):
        if self.code > code:
            if self.left != 0:
                self.left.add(code, price)
            else:
                self.left = Binary_tree(code, price)
        else:
            if self.right != 0:
                self.right.add(code, price)
            else:
                self.right = Binary_tree(code, price)

    def search(self, code):
        if self.code == code:
            return self.price
        if self.code > code:
            if self.left == 0:
                print("there is nothing here")
                return 0
            return self.left.search(code)
        else:
            if self.right == 0:
                print("there is nothing here" )
                return 0
            return self.right.search(code)


root = Binary_tree(1, 50)
root.add(2, 305)
root.add(3, 123)
root.add(4, 399)
root.add(5, 430)
root.add(6, 320)
root.add(7, 150)

code = input("Enter the product code: ")
count = input("Enter the count of products: ")
if not code.isdigit() or not count.isdigit():
    raise TypeError("Variables should have type int")
print(root.search(int(code))*int(count))