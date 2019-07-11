from flask import Flask, request
from src.models.Order import Order
app = Flask(__name__)


@app.route('/retrieve/<_id>')
def order_get(_id):
    order = Order.get(_id)
    print(order.__dict__)
    return "Hello World!"

@app.route('/create', methods=['GET', 'POST'])
def order_create():
    args = request.args.to_dict()
    Order.create(**args).save()
    return "Hello World!", 200

if __name__ == '__main__':
    app.run()