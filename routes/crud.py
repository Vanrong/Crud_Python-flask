from app import app, render_template, request, redirect
from sqlalchemy import create_engine, text

# Connect to the database
engine = create_engine("mysql+mysqlconnector://root:123@localhost:3306/product_db")

# Test the connection
connection = engine.connect()


@app.route('/')
@app.route('/crud')
def crud():
    result = connection.execute(text("SELECT * FROM product"))
    return render_template('crud.html', data=result)


@app.route('/confirm_delete')
def confirm_delete():
    product_id = request.args.get('id')
    result = connection.execute(text(f"SELECT * FROM product where Id = {product_id}"))
    connection.commit()
    data = []
    for product in result:
        data.append({
            'Id': product[0],
            'Name': product[1],
            'Cost': product[2],
            'Price': product[3]
        })
    return render_template('confirm_delete.html', product=data)


@app.route('/delete')
def delete():
    product_id = request.args.get('id')
    result = connection.execute(text(f"DELETE FROM product WHERE Id = {product_id}"))
    connection.commit()
    return redirect('/crud')


@app.route('/edit')
def edit():
    product_id = request.args.get('id')
    result = connection.execute(text(f"SELECT * FROM product where Id = {product_id}"))
    data = []
    for product in result:
        data.append({
            'Id': product[0],
            'Name': product[1],
            'Cost': product[2],
            'Price': product[3]
        })
    return render_template('edit.html', product=data)


@app.route('/submit', methods=['POST'])
def submit():
    # Get form values
    name = request.form.get('name')
    cost = request.form.get('cost')
    price = request.form.get('price')
    product_id = request.form.get('id')

    result = connection.execute(
        text(f"UPDATE `product` SET Name = '{name}', Cost = {cost}, Price = {price} WHERE Id={product_id}"))
    connection.commit()

    # Redirect or return a response
    return redirect('/crud')


@app.route('/submit1', methods=['POST'])
def submit1():
    # Get form values
    name = request.form.get('name')
    cost = request.form.get('cost')
    price = request.form.get('price')

    result = connection.execute(text(f"INSERT INTO `product` (Name, Cost, Price) VALUES ('{name}', {cost}, {price})"))
    connection.commit()

    return redirect('/crud')
