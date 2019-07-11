import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime as dt

COLLECTION = "order"

cred = credentials.Certificate("asset/firestore_service_account.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

class Base:
    def __init__(self):
        self.time = None
        self.index = None

    @classmethod
    def create(cls, index, **d):
        
        result = cls()
        for key, value in d.items():
            setattr(result, key, value)
        setattr(result, 'time', dt.now())
        setattr(result, 'index', index)
        return result

    @classmethod
    def get(cls, index):
        if index:
            d = db.collection(COLLECTION).document(index).get().to_dict()
            return __class__.create(index, **d)


    def save(self):
        result = self.__dict__.copy()
        del result['index']
        db.collection(COLLECTION).document(self.index).set(result)

    

# class Order(Base):

#     def __init__(self):
#         self.name = None
#         self.quantity = None
        

# Order.create(index = "3", name = "abab", quantity=3123).save()
