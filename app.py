from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/poem")
def poem():
    return render_template("poem/index.html")

@app.route("/poem/poem1")
def poem1():
    return render_template("poem/poem1.html")

@app.route("/poem/poem2")
def poem2():
    return render_template("poem/poem2.html")

@app.route("/poem/poem3")
def poem3():
    return render_template("poem/poem3.html")

@app.route("/poem/poem4")
def poem4():
    return render_template("poem/poem4.html")

@app.route("/poem/poem5")
def poem5():
    return render_template("poem/poem5.html")

@app.route("/poem/poem6")
def poem6():
    return render_template("poem/poem6.html")

@app.route("/poem/poem7")
def poem7():
    return render_template("poem/poem7.html")

@app.route("/poem/poem8")
def poem8():
    return render_template("poem/poem8.html")

if __name__ == "__main__":
    import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
