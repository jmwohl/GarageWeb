import time
from datetime import datetime
from flask import Flask, render_template, request

import RPi.GPIO as GPIO
# the pin numbers refer to the board connector not the chip
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# set up pin ?? (one of the above listed pins) as an input with a pull-up resistor
GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)
# set up pin ?? (one of the above listed pins) as an input with a pull-up resistor
GPIO.setup(18, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)


app = Flask(__name__)
CODE = '6154'


@app.route('/', methods=['GET'])
def index():
    return app.send_static_file('index.html')
    # if GPIO.input(16) == GPIO.HIGH and GPIO.input(18) == GPIO.HIGH:
    #      print("Garage is Opening/Closing")
    #      return app.send_static_file('Question.html')
    # else:
    #      if GPIO.input(16) == GPIO.LOW:
    #            print ("Garage is Closed")
    #            return app.send_static_file('Closed.html')
    #      if GPIO.input(18) == GPIO.LOW:
    #            print ("Garage is Open")
    #            return app.send_static_file('Open.html')


@app.route('/status', methods=['GET'])
def status():
    if GPIO.input(16) == GPIO.HIGH and GPIO.input(18) == GPIO.HIGH:
        print("Garage is Opening/Closing")
        return app.send("Opening/Closing")
    else:
        if GPIO.input(16) == GPIO.LOW:
            print("Garage is Closed")
            return app.send("Closed")
        if GPIO.input(18) == GPIO.LOW:
            print("Garage is Open")
            return app.send("Open")


@app.route('/button', methods=['POST'])
def Garage():
    code = request.form['code']
    # 12345678 is the Password that Opens Garage Door (Code if Password is Correct)
    if code == CODE:
        GPIO.output(7, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(7, GPIO.LOW)
        time.sleep(2)
        return 'success'

    # 12345678 is the Password that Opens Garage Door (Code if Password is Incorrect)
    if code != CODE:
        return 'failure'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
