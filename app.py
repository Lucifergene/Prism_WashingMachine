import datetime, os, csv

from flask import Flask, redirect, url_for, request, render_template, redirect, send_file
from flask_restful import Api, Resource
from datetime import timedelta
from gevent.pywsgi import WSGIServer # WSGI Server

import writeCSV as write    #Contains the Methods for writing into CSV Files

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)
api = Api(app)
app.debug = True



# === These routes load the respective HTML Pages === #

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html')

@app.route('/washing-machine', methods=['GET'])
def washingMachine():
    return render_template('washingMachine.html')

@app.route('/air-conditioner', methods=['GET'])
def airConditioner():
    return render_template('AC.html')

@app.route('/ai-speaker', methods=['GET'])
def aiSpeaker():
    return render_template('AiSpeaker.html')

@app.route('/family-hub', methods=['GET'])
def familyHub():
    return render_template('FamilyHub.html')

@app.route('/microwave', methods=['GET'])
def microWave():
    return render_template('Microwave.html')

@app.route('/mobile', methods=['GET'])
def mobile():
    return render_template('Mobile.html')

@app.route('/watch', methods=['GET'])
def watch():
    return render_template('watch.html')



# === These routes download the respective CSV files of each item  === #

@app.route('/download-washing-machine', methods=['GET'])
def download_washingmachine ():
    path = "washing-machine.csv"
    return send_file(path, as_attachment=True)

@app.route('/download-air-conditioner', methods=['GET'])
def download_airconditioner ():
    path = "air-conditioner.csv"
    return send_file(path, as_attachment=True)

@app.route('/download-ai-speaker', methods=['GET'])
def download_aispeaker ():
    path = "ai-speaker.csv"
    return send_file(path, as_attachment=True)

@app.route('/download-family-hub', methods=['GET'])
def downloadFile_familyhub ():
    path = "family-hub.csv"
    return send_file(path, as_attachment=True)

@app.route('/download-microwave', methods=['GET'])
def downloadFile_microwave ():
    path = "microwave.csv"
    return send_file(path, as_attachment=True)

@app.route('/download-mobile', methods=['GET'])
def downloadFile_mobile ():
    path = "mobile.csv"
    return send_file(path, as_attachment=True)

@app.route('/download-watch', methods=['GET'])
def downloadFile_watch ():
    path = "watch.csv"
    return send_file(path, as_attachment=True)


# === These Function Definitions are in the "writeCSV.py" file === #

api.add_resource(write.Save_WashingMachine_CSV, "/save-washing-machine")
api.add_resource(write.Save_AirConditioner_CSV, "/save-air-conditioner")
api.add_resource(write.Save_AiSpeaker_CSV, "/save-ai-speaker")
api.add_resource(write.Save_FamilyHub_CSV, "/save-family-hub")
api.add_resource(write.Save_Microwave_CSV, "/save-microwave")
api.add_resource(write.Save_Mobile_CSV, "/save-mobile")
api.add_resource(write.Save_Watch_CSV, "/save-watch")




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000)) # Application Runs on 5000 PORT
    http_server = WSGIServer(('0.0.0.0', port), app)
    print(f"Flask Server Started at {str(port)}")
    print(f"http://localhost:{str(port)}")
    http_server.serve_forever()
