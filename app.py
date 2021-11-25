import datetime, os, csv, time

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

@app.route('/permute', methods=['GET'])
def permute():
    return render_template('permute.html')



# === These routes download the respective CSV files of each item  === #

@app.route('/download-washing-machine', methods=['GET'])
def download_washingmachine ():
    path = "washing-machine.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before downloading');</script>"
    

@app.route('/download-air-conditioner', methods=['GET'])
def download_airconditioner ():
    path = "air-conditioner.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before downloading');</script>"

@app.route('/download-ai-speaker', methods=['GET'])
def download_aispeaker ():
    path = "ai-speaker.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before downloading');</script>"

@app.route('/download-family-hub', methods=['GET'])
def download_familyhub ():
    path = "family-hub.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before downloading');</script>"

@app.route('/download-microwave', methods=['GET'])
def download_microwave ():
    path = "microwave.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before downloading');</script>"

@app.route('/download-mobile', methods=['GET'])
def download_mobile ():
    path = "mobile.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before downloading');</script>"

@app.route('/download-watch', methods=['GET'])
def download_watch ():
    path = "watch.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before downloading');</script>"


# === These routes download the respective CSV files of each item  === #

@app.route('/permute-washing-machine', methods=['GET'])
def permute_washingmachine ():
    time.sleep(5)
    path = "./permute_output/OutputWashingMachine.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before permutating');</script>"

@app.route('/permute-air-conditioner', methods=['GET'])
def permute_airconditioner ():
    time.sleep(5)
    path = "./permute_output/OutputAC.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before permutating');</script>"

@app.route('/permute-ai-speaker', methods=['GET'])
def permute_aispeaker ():
    time.sleep(5)
    path = "./permute_output/OutputAISpeaker.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before permutating');</script>"

@app.route('/permute-family-hub', methods=['GET'])
def permute_familyhub ():
    time.sleep(5)
    path = "./permute_output/OutputFamilyHub.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before permutating');</script>"

@app.route('/permute-microwave', methods=['GET'])
def permute_microwave ():
    time.sleep(5)
    path = "./permute_output/OutputMicrowave.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before permutating');</script>"

@app.route('/permute-mobile', methods=['GET'])
def permute_mobile ():
    time.sleep(5)
    path = "./permute_output/OutputMobile.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before permutating');</script>"

@app.route('/permute-watch', methods=['GET'])
def permute_watch ():
    time.sleep(5)
    path = "./permute_output/OutputWatch.csv"
    try:
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        return "<script>alert('You need to fill up the form once before permutating');</script>"


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
