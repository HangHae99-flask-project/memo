from flask import Blueprint, render_template, request,redirect,url_for

main = Blueprint('main', __name__)

# http://localhost:5001/
@main.route('/main')
def home():
    
    cookie_value = request.cookies.get('userid')
    if cookie_value:
        return render_template('index.html')
    return redirect(url_for('main.register'))

@main.route('/')
def register():
    cookie_value = request.cookies.get('userid')
    if cookie_value:
        return redirect(url_for('main.home'))
    return render_template('page/sign_up.html')