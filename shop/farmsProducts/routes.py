from flask import redirect, render_template, url_for, flash, request
from shop import db, app
from .models import Brand, Category
from .forms import Addproducts

@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == 'POST':
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        db.session.commit()
        flash(f'The Brand {getbrand} was added to your database', 'success')
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', brands='brands')

@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if request.method == 'POST':
        getbrand = request.form.get('category')
        brand = Category(name=getbrand)
        db.session.add(brand)
        db.session.commit()
        flash(f'The Category {getbrand} was added to your database', 'success')
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html')


@app.route('/addproduct', methods=['GET', 'POST'])
def addproduct():
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    return render_template('products/addproduct.html', title="Add product page", form=form, brands=brands, categories=categories)
