from flask import Flask
from flask import request
import subprocess
import sys


app = Flask(__name__)

@app.route('/name',methods=['GET', 'POST'])
def GetName():
    cmd = "hostname"
    result = str(subprocess.check_output(cmd, shell=True))

    return(result)
