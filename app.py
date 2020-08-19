import os
from flask import Flask, render_template, redirect, url_for, request, sessions
from controllers.generatetrackingnum import GenerateTrackingNumber
from repository.packages import packages
from models.package import package
from views.packageform import packageForm
from views.trackingform import trackingForm
import json
import settings


app = Flask(__name__)
app.secret_key = settings.secret_key

packagecontroller = packages()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = trackingForm()
    
    # GET Request
    if request.method == 'GET':
        return render_template('index.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit():
            trackingnumber = form.trackingNumber.data
            packageitem = packagecontroller.read(trackingnumber)
            return render_template('tracking.html', form=form, packageitem=packageitem)


@app.route('/post-package', methods=['GET', 'POST'])
def postpackage():
    form = packageForm()
    if request.method == 'GET':
        
        return render_template('post-package.html', form=form)

    if request.method == 'POST':
        trackingnum = None
        if form.validate_on_submit():
            packagename = form.packagename.data
            location = form.location.data
            status = form.status.data
            quantity = form.quantity.data
            trackingnum = GenerateTrackingNumber.gettracknumber(GenerateTrackingNumber)

            singlePackage = package(None, packagename, location, status, quantity, trackingnum)
            packagecontroller.create(singlePackage)
            return render_template('post-package.html', form=form, trackingnum=trackingnum)

if __name__ == "__main__":
    app.run(debug=True)