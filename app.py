class Product:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self._stock = 0
        self._price = 0

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError('Stock can not be less than zero.')
        self._stock

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price can not be less than zero.')
        self._price
