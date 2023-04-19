from flask import Flask, request

app = Flask(__name__)

@app.get("/welcome")
def welcome():
    """Returns 'welcome'"""
    return """welcome"""

@app.get("/welcome/home")
def welcome_home():
    """Returns 'welcome home'"""
    return """welcome home"""

@app.get("/welcome/back")
def welcome_back():
    """Returns 'welcome back'"""
    return """welcome back"""
