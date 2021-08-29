# ================================================ #
# This file contains the methods to save the Form Data into the CSV files.
# Each Class corresponds to a particular item.
# The form details are fetched from the HTML file and are saved in a CSV File.
# ================================================ #

import datetime, os, csv

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

        _specialFeature = request.form.get('sp-feature')

        _connectionType = request.form.get('connection-type')
        _displayLanguage = request.form.get('display-lang')
        _speechLanguage = request.form.get('speech-lang')

        _timestamp = datetime.datetime.now()


        fieldnames = ['Power Rating', 'Type', 'Model' , 'Capacity' , 'Body Color' , 'Panel Display' , 'Special Feature' , 'Connection Type' , 'Display Language' , 'Speech Language' , 'Timestamp']

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

        _specialFeature = request.form.get('sp-feature')

        _connectionType = request.form.get('connection-type')
        _displayLanguage = request.form.get('display-lang')
        _speechLanguage = request.form.get('speech-lang')

        _timestamp = datetime.datetime.now()


        fieldnames = ['Power Rating', 'Type', 'Model' , 'Capacity' , 'Body Color' , 'Special Feature' , 'Connection Type' , 'Display Language' , 'Speech Language' , 'Timestamp']

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


        _connectionType = request.form.get('connection-type')
        _displayLanguage = request.form.get('display-lang')
        _speechLanguage = request.form.get('speech-lang')

        _currentMode = request.form.get('current-mode')

        _timestamp = datetime.datetime.now()


        fieldnames = ['Far Field Voice Processing', 'Body Color' , 'Connection Type' , 'Display Language' , 'Speech Language' , 'Current Mode' ,'Timestamp']

        with open('ai-speaker.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {'Far Field Voice Processing': _farField, 
                 'Body Color': _bodyColor,
                 'Connection Type': _connectionType,
                 'Display Language': _displayLanguage,
                 'Speech Language': _speechLanguage,
                 'Current Mode':_currentMode,
                 'Timestamp': _timestamp
                 })

        return redirect(url_for('aiSpeaker'))


# === Watch === #
class Save_Watch_CSV(Resource):

    def post(self):
       
       ##==================================
       # Pull the form data into here & push it into the CSV.
       ##==================================

        _timestamp = datetime.datetime.now()


        fieldnames = ['Timestamp']

        with open('watch.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {
                 'Timestamp': _timestamp
                 })

        return redirect(url_for('watch'))


# === Mobile === #
class Save_Mobile_CSV(Resource):

    def post(self):

         ##==================================
         # Pull the form data into here & push it into the CSV.
         ##==================================

        _timestamp = datetime.datetime.now()


        fieldnames = ['Timestamp']

        with open('mobile.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {
                 'Timestamp': _timestamp
                 })

        return redirect(url_for('mobile'))


# === Microwave === #
class Save_Microwave_CSV(Resource):

    def post(self):

            ##==================================
            # Pull the form data into here & push it into the CSV.
            ##==================================

        _timestamp = datetime.datetime.now()


        fieldnames = ['Timestamp']

        with open('microwave.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {
                 'Timestamp': _timestamp
                 })

        return redirect(url_for('microwave'))


# === FamilyHub === #
class Save_FamilyHub_CSV(Resource):

    def post(self):

        _type = request.form.get('type')
        _powerRating = request.form.get('power')

        _model = request.form.get('model')
        _capacity = request.form.get('capacity')
        _dimWidth = request.form.get('dimWidth')
        _dimDepth = request.form.get('dimDepth')
        _weight = request.form.get('weight')
        _bodyColor = request.form.get('body-color')

        _familyHub = request.form.get('familyHub')
        _viewInside = request.form.get('viewInside')
        _errorCodes = request.form.get('error-codes-software')

        _smartThingSupport = request.form.get('smartThingSupport')
        _bluetooth = request.form.get('bluetooth')
        _wifi = request.form.get('wifi')
        _voiceAssistance = request.form.get('voiceAssistanct')
        _displayLangConn = request.form.get('display-lang-conn')
        _speechLangConn = request.form.get('speech-lang-conn')

        _currentMode = request.form.get('current-mode')
        _previousMode = request.form.get('previous-mode')
        _errorState = request.form.get('error-state')
        _lastOperation = request.form.get('last-operation')
        _currentOperatingTime = request.form.get('CurrOpr')
        _wifiConnected = request.form.get('wifiConnected')
        _bluetoothConnected = request.form.get('bluetoothConnected')
        _internetAvailable = request.form.get('internetAvailable')
        _displayLang = request.form.get('display-lang')
        _speechLang = request.form.get('speech-lang')

        _timestamp = datetime.datetime.now()

        fieldnames = [
            'Type', 'Power Rating', 'Model', 'Capacity', 'Width', 'Depth',
            'Weight',
            'Body Color',
            'Family Hug',
            'View Inside',
            'Error Codes',
            'Smart Things Support',
            'Bluetooth',
            'Wifi',
            'Voice Assistance',
            'Display Lang Connnection',
            'Speech Lang Connection',
            'Current Mode',
            'Previous Mode',
            'Error State',
            'Last Operation',
            'Current Operating Time',
            'Wifi Connected',
            'Bluetooth Connected',
            'Internet Available',
            'Display Lang OS',
            'Speech Lang OS',
            'Timestamp'
        ]

        with open('family-hub.csv', 'a') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow(
                {
                    'Type': _type
                    'Power Rating': _powerRating
                    'Model': _model
                    'Capacity': _capacity
                    'Width': _dimWidth
                    'Depth': _dimDepth
                    'Weight': _weight
                    'Body Color': _bodyColor
                    'Family Hug': _familyHub
                    'View Inside': _viewInside
                    'Error Codes': _errorCodes
                    'Smart Things Support': _smartThingSupport
                    'Bluetooth': _bluetooth
                    'Wifi': _wifi
                    'Voice Assistance': _voiceAssistance
                    'Display Lang Connnection': _displayLangConn
                    'Speech Lang Connection': _speechLangConn
                    'Current Mode': _currentMode
                    'Previous Mode': _previousMode
                    'Error State': _errorState
                    'Last Operation': _lastOperation
                    'Current Operating Time': _currentOperatingTime
                    'Wifi Connected': _wifiConnected
                    'Bluetooth Connected': _bluetoothConnected
                    'Internet Available': _internetAvailable
                    'Display Lang OS': _displayLang
                    'Speech Lang OS': _speechLang
                    'Timestamp': _timestamp
                 })

        return redirect(url_for('familyHub'))


