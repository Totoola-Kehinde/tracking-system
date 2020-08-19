from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required

class trackingForm(FlaskForm):
    trackingNumber = StringField("Paste Tracking Number", [data_required()])
    submit = SubmitField("Track Now!")