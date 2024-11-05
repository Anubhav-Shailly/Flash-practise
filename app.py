from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/cal", methods = ["GET"])
def cal():
    operation = request.json["operation"]
    number1 = request.json["number1"]
    number2 = request.json["number2"]
    if operation == "add":
        result = int(number1) + int(number2)

    elif operation == "multiply":
        result = int(number1) * int(number2)

    elif operation == "divide":
        result = int(number1) / int(number2)

    else:
        result = int(number1) - int(number2)

    return "the operation is {} and the result is {}" .format(operation, result)

if (__name__) == ('__main__'):
    app.run(debug = True)