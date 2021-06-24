from flask import Flask, render_template


app = Flask(__name__, template_folder= 'templets')

@app.route('/')
def homepage():
    return render_template('homepage.html')
    
@app.route('/products')
def product_page():
    return "render_template('homepage')"


if __name__ == '__main__':
      app.run(debug=True, port=5000)