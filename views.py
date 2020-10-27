import flask
from . import app
from .models import products

# "/search/by-category/kitchen":
# returns list of all products whose category is kitchen or technology

@app.route("/search/by_category/<category>")
def product_by_id(category):
    for product in products:
        if product['category']== category: # Case insensitive
           break
    else:
        return "product not found"
    return flask.render_template("product_by_category.html", product=product)


# "/product/1" - returns the product thats equal to 1
#use Python's built in filter() function to perform these searches
@app.route("/search/by-name/<name>")
def product_by_name(name):
    for product in products:
        if product['name']== name: # Case insensitive
           break
    else:
        return "product not found"
    return flask.render_template("product_by_name.html", product=product)
