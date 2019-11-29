#!/bin/env python3
import OPi.GPIO as GPIO
from time import sleep
from flask import Flask, render_template
import atexit

# setup the gpio
GPIO.setboard(GPIO.PCPCPLUS)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

GPIO.output(19, 0)

p = GPIO.PWM(13, 1000)
p.start(0)

app = Flask(__name__)

@app.route('/')
def hello():
	return '<a href="/home">here</a>'

@app.route('/home/')
@app.route('/home/<auto_update>')
def home(auto_update=None):
    return render_template('index.html', no_update=auto_update)
	
@app.route('/set/<int:value>')
def set(value):
    try:
        p.ChangeDutyCycle(value)
        return "Value: %d" % (value)
    except:
        return "Error"

#clean up on exit
def cleanup():
    p.stop()
    GPIO.output(13, 0)
    GPIO.cleanup()

atexit.register(cleanup)
