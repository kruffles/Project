__author__ = 'Keziah'

from hashlib import md5
import subprocess
import re

from PySide.QtGui import *
from PySide import QtCore
import time


global output_file
global log_file_name

#quits the application
def close_it():
    QtCore.QCoreApplication.instance().quit()

#opens the report
def view_it():
    eof_hash()
    try:
        subprocess.call(['notepad.exe', output_file])
    except:
        QMessageBox.information(None, 'WARNING!!!', 'No case file created')

#fetches the log file.txt
def get_log_file():
    global log_file_name
    log_file_name = QFileDialog.getOpenFileName(None, 'Select File for Analysis')
    hash_file(log_file_name[0])

#allows user to assign a case ID to the report
def assign_case_id():
    return QFileDialog.getSaveFileName(None, 'Please Assign Your Case ID')[0]

#hashes the log file.txt immediately
def hash_file(file_name):
    global output_file
    localtime = time.asctime(time.localtime(time.time()))
    with open(file_name, 'r') as f:
        hashFile = f.read()
        md5Hash = md5(hashFile)
        md5Hashed = md5Hash.hexdigest()
    output_file = assign_case_id()
    try:
        with open(output_file, 'a') as g:
            g.write('\n\n  ********************************************\n> PRE ANALYSIS HASH OF LOG FILE:\n\n> Log file :         {}  \n> Time of Hash :     {} \n> Hash Value :       {} \n\n  ********************************************\n\n\n'.format(file_name,localtime,md5Hashed))
        QMessageBox.information(None, 'Done', output_file + '\n\nYour case file has been successfully created!')
    except:
        QMessageBox.information(None, 'Unexpected Error', 'Please try again')

#hashes the log file.txt after every analysis
def eof_hash():
    global output_file
    localtime = time.asctime(time.localtime(time.time()))
    with open(log_file_name[0], 'r') as f:
        hashFile = f.read()
        md5Hash = md5(hashFile)
        md5Hashed = md5Hash.hexdigest()
    with open(output_file, 'a') as g:
        g.write('\n\n  *********************************************\n> POST ANALYSIS HASH OF LOG FILE:\n\n> Log file :          {}  \n> Time of Hash :      {} \n> Hash Value :        {}\n\n  *********************************************\n\n\n'.format(log_file_name[0],localtime,md5Hashed))

# identifies the strings associated with mac flood detection
def mac_flood_detection():
    macAddCount = []
    with open(output_file, 'a')as outputFile:
        with open(log_file_name[0], 'r')as inputFile:
            for line in inputFile:
                if line.startswith('Mac Entries'):
                    macAddCount = ['\n' + line]
                elif line.startswith('Total Mac Address Space Available'):
                    macAddCount.append(line + '\n')
                    outputFile.write('\n\n  ********************************************\n> MAC FLOOD ATTACK DETECTION\n\n  ********************************************\n\n')
                    outputFile.write('> Check "Total Mac Address Space Available"\n\n> CAM table exhaustion presents evidence of a MAC flood attack:\n\n')
                    outputFile.write(''.join(macAddCount))
                    macAddCount = []
                elif macAddCount:
                    macAddCount.append(line)

#identifies the strings associated with port security
def port_security():
    violation = []
    disabled = []
    secVCount = []
    with open(output_file, 'a')as outputFile:
        with open(log_file_name[0], 'r')as inputFile:
            outputFile.write('\n\n  ********************************************\n> PORT SECURITY VIOLATION\n\n  ********************************************\n\n> Log Buffer Extraction:\n\n')
            for line in inputFile:
                if line.__contains__('%PM-4-ERR_DISABLE: psecure-violation'):
                    disabled.append(line)  # each matching line is appended to the list
                    outputFile.write(line)
                elif line.__contains__('%PORT_SECURITY-2-PSECURE_VIOLATION'):
                    violation.append(line)
                    outputFile.write(line)

        outputFile.write('\n\n> Summary of Port Security Violation:\n\n\n')
        for item in violation:  #for each item in output
            time = item[:8]  #first 8 chars of line
            macAddress = item[98:112]
            ethPort = item[132:136]
            outputFile.write('Event Timestamp:                {}\nAffected Switch Port No:        {}Non-secure Mac Address:         {}'
                             '\n ------------------------\n'.format(time, ethPort, macAddress))

        outputFile.write('\n\n> Status of affected ports:\n\n')

        for item in disabled:
            portDis = item[67:70]

            outputFile.write('\nPort {} is disabled'.format(portDis))


        with open(log_file_name[0], 'r')as inputFile:
            outputFile.write('\n\n\n> Show port security output (dynamic learning configuration):\n')
            for line in inputFile:
                if line.startswith('Secure Port'):
                    secVCount = ['\n\n' + line]
                elif line.startswith('Max Addresses'):
                    secVCount.append(line + '\n')
                    outputFile.write(''.join(secVCount))
                    secVCount = []
                elif secVCount:
                    secVCount.append(line)

#identifies the time entries within the logging buffer
def timestamps():
    time_re = re.compile(r'^(([01]\d|2[0-3]):([0-5]\d)|24:00)')

    with open(output_file, 'a')as outputFile:
        with open(log_file_name[0], 'r')as inputFile:
            lines = inputFile.readlines()
            outputFile.write('\n  ********************************************\n> LOG BUFFER TIMESTAMPS\n\n  ********************************************\n\n')
            for line in lines:
                # match the regex to every line in file
                if re.match(time_re, line):
                    outputFile.write(line)

