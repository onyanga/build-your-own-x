from flask import Flask, request, jsonify
from .models import db, Inventory, Delivery, Staff, ExtraJob, Equipment

app = Flask(__name__)

@app.route('/inventory', methods=['GET', 'POST'])
def manage_inventory():
    if request.method == 'GET':
        inventory = Inventory.query.all()
        return jsonify([{'item_name': i.item_name, 'quantity': i.quantity} for i in inventory])
    elif request.method == 'POST':
        data = request.json
        new_item = Inventory(item_name=data['item_name'], quantity=data['quantity'])
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Item added successfully'})

@app.route('/staff', methods=['GET'])
def get_staff():
    staff = Staff.query.all()
    return jsonify([{'name': s.name, 'role': s.role} for s in staff])

@app.route('/equipment', methods=['GET'])
def get_equipment():
    equipment = Equipment.query.all()
    return jsonify([{'name': e.name, 'status': e.status} for e in equipment])

if __name__ == '__main__':
    app.run(debug=True)