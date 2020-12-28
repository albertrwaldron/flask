from flask import render_template, request, url_for
from flask import current_app as app
from .forms import ProductForm, CustomerForm, VendorForm, PurchaseForm, PurchaseLineItemForm, SaleForm, SaleLineItemForm
from .models import db, Product, Customer, Vendor, Purchase, PurchaseLineItem, Sale, SaleLineItem, Inventory

@app.route('/home')
@app.route('/')
def home():
    return render_template(
        'home.html', 
        title='FOSS OMS - Al Waldron', 
        description='Free Open-Source Order Management System',
        nav=nav
    )

@app.route('/product', methods=('GET', 'POST'))
def product():
    form = ProductForm()
    # action = '/product'
    if request.method == 'POST':
        sku = request.form.get('sku')
        description = request.form.get('description')
        if sku and description:
            product = Product(
                sku=sku,
                description=description
            )
            try:
                db.session.add(product)
                db.session.commit()
                inv_item = Inventory(
                    product_id=product.id,
                    quantity=0
                )
                db.session.add(inv_item)
                db.session.commit()
                print('SUCCESS!')
            except:
                print('Database error. Make sure SKU is unique.')
    return render_template(
        'form.html',
        form=form,
        title='foo',
        # action=action,
        nav=nav,
        cols=Product.__table__.columns,
        query=Product.query.all()
    )

@app.route('/customer', methods=('GET', 'POST'))
def customer():
    form = CustomerForm()
    # action = '/customer'
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        if (first_name and 
            last_name and 
            email and 
            phone):
            customer = Customer(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone
            )
            try:
                db.session.add(customer)
                db.session.commit()
                print('customer added')
            except:
                db.session.rollback()
                print('db error')
            # db.session.add(customer)
            # db.session.commit()
    return render_template(
        'form.html',
        form=form,
        # action=action,
        nav=nav,
        cols=Customer.__table__.columns,
        query=Customer.query.all()
        )
@app.route('/vendor', methods=('GET', 'POST'))
def vendor():
    form = VendorForm()
    # action = '/vendor'
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            vendor = Vendor(
                name=name
            )
            try:
                db.session.add(vendor)
                db.session.commit()
                print('SUCCESS!')
            except:
                print('Database error. Make sure SKU is unique.')
    return render_template(
        'form.html',
        form=form,
        title='foo',
        # action=action,
        nav=nav,
        cols=Vendor.__table__.columns,
        query=Vendor.query.all()
    )


@app.route('/purchase', methods=('GET', 'POST'))
def purchase():
    form = PurchaseForm()
    form.vendor_id.choices = [(id, name) for id, name in db.session.query(Vendor.id, Vendor.name)]
    if request.method == 'POST':
        vendor_id = request.form.get('vendor_id')
        if vendor_id:
            purchase = Purchase(
                vendor_id=vendor_id
            )
            try:
                db.session.add(purchase)
                db.session.commit()
                print('SUCCESS!')
            except:
                print('Database error. Make sure SKU is unique.')
    return render_template(
        'form.html',
        form=form,
        title='foo',
        # action=action,
        nav=nav,
        cols=Purchase.__table__.columns,
        query=Purchase.query.all()
    )
@app.route('/purchase_line_item', methods=('GET', 'POST'))
def purchase_line_item():
    form = PurchaseLineItemForm()
    form.product_id.choices = [(id, name) for id, name in db.session.query(Product.id, Product.description)]
    form.purchase_id.choices = [(id[0], id[0]) for id in db.session.query(Purchase.id).all()]
    print(form.purchase_id.choices)
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        purchase_id = request.form.get('purchase_id')
        quantity = request.form.get('quantity')
        if purchase_id and product_id and quantity:
            purchase_line_item = PurchaseLineItem(
                product_id=product_id,
                purchase_id=purchase_id,
                quantity=quantity
            )
            try:
                db.session.add(purchase_line_item)
                inv_item = Inventory.query.filter_by(product_id=product_id).first()
                print(type(inv_item.quantity))
                inv_item.quantity += int(quantity)
                db.session.commit()
                print('SUCCESS!')
            except:
                
                db.session.rollback()
                print('Database error. Make sure SKU is unique.')
    return render_template(
        'form.html',
        form=form,
        title='foo',
        # action=action,
        nav=nav,
        cols=PurchaseLineItem.__table__.columns,
        query=PurchaseLineItem.query.all()
    )

@app.route('/sale', methods=('GET', 'POST'))
def sale():
    form = SaleForm()
    form.customer_id.choices = [(id, name) for id, name in db.session.query(Customer.id, Customer.last_name)]
    if request.method == 'POST':
        customer_id = request.form.get('customer_id')
        if customer_id:
            sale = Sale(
                customer_id=customer_id
            )
            try:
                db.session.add(sale)
                db.session.commit()
                print('SUCCESS!')
            except:
                print('Database error. Make sure SKU is unique.')
    return render_template(
        'form.html',
        form=form,
        title='foo',
        # action=action,
        nav=nav,
        cols=Sale.__table__.columns,
        query=Sale.query.all()
    )
@app.route('/sale_line_item', methods=('GET', 'POST'))
def sale_line_item():
    form = SaleLineItemForm()
    form.product_id.choices = [(id, name) for id, name in db.session.query(Product.id, Product.description)]
    form.sale_id.choices = [(id[0], id[0]) for id in db.session.query(Sale.id).all()]
    print(form.sale_id.choices)
    if request.method == 'POST':
        product_id = request.form.get('product_id')
        sale_id = request.form.get('sale_id')
        quantity = request.form.get('quantity')
        if sale_id and product_id and quantity:
            sale_line_item = SaleLineItem(
                product_id=product_id,
                sale_id=sale_id,
                quantity=quantity
            )
            try:
                db.session.add(sale_line_item)

                inv_item = Inventory.query.filter_by(product_id=product_id).first()
                print(type(inv_item.quantity))
                inv_item.quantity -= int(quantity)
                db.session.commit()
                print('SUCCESS!')
            except:
                
                db.session.rollback()
                print('Database error. Make sure SKU is unique.')
    return render_template(
        'form.html',
        form=form,
        title='foo',
        # action=action,
        nav=nav,
        cols=SaleLineItem.__table__.columns,
        query=SaleLineItem.query.all()
    )

@app.route('/inventory')
def inventory():
    return render_template(
        'form.html',
        nav=nav,
        cols=Inventory.__table__.columns,
        query=Inventory.query.all()
    )

with app.test_request_context():
    nav = [
        # {'name': 'Home' , 'url': url_for('home')},
        {'name': 'Product', 'url': url_for('product')},
        {'name': 'Customer', 'url': url_for('customer')},
        {'name': 'Vendor', 'url': url_for('vendor')},
        {'name': 'Purchase', 'url': url_for('purchase')},
        {'name': 'Purchase Items', 'url': url_for('purchase_line_item')},
        {'name': 'Sale', 'url': url_for('sale')},
        {'name': 'Sale Items', 'url': url_for('sale_line_item')},
        {'name': 'Inventory', 'url': url_for('inventory')}
    ]
