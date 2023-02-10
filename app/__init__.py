from flask import Flask, render_template, redirect
from .config import Config
from .shipping_form import ShippingForm

app = Flask(__name__)

app.config.from_object(Config)

@app.route("/")
def index():
    return render_template("package_status.html")

@app.route("/new_package", methods=["GET", "POST"])
def packageForm():
    form = ShippingForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template("shipping_request.html", form=form)