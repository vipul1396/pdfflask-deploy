from flask import Flask,render_template,url_for
import os
app = Flask(__name__,static_url_path="",static_folder="",template_folder="/home/vipul/Documents/pdfflask-deploy/templates")
global directory
path = '/ram'
directory = os.listdir(path)
s="ram/"
li=[]
for var in directory:
    li.append(s+var)
@app.route("/")
def home():
    return render_template('test.html', li=li,value=len(li))
if(__name__=="__main__"):
    app.run()
