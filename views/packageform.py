from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import data_required

class packageForm(FlaskForm):
    packagename = StringField("Input Package Name", [data_required()])
    quantity = IntegerField("Package Quantity", [data_required()])
    location = StringField("Current Location", [data_required()])
    status = StringField("Package Status", [data_required()])
    submit = SubmitField("Submit!")