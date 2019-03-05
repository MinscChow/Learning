from flask import Flask,request,render_template

prac_app = Flask(__name__)

@prac_app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        return render_template('prac_form.html')
    return render_template('prac_home.html')

@prac_app.route('/signin',methods = ['GET'])
def parc_form():
    return render_template('prac_form.html')

@prac_app.route('/signin',methods = ['POST'])
def prac_signok():
    username = request.form['username']
    password = request.form['password']
    if username == 'crows' and password == '123456':
        return render_template('prac_signok.html',username = username)
    return render_template('prac_form.html',message = 'Incorrect username or password', username = username)


if __name__ == '__main__':
    prac_app.run()
