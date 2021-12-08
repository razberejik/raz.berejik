from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route('/')
def main():
    print ('first redirect')
    return  redirect('/home')

@app.route('/home')
def home_func():
    print('the usage url for')
    return  redirect(url_for('raz_func'))

@app.route('/razi' )
def raz_func():
    print("instarction for the assignment is in thw pdf file ")
    return 'my first  work with flask'

if __name__ == '__main__':
    app.run()
