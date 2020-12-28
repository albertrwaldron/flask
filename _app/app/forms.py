from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, Email

class ProductForm(FlaskForm):
    sku = StringField(
        'SKU',
        [DataRequired()]
    )

    description = StringField(
        'Description',
        [DataRequired()]
    )
    submit = SubmitField()

class CustomerForm(FlaskForm):
    first_name = StringField(
        'First Name',
        [DataRequired(), Length(max=30)]
    )
    last_name = StringField(
        'Last Name',
        [DataRequired(), Length(max=30)]
    )
    email = StringField(
        'Email',
        [DataRequired(), Email(), Length(max=50)]
    )
    phone = IntegerField(
        'Phone',
        [DataRequired(), Length(min=10,max=10)]
    )
    submit = SubmitField()

class VendorForm(FlaskForm):
    name = StringField(
        'Name',
        [DataRequired()]
    )
    submit = SubmitField()

class PurchaseForm(FlaskForm):
    vendor_id = SelectField(
        'Vendor ID',
        [DataRequired()]
    )
    submit = SubmitField()

class SaleForm(FlaskForm):
    customer_id = SelectField(
        'Customer ID',
        [DataRequired()]
    )
    submit = SubmitField()

class PurchaseLineItemForm(FlaskForm):
    product_id = SelectField(
        'Product Id',
        [DataRequired()]
    )
    purchase_id = SelectField(
        'Purchase Id',
        [DataRequired()]
    )
    quantity = IntegerField(
        'Quantity',
        [DataRequired()]
    )
    submit = SubmitField()

class SaleLineItemForm(FlaskForm):
    product_id = SelectField(
        'Product Id',
        [DataRequired()]
    )
    sale_id = SelectField(
        'Sale Id',
        [DataRequired()]
    )
    quantity = IntegerField(
        'Quantity',
        [DataRequired()]
    )
    submit = SubmitField()