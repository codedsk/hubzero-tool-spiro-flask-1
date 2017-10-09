from __future__ import print_function

import numpy as np
import sys

from app import app
from flask import render_template, jsonify
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange


def debug(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def spiro(n1,n2,n3):
    t = np.linspace(0,1,1000);
    z = np.exp(1j*2*np.pi*n1*t) + np.exp(1j*2*np.pi*n2*t) + np.exp(1j*2*np.pi*n3*t)
    return (np.real(z),np.imag(z))


class SpiroForm(FlaskForm):
    n1 = IntegerField('n1', default=13,
            validators=[DataRequired(), NumberRange(min=-20, max=20)])
    n2 = IntegerField('n2', default=-7,
            validators=[DataRequired(), NumberRange(min=-20, max=20)])
    n3 = IntegerField('n3', default=-3,
            validators=[DataRequired(), NumberRange(min=-20, max=20)])


@app.route('/', methods=['GET','POST'])
def index():

    debug("received request for /")

    form = SpiroForm()

    if form.validate_on_submit():
        debug("running spiro with n1={} n2={} n3={}"
                .format(form.n1.data,form.n2.data,form.n3.data))
        (x,y) = spiro(form.n1.data,form.n2.data,form.n3.data)
        debug("returning spirograph data")
        return jsonify(x=x.tolist(), y=y.tolist())

    if len(form.errors) > 0:
        debug("processing errors: ".format(form.errors))

    # handle GET and everything else
    debug("rendering index.html")
    return render_template("index.html", form=form)
