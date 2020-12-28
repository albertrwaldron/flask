from . import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(
        'id',
        db.Integer(),
        primary_key=True
    )
    sku = db.Column(
        db.String(20),
        unique=True
    )
    description = db.Column(
        db.String(144)
    )
    purchases = db.relationship('PurchaseLineItem', backref='products', lazy=True)
    inventory = db.relationship('Inventory', backref='products', lazy=True)

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(
        'id', 
        db.Integer(), 
        primary_key=True)
    first_name = db.Column(
        db.String(30),
        nullable=False)
    last_name = db.Column(
        db.String(30),
        nullable=False)
    email = db.Column(
        db.String(50),
        nullable=False,
        unique=True)
    phone = db.Column(
        db.BigInteger()
    )
    sales = db.relationship('Sale', backref='customers', lazy=True)
class Vendor(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(
        'id',
        db.Integer(),
        primary_key=True
    )
    name = db.Column(
        db.String(50)
    )
    purchases = db.relationship('Purchase', backref='vendor', lazy=True)
class Purchase(db.Model):
    __tablename__ = 'purchases'
    id = db.Column(
        'id',
        db.Integer(),
        primary_key=True
    )
    vendor_id = db.Column(
        db.Integer(),
        db.ForeignKey('vendor.id'),
        nullable=False
    )
    line_items = db.relationship('PurchaseLineItem', backref='purchases', lazy=True)

class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(
        'id',
        db.Integer(),
        primary_key=True
    )
    customer_id = db.Column(
        db.Integer(),
        db.ForeignKey('customers.id'),
        nullable=False
    )
    line_items = db.relationship('SaleLineItem', backref='sales', lazy=True)


class PurchaseLineItem(db.Model):
    __tablename__ = 'purchase_line_items'
    id = db.Column(
        'id',
        db.Integer(),
        primary_key=True
    )
    product_id = db.Column(
        db.Integer(),
        db.ForeignKey('products.id'),
        nullable=False
    )
    purchase_id = db.Column(
        db.Integer(),
        db.ForeignKey('purchases.id'),
        nullable=False
    )
    quantity = db.Column(
        db.Integer(),
        nullable=False
    )

class SaleLineItem(db.Model):
    __tablename__ = 'sale_line_items'
    id = db.Column(
        'id',
        db.Integer(),
        primary_key=True
    )
    sale_id = db.Column(
        db.Integer(),
        db.ForeignKey('sales.id'),
        nullable=False
    )
    product_id = db.Column(
        db.Integer(),
        db.ForeignKey('products.id'),
        nullable=False
    )
    
    quantity = db.Column(
        db.Integer(),
        nullable=False
    )

class Inventory(db.Model):
    __tablename__ = 'inventory'
    id = db.Column(
        'id',
        db.Integer(),
        primary_key=True
    )
    product_id = db.Column(
        db.Integer(),
        db.ForeignKey('products.id'),
        nullable=False,
        unique=True
    )
    quantity = db.Column(
        db.Integer(),
        nullable=False
    )