#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import flask
from flask import Flask, request


class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]


def conversation(message):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    a = Stack()
    pl = []
    tl = message.split()

    for t in tl:
        if t.isdigit():
            pl.append(t)
        elif t == '(':
            a.push(t)
        elif t == ')':
            top = a.pop()
            while top != '(':
                pl.append(top)
                top = a.pop()
        else:
            while (not a.isempty()) and (prec[a.peek()] >= prec[t]):
                pl.append(a.pop())
            a.push(t)
    while not a.isempty():
        pl.append(a.pop())
    return " ".join(pl)


app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/polishcow", methods=["POST", "GET"])
def polishcow():
    text = request.form.get('message')
    result = conversation(str(text))
    return flask.render_template("polishcow.html", conversation=result)


if __name__ == "__main__":
    app.run(debug=True)