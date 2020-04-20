from flask import Flask,render_template,url_for
import os
path1 = os.getcwd() + "//templates"
app = Flask(__name__,static_url_path="",static_folder="",template_folder=path1)
global directory
path = os.getcwd() + "//ram"
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
