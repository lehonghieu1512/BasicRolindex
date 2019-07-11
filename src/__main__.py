from flask import Flask, request, jsonify
from src.models.Order import Order
app = Flask(__name__)


@app.route('/retrieve/<_id>')
def order_get(_id):
    order = Order.get(_id)
    return jsonify(order.__dict__)

@app.route('/create', methods=['GET', 'POST'])
def order_create():
    args = request.args.to_dict()
    Order.create(**args).save()
    return 200

if __name__ == '__main__':
    app.run()