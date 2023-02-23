class Item:
    pay_rate = 0.8 #the pay rate after  discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater or equal to zero'
        assert quantity >= 0, f'Quantity {quantity} is not greater or equal to zero'

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Action to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    
        
phone = Item('Iphone', 65000, 5)
laptop = Item('MacBook', 144000, 3)
cable = Item('usb type-c', 440, 10)
mouse = Item('Logitech', 900, 20)
keybord = Item('Razor', 4999, 2)

print(Item.all)
for instance in Item.all:
    print(instance.name)

# phone.apply_discount()
# print(phone.price)
# laptop.pay_rate = 0.7
# laptop.apply_discount()
# print(laptop.price)

# print(phone.name)
# print(laptop.name)

# print(phone.price)
# print(laptop.price)

# print(phone.quantity)
# print(laptop.quantity)

# print(phone.calculate_total_price())
# print(laptop.calculate_total_price())

# print(Item.pay_rate)
# print(Item.__dict__) # All the attributes for class level
# print(phone.__dict__) # All the attributes for instance level