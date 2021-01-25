from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "SecretKey"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/python_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Customers(db.Model):
    CustomerID = db.Column(db.VARCHAR(5), primary_key=True)
    CompanyName = db.Column(db.VARCHAR(40))
    ContactName = db.Column(db.VARCHAR(30))
    ContactTitle = db.Column(db.VARCHAR(30))
    Address = db.Column(db.VARCHAR(60))
    City = db.Column(db.VARCHAR(15))
    Region = db.Column(db.VARCHAR(15))
    PostalCode = db.Column(db.VARCHAR(10))
    Country = db.Column(db.VARCHAR(15))
    Phone = db.Column(db.VARCHAR(24))
    Fax = db.Column(db.VARCHAR(24))

    def __init__(self, CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country,
                 Phone, Fax):
        self.CustomerID = CustomerID
        self.CompanyName = CompanyName
        self.ContactName = ContactName
        self.ContactTitle = ContactTitle
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostalCode = PostalCode
        self.Country = Country
        self.Phone = Phone
        self.Fax = Fax


class Orders(db.Model):
    OrderID = db.Column(db.INTEGER, primary_key=True)
    CustomerID = db.Column(db.VARCHAR(5))
    EmployeeID = db.Column(db.INTEGER)
    OrderDate = db.Column(db.DATETIME)
    RequiredDate = db.Column(db.DATETIME)
    ShippedDate = db.Column(db.DATETIME)
    ShipVia = db.Column(db.INTEGER)
    Freight = db.Column(db.DECIMAL(10, 4))
    ShipName = db.Column(db.VARCHAR(40))
    ShipAddress = db.Column(db.VARCHAR(60))
    ShipCity = db.Column(db.VARCHAR(15))
    ShipRegion = db.Column(db.VARCHAR(15))
    ShipPostalCode = db.Column(db.VARCHAR(10))
    ShipCountry = db.Column(db.VARCHAR(15))

    def __init__(self, OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight,
                 ShipName, ShipAddress,
                 ShipCity, ShipRegion, ShipPostalCode, ShipCountry):
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.EmployeeID = EmployeeID
        self.OrderDate = OrderDate
        self.RequiredDate = RequiredDate
        self.ShippedDate = ShippedDate
        self.ShipVia = ShipVia
        self.Freight = Freight
        self.ShipName = ShipName
        self.ShipAddress = ShipAddress
        self.ShipCity = ShipCity
        self.ShipRegion = ShipRegion
        self.ShipPostalCode = ShipPostalCode
        self.ShipCountry = ShipCountry


class Products(db.Model):
    ProductID = db.Column(db.INTEGER, primary_key=True)
    ProductName = db.Column(db.VARCHAR(40))
    SupplierID = db.Column(db.INTEGER)
    CategoryID = db.Column(db.INTEGER)
    QuantityPerUnit = db.Column(db.VARCHAR(20))
    UnitPrice = db.Column(db.DECIMAL(10, 4))
    UnitsInStock = db.Column(db.INTEGER)
    UnitsOnOrder = db.Column(db.INTEGER)
    RecorderLevel = db.Column(db.INTEGER)
    Discontinued = db.Column(db.INTEGER)

    def __init__(self, ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock,
                 UnitsOnOrder, RecorderLevel, Discontinued):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.SupplierID = SupplierID
        self.CategoryID = CategoryID
        self.QuantityPerUnit = QuantityPerUnit
        self.UnitPrice = UnitPrice
        self.UnitsInStock = UnitsInStock
        self.UnitsOnOrder = UnitsOnOrder
        self.RecorderLevel = RecorderLevel
        self.Discontinued = Discontinued


@app.route('/')
@app.route('/index')
def index():
    all_data = Customers.query.all()
    return render_template('index.html', customers=all_data)


@app.route('/order')
def order():
    all_data = Orders.query.all()
    return render_template('order.html', orders=all_data)


@app.route('/product')
def product():
    all_data = Products.query.all()
    return render_template('product.html', products=all_data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        CustomerID = request.form['CustomerID']
        CompanyName = request.form['CompanyName']
        ContactName = request.form['ContactName']
        ContactTitle = request.form['ContactTitle']
        Address = request.form['Address']
        City = request.form['City']
        Region = request.form['Region']
        PostalCode = request.form['PostalCode']
        Country = request.form['Country']
        Phone = request.form['Phone']
        Fax = request.form['Fax']

        my_customers = Customers(CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode,
                                 Country, Phone, Fax)
        db.session.add(my_customers)
        db.session.commit()

        flash("Customers added successfully")

        return redirect(url_for('index'))


@app.route('/insertorder', methods=['POST'])
def insertorder():
    if request.method == 'POST':
        OrderID = request.form['OrderID']
        CustomerID = request.form['CustomerID']
        EmployeeID = request.form['EmployeeID']
        OrderDate = request.form['OrderDate']
        RequiredDate = request.form['RequiredDate']
        ShippedDate = request.form['ShippedDate']
        ShipVia = request.form['ShipVia']
        Freight = request.form['Freight']
        ShipName = request.form['ShipName']
        ShipAddress = request.form['ShipAddress']
        ShipCity = request.form['ShipCity']
        ShipRegion = request.form['ShipRegion']
        ShipPostalCode = request.form['ShipPostalCode']
        ShipCountry = request.form['ShipCountry']

        my_orders = Orders(OrderID, CustomerID, EmployeeID, OrderDate, RequiredDate, ShippedDate, ShipVia, Freight,
                           ShipName, ShipAddress,
                           ShipCity, ShipRegion, ShipPostalCode, ShipCountry)
        db.session.add(my_orders)
        db.session.commit()

        flash("Orders added successfully")

        return redirect(url_for('order'))


@app.route('/insertproducts', methods=['POST'])
def insertproducts():
    if request.method == 'POST':
        ProductID = request.form['ProductID']
        ProductName = request.form['ProductName']
        SupplierID = request.form['SupplierID']
        CategoryID = request.form['CategoryID']
        QuantityPerUnit = request.form['QuantityPerUnit']
        UnitPrice = request.form['UnitPrice']
        UnitsInStock = request.form['UnitsInStock']
        UnitsOnOrder = request.form['UnitsOnOrder']
        RecorderLevel = request.form['RecorderLevel']
        Discontinued = request.form['Discontinued']

        my_products = Products(ProductID, ProductName, SupplierID, CategoryID, QuantityPerUnit, UnitPrice, UnitsInStock,
                               UnitsOnOrder, RecorderLevel, Discontinued)
        db.session.add(my_products)
        db.session.commit()

        flash("Products added successfully")

        return redirect(url_for('product'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_customers = Customers.query.get(request.form.get('CustomerID'))

        my_customers.CustomerID = request.form['CustomerID']
        my_customers.CompanyName = request.form['CompanyName']
        my_customers.ContactName = request.form['ContactName']
        my_customers.ContactTitle = request.form['ContactTitle']
        my_customers.Address = request.form['Address']
        my_customers.City = request.form['City']
        my_customers.Region = request.form['Region']
        my_customers.PostalCode = request.form['PostalCode']
        my_customers.Country = request.form['Country']
        my_customers.Phone = request.form['Phone']
        my_customers.Fax = request.form['Fax']

        db.session.commit()
        flash("Customer Updated Successfully")

        return redirect(url_for('index'))


@app.route('/updateorder', methods=['GET', 'POST'])
def updateorder():
    if request.method == 'POST':
        my_orders = Orders.query.get(request.form.get('OrderID'))

        my_orders.OrderID = request.form['OrderID']
        my_orders.CustomerID = request.form['CustomerID']
        my_orders.EmployeeID = request.form['EmployeeID']
        my_orders.OrderDate = request.form['OrderDate']
        my_orders.RequiredDate = request.form['RequiredDate']
        my_orders.ShippedDate = request.form['ShippedDate']
        my_orders.ShipVia = request.form['ShipVia']
        my_orders.Freight = request.form['Freight']
        my_orders.ShipName = request.form['ShipName']
        my_orders.ShipAddress = request.form['ShipAddress']
        my_orders.ShipCity = request.form['ShipCity']
        my_orders.ShipRegion = request.form['ShipRegion']
        my_orders.ShipPostalCode = request.form['ShipPostalCode']
        my_orders.ShipCountry = request.form['ShipCountry']

        db.session.commit()
        flash("Orders Updated Successfully")

        return redirect(url_for('order'))


@app.route('/updateproducts', methods=['GET', 'POST'])
def updateproducts():
    if request.method == 'POST':
        my_products = Products.query.get(request.form.get('ProductID'))

        my_products.ProductID = request.form['ProductID']
        my_products.ProductName = request.form['ProductName']
        my_products.SupplierID = request.form['SupplierID']
        my_products.CategoryID = request.form['CategoryID']
        my_products.QuantityPerUnit = request.form['QuantityPerUnit']
        my_products.UnitPrice = request.form['UnitPrice']
        my_products.UnitsInStock = request.form['UnitsInStock']
        my_products.UnitsOnOrder = request.form['UnitsOnOrder']
        my_products.RecorderLevel = request.form['RecorderLevel']
        my_products.Discontinued = request.form['Discontinued']

        db.session.commit()
        flash("Products Updated Successfully")

        return redirect(url_for('product'))


if __name__ == "__main__":
    app.run(debug=True)
