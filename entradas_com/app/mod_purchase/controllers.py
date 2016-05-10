# Import flask dependencies
from flask import Blueprint, render_template, redirect, request, make_response
from app.models import *
from app import db

mod_purchase = Blueprint('purchase', __name__,)

@mod_purchase.route('/purchase')
def purchase():
	if 'username' in session:
		user = session['username']
		return render_template("shop/shop.html", user=user)
	else:
		return render_template("shop/shop.html")

@mod_purchase.route('/purchase/end')
def finish_purchase():
	if 'username' in session:
		user = session['username']
		return render_template("shop/end.html", user=user)
	else:
		return render_template("shop/end.html")	
