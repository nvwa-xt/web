from flask import Flask, flash, redirect, render_template, \
     request, url_for
	 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


@app.route('/index/')
@app.route('/index/<name>')
def index(name=None):
    return render_template('index.html',name=name)
  

@app.route('/hello')
def hello_world():
    return render_template('hello.html')
	
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
	

@app.route('/about')
def about():
    return render_template('about.html')
	
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('about'))
    return render_template('login.html', error=error)

@app.errorhandler(404) 
def page_not_found(error): 
    return 'sorry that is my 404'
	
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8080)