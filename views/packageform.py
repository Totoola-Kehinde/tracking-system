from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import data_required

class packageForm(FlaskForm):
    packagename = StringField("Input Package Name", [data_required()])
    packageownername = StringField("Input Package Owner Name", [data_required()])
    packageowneremail = StringField("Input Package Owner Email", [data_required()])
    quantity = IntegerField("Package Quantity", [data_required()])
    location = StringField("Current Location", [data_required()])
    status = StringField("Package Status", [data_required()])
    arrival = TextAreaField("Package Arrival Date", [data_required()])
    address = TextAreaField("Address", [data_required()])
    description = TextAreaField("Description", [data_required()])
    submit = SubmitField("Submit!")