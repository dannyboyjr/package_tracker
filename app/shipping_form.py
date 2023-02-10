from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField, SubmitField
from map.map import map
from wtforms.validators import DataRequired

class ShippingForm(FlaskForm):
    sender_name = StringField('Sender Name', validators=[DataRequired()])
    recipient = StringField('Recipient', validators=[DataRequired()])
    origin = SelectField("Origin", choices=list(map.keys()), default=list(map.keys())[0], validators=[DataRequired()])
    destination = SelectField("desination", choices=list(map.keys()), default=list(map.keys())[1], validators=[DataRequired()])
    express_shipping = BooleanField('Express Shipping', default=False)
    submit = SubmitField('submit')
