from flask import flask, render_template, request, redirect

app = flask(_name_)

# Initialize food list and user list
food_list = []
user_list = []

# Food class to represent food items
class Food:
    def _init_(self, food_id, name, quantity, price, discount, stock):
        self.food_id = food_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

# User class to represent registered users
class User:
    def _init_(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password

# Admin functionalities
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Add new food item
        if 'add_food' in request.form:
            food_id = len(food_list) + 1 # Generate FoodID automatically
            name = request.form['name']
            quantity = request.form['quantity']
            price = float(request.form['price'])
            discount = float(request.form['discount'])
            stock = int(request.form['stock'])
            food_item = Food(food_id, name, quantity, price, discount, stock)
            food_list.append(food_item)
            return redirect('/admin')
        # Remove food item
        elif 'remove_food' in request.form:
            food_id = int(request.form['food_id'])
            for food_item in food_list:
                if food_item.food_id == food_id:
                    food_list.remove(food_item)
                    break
            return redirect('/admin')
    return render_template('admin.html', food_list=food_list)

# User functionalities
@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        # Register new user
        if 'register' in request.form:
            full_name = request.form['full_name']
            phone_number = request.form['phone_number']
            email = request.form['email']
            address = request.form['address']
            password = request.form['password']
            user = User(full_name, phone_number, email, address, password)
            user_list.append(user)
            return redirect('/user')
        # Place new order
        elif 'place_order' in request.form:
            selected_items = request.form.getlist('selected_items')
            order_list = []
            for item in selected_items:
                food_id = int(item)
                for food_item in food_list:
                    if food_item.food_id == food_id:
                        order_list.append(food_item)
                        break
            return render_template('order.html', order_list=order_list)
    return render_template('user.html', food_list=food_list)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

if _name_ == '_main_':
    app.run(debug=True)