from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from models import db, Customer, Pet
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///veterinary_crm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    """Main dashboard showing customers and pets"""
    customers = Customer.query.all()
    return render_template('index.html', customers=customers)

@app.route('/customers')
def customers():
    """List all customers"""
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@app.route('/customer/<int:customer_id>')
def customer_detail(customer_id):
    """Show customer details and their pets"""
    customer = Customer.query.get_or_404(customer_id)
    return render_template('customer_detail.html', customer=customer)

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    """Add a new customer"""
    if request.method == 'POST':
        try:
            customer = Customer(
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                email=request.form['email'],
                phone=request.form['phone'],
                address=request.form.get('address', '')
            )
            db.session.add(customer)
            db.session.commit()
            flash('Customer added successfully!', 'success')
            return redirect(url_for('customer_detail', customer_id=customer.id))
        except Exception as e:
            flash(f'Error adding customer: {str(e)}', 'error')
            db.session.rollback()
    
    return render_template('add_customer.html')

@app.route('/edit_customer/<int:customer_id>', methods=['GET', 'POST'])
def edit_customer(customer_id):
    """Edit an existing customer"""
    customer = Customer.query.get_or_404(customer_id)
    
    if request.method == 'POST':
        try:
            customer.first_name = request.form['first_name']
            customer.last_name = request.form['last_name']
            customer.email = request.form['email']
            customer.phone = request.form['phone']
            customer.address = request.form.get('address', '')
            db.session.commit()
            flash('Customer updated successfully!', 'success')
            return redirect(url_for('customer_detail', customer_id=customer.id))
        except Exception as e:
            flash(f'Error updating customer: {str(e)}', 'error')
            db.session.rollback()
    
    return render_template('edit_customer.html', customer=customer)

@app.route('/add_pet/<int:customer_id>', methods=['GET', 'POST'])
def add_pet(customer_id):
    """Add a new pet to a customer"""
    customer = Customer.query.get_or_404(customer_id)
    
    if request.method == 'POST':
        try:
            pet = Pet(
                name=request.form['name'],
                species=request.form['species'],
                breed=request.form.get('breed', ''),
                age=int(request.form['age']) if request.form.get('age') else None,
                weight=float(request.form['weight']) if request.form.get('weight') else None,
                color=request.form.get('color', ''),
                gender=request.form.get('gender', ''),
                microchip_id=request.form.get('microchip_id', ''),
                notes=request.form.get('notes', ''),
                customer_id=customer_id
            )
            db.session.add(pet)
            db.session.commit()
            flash('Pet added successfully!', 'success')
            return redirect(url_for('customer_detail', customer_id=customer_id))
        except Exception as e:
            flash(f'Error adding pet: {str(e)}', 'error')
            db.session.rollback()
    
    return render_template('add_pet.html', customer=customer)

@app.route('/edit_pet/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Edit an existing pet"""
    pet = Pet.query.get_or_404(pet_id)
    
    if request.method == 'POST':
        try:
            pet.name = request.form['name']
            pet.species = request.form['species']
            pet.breed = request.form.get('breed', '')
            pet.age = int(request.form['age']) if request.form.get('age') else None
            pet.weight = float(request.form['weight']) if request.form.get('weight') else None
            pet.color = request.form.get('color', '')
            pet.gender = request.form.get('gender', '')
            pet.microchip_id = request.form.get('microchip_id', '')
            pet.notes = request.form.get('notes', '')
            db.session.commit()
            flash('Pet updated successfully!', 'success')
            return redirect(url_for('customer_detail', customer_id=pet.customer_id))
        except Exception as e:
            flash(f'Error updating pet: {str(e)}', 'error')
            db.session.rollback()
    
    return render_template('edit_pet.html', pet=pet)

@app.route('/delete_customer/<int:customer_id>', methods=['POST'])
def delete_customer(customer_id):
    """Delete a customer and all their pets"""
    try:
        customer = Customer.query.get_or_404(customer_id)
        db.session.delete(customer)
        db.session.commit()
        flash('Customer deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting customer: {str(e)}', 'error')
        db.session.rollback()
    
    return redirect(url_for('customers'))

@app.route('/delete_pet/<int:pet_id>', methods=['POST'])
def delete_pet(pet_id):
    """Delete a pet"""
    try:
        pet = Pet.query.get_or_404(pet_id)
        customer_id = pet.customer_id
        db.session.delete(pet)
        db.session.commit()
        flash('Pet deleted successfully!', 'success')
        return redirect(url_for('customer_detail', customer_id=customer_id))
    except Exception as e:
        flash(f'Error deleting pet: {str(e)}', 'error')
        db.session.rollback()
        return redirect(url_for('index'))

# API endpoints for AJAX requests
@app.route('/api/customers', methods=['GET'])
def api_customers():
    """Get all customers as JSON"""
    customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers])

@app.route('/api/customer/<int:customer_id>', methods=['GET'])
def api_customer(customer_id):
    """Get a specific customer as JSON"""
    customer = Customer.query.get_or_404(customer_id)
    return jsonify(customer.to_dict())

@app.route('/api/pets', methods=['GET'])
def api_pets():
    """Get all pets as JSON"""
    pets = Pet.query.all()
    return jsonify([pet.to_dict() for pet in pets])

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)
