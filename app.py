import datetime
import csv

from flask import Flask, redirect, url_for, request, render_template, redirect
from flask_restful import Api, Resource
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)
api = Api(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/washing-machine', methods=['GET'])
def washingMachine():
    return render_template('washingMachine.html')


class Save_CSV(Resource):

    def post(self):

        _hardware = request.form.get('hardware')
        _software = request.form.get('software')
        _timestamp = datetime.datetime.now()

        fieldnames = ['hardware', 'software', 'time']

        with open('nameList.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {'hardware': _hardware, 'software': _software, 'time': _timestamp})

        return redirect(url_for('washingMachine'))


api.add_resource(Save_CSV, "/save")


if __name__ == '__main__':
    app.run(debug=True)
