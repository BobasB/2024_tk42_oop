class Phone:
    # тут ми динамічно прибудумували які атрибути буде мати клас
    pass

class PhoneWithAttributes:
    def __init__(self, vendor, model, ram, made_in = None):
        # Цей клас має наперед визначені атрибути
        self.vendor = vendor
        self.model = model
        self.ram = ram
        self.made_in = made_in