class CashRegister:
    # Constructs a cash register with cleared item count and total,
    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0.0

    # Adds an item to this cash register.
    # @param price the price of this item
    def addItem(self, price):
        self._itemCount = self._itemCount + 1
        self._totalPrice = self._totalPrice + price

    # Gets the price of all items in the current sale.
    # @return the total price.
    def getTotal(self):
        return self._totalPrice

    def getCount(self):
        return self._itemCount

    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0.0
