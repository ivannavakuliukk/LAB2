class BINARY_TREE:

    def __init__(self, code = -1, price = -1):
        self.__code = code
        self.__price = price
        self.__left = 0
        self.__right = 0

    def add(self, code, price):
        BINARE_TREE = BINARY_TREE
        if self.__code > code:
            if self.__left != 0:
                self.__left.add(code, price)
            else:
                self.__left = BINARE_TREE(code, price)
        else:
            if self.__right != 0:
                self.__right.add(code, price)
            else:
                self.__right = BINARE_TREE(code, price)

    def search(self, code):
        if self.__code == code:
            return self.__price
        if self.__code > code:
            if self.__left == 0:
                print("there is nothing here")
                return 0
            return self.__left.search(code)
        else:
            if self.__right == 0:
                print("there is nothing here" )
                return 0
            return self.__right.search(code)


root = BINARY_TREE(1, 50)
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