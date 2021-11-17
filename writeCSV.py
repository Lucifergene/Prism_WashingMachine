# ================================================ #
# This file contains the methods to save the Form Data into the CSV files.
# Each Class corresponds to a particular item.
# The form details are fetched from the HTML file and are saved in a CSV File.
# ================================================ #

import datetime
import os
import csv

from flask import Flask, redirect, url_for, request, render_template, redirect, send_file
from flask_restful import Resource
from datetime import timedelta


# === Washing Machine === #
class Save_WashingMachine_CSV(Resource):

    def post(self):

        _powerRating = request.form.get('power')
        _type = request.form.get('type')

        _model = request.form.get('model')
        _capacity = request.form.get('capacity')
        _bodyColor = request.form.get('body-color')
        _panelDisplay = request.form.get('panel-display')

        _specialFeature = request.form.getlist('sp-feature')

        _drumType = request.form.get('drum-type')
        _motor = request.form.get('motor')
        _spinSpeed = request.form.get('spin-speed')
        _errorCodes = request.form.get('error-codes')

        _connectionType = request.form.getlist('connection-type')
        _displayLanguage = request.form.get('display-lang')
        _speechLanguage = request.form.get('speech-lang')

        _timestamp = datetime.datetime.now()

        fieldnames = ['Power Rating', 'Type', 'Model', 'Capacity', 'Body Color', 'Panel Display',
                      'Special Feature', 'Drum Type', 'Motor', 'Spin Speed', 'Error Codes', 'Connection Type', 'Display Language', 'Speech Language', 'Timestamp']

        with open('washing-machine.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {'Power Rating': _powerRating,
                 'Type': _type,
                 'Model': _model,
                 'Capacity': _capacity,
                 'Body Color': _bodyColor,
                 'Panel Display': _panelDisplay,
                 'Special Feature': _specialFeature,
                 'Drum Type': _drumType,
                 'Motor': _motor,
                 'Spin Speed': _spinSpeed,
                 'Error Codes': _errorCodes,
                 'Connection Type': _connectionType,
                 'Display Language': _displayLanguage,
                 'Speech Language': _speechLanguage,
                 'Timestamp': _timestamp
                 })

        return redirect(url_for('washingMachine'))


# === Air Conditioner === #
class Save_AirConditioner_CSV(Resource):

    def post(self):

        _powerRating = request.form.get('power')
        _type = request.form.get('type')

        _model = request.form.get('model')
        _capacity = request.form.get('capacity')
        _bodyColor = request.form.get('body-color')

        _specialFeature = request.form.getlist('sp-feature')

        _connectionType = request.form.getlist('connection-type')
        _displayLanguage = request.form.get('display-lang')
        _speechLanguage = request.form.get('speech-lang')

        _timestamp = datetime.datetime.now()

        fieldnames = ['Power Rating', 'Type', 'Model', 'Capacity', 'Body Color',
                      'Special Feature', 'Connection Type', 'Display Language', 'Speech Language', 'Timestamp']

        with open('air-conditioner.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {'Power Rating': _powerRating,
                 'Type': _type,
                 'Model': _model,
                 'Capacity': _capacity,
                 'Body Color': _bodyColor,
                 'Special Feature': _specialFeature,
                 'Connection Type': _connectionType,
                 'Display Language': _displayLanguage,
                 'Speech Language': _speechLanguage,
                 'Timestamp': _timestamp
                 })

        return redirect(url_for('airConditioner'))


# === AI Speaker === #
class Save_AiSpeaker_CSV(Resource):

    def post(self):

        _farField = request.form.get('far-field')
        _bodyColor = request.form.get('body-color')

        _connectionType = request.form.getlist('connection-type')
        _speechLanguage = request.form.get('speech-lang')

        _currentMode = request.form.get('current-mode')
        _wifiConnected = request.form.get('wifi-conn')
        _bluetoothConnected = request.form.get('bluetooth-conn')
        _internetAvailablity = request.form.get('int-avail')
        _currentspeechLanguage = request.form.get('current-speech-lang')

        _timestamp = datetime.datetime.now()

        fieldnames = ['Far Field Voice Processing', 'Body Color', 'Connection Type',
                      'Speech Language', 'Current Mode', 'Wifi Connected', 'Bluetooth Connected', 'Internet Availablity', 'Current Speech Language', 'Timestamp']

        with open('ai-speaker.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {'Far Field Voice Processing': _farField,
                 'Body Color': _bodyColor,
                 'Connection Type': _connectionType,
                 'Speech Language': _speechLanguage,
                 'Current Mode': _currentMode,
                 'Wifi Connected': _wifiConnected,
                 'Bluetooth Connected': _bluetoothConnected,
                 'Internet Availablity': _internetAvailablity,
                 'Current Speech Language': _currentspeechLanguage,
                 'Timestamp': _timestamp
                 })

        return redirect(url_for('aiSpeaker'))


# === Watch === #
class Save_Watch_CSV(Resource):

    def post(self):

       # ==================================
       # Pull the form data into here & push it into the CSV.
       # ==================================

        _bodycolor = request.form.get('body-color')
        _timestamp = datetime.datetime.now()
        _currentMode = request.form.get('current-mode')
        _connectionType = request.form.getlist('connection-type')
        _dispLang = request.form.get('display-lang')
        _speechLang = request.form.get('speech-lang')

        fieldnames = ['Body Color', 'Current Mode', 'Connection Type',
                      'Display Lang', 'Speech Lang', 'Timestamp']

        with open('watch.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {

                    'Body Color': _bodycolor,
                    'Current Mode': _currentMode,
                    'Connection Type': _connectionType,
                    'Display Lang': _dispLang,
                    'Speech Lang': _speechLang,
                    'Timestamp': _timestamp
                })

        return redirect(url_for('watch'))


# === Mobile === #
class Save_Mobile_CSV(Resource):

    def post(self):

        # ==================================
        # Pull the form data into here & push it into the CSV.
        # ==================================
        _spen = request.form.get('s-pen')
        _bodycolor = request.form.get('body-color')
        _timestamp = datetime.datetime.now()
        _currentMode = request.form.get('current-mode')
        _connectionType = request.form.getlist('connection-type')
        _dispLang = request.form.get('display-lang')
        _speechLang = request.form.get('speech-lang')

        fieldnames = ['S-Pen', 'Body Color', 'Current Mode',
                      'Connection Type', 'Display Lang', 'Speech Lang', 'Timestamp']

        with open('mobile.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {
                    'S-Pen': _spen,
                    'Body Color': _bodycolor,
                    'Current Mode': _currentMode,
                    'Connection Type': _connectionType,
                    'Display Lang': _dispLang,
                    'Speech Lang': _speechLang,
                    'Timestamp': _timestamp
                })

        return redirect(url_for('mobile'))


# === Microwave === #
class Save_Microwave_CSV(Resource):

    def post(self):

        _powerRating = request.form.get('power')
        _type = request.form.get('type')

        _model = request.form.get('model')
        _capacity = request.form.get('capacity')
        _bodyColor = request.form.get('body-color')
        _controlMethod = request.form.get('control-method')

        _specialFeature = request.form.getlist('sp-feature')
        _errorCodes = request.form.get('error-codes')

        _connectionType = request.form.getlist('connection-type')
        _displayLanguage = request.form.get('display-lang')
        _speechLanguage = request.form.get('speech-lang')

        _timestamp = datetime.datetime.now()

        fieldnames = ['Power Rating', 'Type', 'Model', 'Capacity', 'Body Color', 'Control Method',
                      'Special Features', 'Error Codes', 'Connection Type', 'Display Language', 'Speech Language', 'Timestamp']

        with open('microwave.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {

                    'Power Rating': _powerRating,
                    'Type': _type,
                    'Model': _model,
                    'Capacity': _capacity,
                    'Body Color': _bodyColor,
                    'Control Method': _controlMethod,
                    'Special Features': _specialFeature,
                    'Error Codes': _errorCodes,
                    'Connection Type': _connectionType,
                    'Display Language': _displayLanguage,
                    'Speech Language': _speechLanguage,
                    'Timestamp': _timestamp

                })

        return redirect(url_for('microWave'))


# === FamilyHub === #
class Save_FamilyHub_CSV(Resource):

    def post(self):

        _powerRating = request.form.get('power')
        _type = request.form.get('type')

        _model = request.form.get('model')
        _capacity = request.form.get('capacity')
        _width = request.form.get('width')
        _height = request.form.get('height')
        _depth = request.form.get('depth')
        _weight = request.form.get('weight')
        _bodyColor = request.form.get('body-color')
        
        _specialFeature = request.form.getlist('sp-feature')
        _errorCodes = request.form.get('error-codes')

        _connectionType = request.form.getlist('connection-type')
        _displayLanguage = request.form.get('display-lang')
        _speechLanguage = request.form.get('speech-lang')

        _timestamp = datetime.datetime.now()

        fieldnames = ['Power Rating', 'Type', 'Model', 'Capacity', 'Width', 'Height', 'Depth', 'Weight', 'Body Color', 'Special Feature', 'Error Codes', 'Connection Type', 'Display Language', 'Speech Language', 'Timestamp']

        with open('family-hub.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {'Power Rating': _powerRating,
                 'Type': _type,
                 'Model': _model,
                 'Capacity': _capacity,
                 'Width': _width,
                 'Height': _height,
                 'Depth': _depth,
                 'Weight': _weight,
                 'Body Color': _bodyColor,
                 'Special Feature': _specialFeature,
                 'Error Codes': _errorCodes,
                 'Connection Type': _connectionType,
                 'Display Language': _displayLanguage,
                 'Speech Language': _speechLanguage,
                 'Timestamp': _timestamp
                 })

        return redirect(url_for('familyHub'))
