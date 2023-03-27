class Item:
    
    discount = 0.8
    allItems = []
    
    def __init__(self, name, price, quantity = 0):
        #checks
        assert isinstance(name, str), "Name should be a string."
        assert isinstance(price, (float, int)), "Price has to be a number."
        assert isinstance(quantity, int), "Quantity has to be a number"
        assert price >= 0, "Price cannot be negative"
        assert quantity >= 0, "Quantity cannot be negative"
                
        #Intializations
        self.name = name
        self.price = price
        self.quantity = quantity
        
        #Actions to be performed.
        Item.allItems.append(self)

    def calc_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.discount
        
    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 30)
item4 = Item("Mouse", 25, 12)
item5 = Item("Keyboard", 50, 15)

print(Item.allItems)