#This code will use index.html in templates folder to create a card using the CSS (cascading style sheets)
from flask import Flask
from flask import render_template



app=Flask(__name__)

def styled_card(function):
    def wrapper():
        pass



@app.route('/')
def home():
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)

