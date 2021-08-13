import datetime, os, csv

from flask import Flask, redirect, url_for, request, render_template, redirect, send_file
from flask_restful import Api, Resource
from datetime import timedelta
from gevent.pywsgi import WSGIServer # WSGI Server


app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)
api = Api(app)
app.debug = True


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/washing-machine', methods=['GET'])
def washingMachine():
    return render_template('washingMachine.html')

@app.route('/download', methods=['GET'])
def downloadFile ():
    path = "nameList.csv"
    return send_file(path, as_attachment=True)


class Save_CSV(Resource):

    def post(self):

        _powerRating = request.form.get('power')
        _type = request.form.get('type')

        _model = request.form.get('model')
        _capacity = request.form.get('capacity')
        _bodyColor = request.form.get('body-color')
        _panelDisplay = request.form.get('panel-display')

        _specialFeature = request.form.get('sp-feature')

        _connectionType = request.form.get('connection-type')
        _displayLanguage = request.form.get('display-lang')
        _speechLanguage = request.form.get('speech-lang')

        _timestamp = datetime.datetime.now()


        fieldnames = ['Power Rating', 'Type', 'Model' , 'Capacity' , 'Body Color' , 'Panel Display' , 'Special Feature' , 'Connection Type' , 'Display Language' , 'Speech Language' , 'Timestamp']

        with open('nameList.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {'Power Rating': _powerRating, 
                 'Type': _type,
                 'Model': _model,
                 'Capacity': _capacity,
                 'Body Color': _bodyColor,
                 'Panel Display': _panelDisplay,
                 'Special Feature': _specialFeature,
                 'Connection Type': _connectionType,
                 'Display Language': _displayLanguage,
                 'Speech Language': _speechLanguage,
                 'Timestamp': _timestamp
                 })

        return redirect(url_for('washingMachine'))


api.add_resource(Save_CSV, "/save")




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) 
    http_server = WSGIServer(('0.0.0.0', port), app)
    print(f"Flask Server Started at {str(port)}")
    http_server.serve_forever()
