from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/produk')
def produk():
    return render_template("PRODUK.html")

if __name__=="__main__":
    app.run(debug=True)