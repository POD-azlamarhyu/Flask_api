from flask import Flask,render_template,request,redirect,url_for
from flask import Blueprint, request, abort, jsonify

app = Flask(__name__)
@app.route("/")
def main():
    return "index page"


@app.route("/home/")
def render_home():
    resp="Response test:tuple"
    status_code="200"
    data={
        "user": "myuser",
        "email":"sample.sam@email.com",
        "nickname":"nickname"
    }
    return (resp,status_code,data)