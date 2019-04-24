#!/usr/bin/env python3

from flask import Flask, render_template, request, flash, redirect

import pingT

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/')
def homepage():
    rows = pingT.threadWrapperPing("data.csv")
    return render_template("home.html", rows = rows)


if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0")



#
