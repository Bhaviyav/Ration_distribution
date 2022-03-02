from flask import Flask,render_template,session,request
from DBConnection import Db
app = Flask(__name__)
import datetime
db=Db()
app.secret_key="tocs"




@app.route('/')
def home():
    return render_template("index.html")


@app.route('/qr')
def qrtemplateload():
    return render_template("admin/qr_scanner.html")


@app.route('/view')
def view_details():
    qry = db.select("select * from details")
    return render_template("admin/view_page.html",data=qry)






#import cv2
#import numpy as np
#import pyzbar.pyzbar as pyzbar

#cap=cv2.ViedioCapture(0)
#font=cv2.FONT_HERSHEY
#while True:
   # _,frame=cap.read()
    #decodeObjects=pyzbar.decode(frame)
    #for obj in decodeObjects:
       # cv2.putText(frame,str(obj.data),(50,50),font,2,(255,0,0),3)
#Remove #

#@app.route('/view_details')
#def view_details():
    #qry=db.select("select * from details")
    #return render_template("admin/view_page.html",data=qry)

if __name__ == '__main__':
    app.run(debug=True)