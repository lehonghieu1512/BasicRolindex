from src.models.Base import Base

class Order(Base):

    def __init__(self):
        self.name = None
        self.quantity = None
        
# Order.create(index = '4', name = "dddd", quantity = 32).save()
# print(Order.get('4').__dict__)