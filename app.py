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
        title = 'Princess Cruise Liners Business Tracking -  Track Your Packages'
        return render_template('index.html', form=form, title=title)

    if request.method == 'POST':
        if form.validate_on_submit():
            title = 'Tracking Details'
            trackingnumber = form.trackingNumber.data
            # Read Product from MongoDB
            packageitem = packagecontroller.read(trackingnumber)
            return render_template('tracking.html', form=form, packageitem=packageitem, title=title)


@app.route('/post-package', methods=['GET', 'POST'])
def postpackage():
    form = packageForm()
    if request.method == 'GET':
        title = 'Post A Package'
        return render_template('post-package.html', form=form, title=title)

    if request.method == 'POST':
        trackingnum = None
        if form.validate_on_submit():
            title = 'Post A Package'
            # Getting user inputs 
            packagename = form.packagename.data
            location = form.location.data
            status = form.status.data
            arrival = form.arrival.data
            quantity = form.quantity.data
            ownername = form.packageownername.data
            owneremail = form.packageowneremail.data
            address = form.address.data
            description = form.description.data

            # Generate Tracking number for product!
            trackingnum = GenerateTrackingNumber.gettracknumber(GenerateTrackingNumber)

            # Make Package from package Model
            singlePackage = package(None, packagename, location, status, arrival, quantity, trackingnum, ownername, owneremail, address, description)
            # Post Package Details to MongoDB
            packagecontroller.create(singlePackage)
            return render_template('post-package.html', form=form, trackingnum=trackingnum, title=title)

if __name__ == "__main__":
    app.run(debug=True)