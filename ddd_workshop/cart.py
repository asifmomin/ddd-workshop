class Item:
    def __init__(self, name,qty=1):
        self.name = name
        self.qty = qty


class Cart:
    __items = []

    def addItem(self, item):
        self.__items.append(item)

    def length(self):
        return len(self.__items)

    def getItems(self):
        return self.__items

    def getTotalItemCount(self):
        count = 0
        for item in self.__items:
            count += item.qty

        return count
