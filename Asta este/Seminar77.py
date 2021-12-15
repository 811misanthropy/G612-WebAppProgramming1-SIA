from flask import Flask

app = Flask(__name__)

@app.route("/")
def hell_world():
    return "<h1>Hello World!</h1>"

@app.route("/animal-info")
def animal_info():
    a=Animal("Ruf", 10)
    response = a.get()
    return response

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=3002)