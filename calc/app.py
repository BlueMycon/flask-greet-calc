from flask import Flask, request
import operations

app = Flask(__name__)

@app.get("/add")
def add():
    """adds the arguments in the query string, a + b"""
    a, b = get_math_args(request.args)
    return str(operations.add(a, b))

@app.get("/sub")
def sub():
    """subtracts the arguments in the query string, a - b"""
    a, b = get_math_args(request.args)
    return str(operations.sub(a, b))

@app.get("/mult")
def mult():
    """multiplies the arguments in the query string, a * b"""
    a, b = get_math_args(request.args)
    return str(operations.mult(a, b))

@app.get("/div")
def div():
    """divides the arguments in the query string, a / b"""
    a, b = get_math_args(request.args)
    return str(operations.div(a, b))

def get_math_args(request_args):
    """returns a tuple of two ints, given an ImmutableMultiDict
    where a and b are integer query params"""
    return (int(request_args.get("a")), int(request_args.get("b")))

