import cv2
import time
import numpy as np
import ssl
from os import walk
from flask import Flask, render_template, Response, url_for, send_file, make_response

ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)

url = 'http://10.0.0.101:8080/video'

@app.route("/")
def home():
    
    files = next(walk("templates/takes"), (None, None, []))[2]
    print(files)
    return render_template('home.html', files=files)



def original(): 
    video = cv2.VideoCapture(0)
    
    while True:
        video.open(url)    

        b , frame = video.read()

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        canny=cv2.Canny(cv2.GaussianBlur(gray,(11,11),0),30,150,3)
        dilated=cv2.dilate(canny,(1,1),iterations=2)
        (Cnt,_)=cv2.findContours(dilated.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame,Cnt,-1,(0,255,0),2)

        convert = cv2.imencode('.jpg', frame)[1].tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + convert + b'\r\n')

def processed(): 
    video = cv2.VideoCapture(0)
    
    while True:
        video.open(url)    
        b , frame = video.read()

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        canny=cv2.Canny(cv2.GaussianBlur(gray,(11,11),0),30,150,3)
        dilated=cv2.dilate(canny,(1,1),iterations=2)
        (Cnt,_)=cv2.findContours(dilated.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame,Cnt,-1,(0,255,0),2)

        canny = cv2.putText(
            img = canny,
            text = 'Objetos: '+str(len(Cnt)),
            org = (30, 50),
            fontFace = cv2.FONT_HERSHEY_DUPLEX,
            fontScale = 0.75,
            color = (255, 255, 255)
        )
        convert = cv2.imencode('.jpg', canny)[1].tobytes()
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + convert + b'\r\n')


@app.route("/live")
def live():
    return Response(original(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route("/livecanny")
def livecanny():
    return Response(processed(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/takes/<path>')
def view_takes(path):
    print(path)
    filename = "templates/takes/" + path
    return send_file(filename, mimetype='image/gif')
    

@app.route('/saved/<path>')
def view_processed(path):
    print(path)
    filename = "templates/takes/" + path

    
    frame = cv2.imread(filename, cv2.COLOR_BGR2GRAY)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canny=cv2.Canny(cv2.GaussianBlur(gray,(11,11),0),30,150,3)
    dilated=cv2.dilate(canny,(1,1),iterations=2)
    (Cnt,_)=cv2.findContours(dilated.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame,Cnt,-1,(0,255,0),2)

    canny = cv2.putText(
        img = canny,
        text = 'Objetos: '+str(len(Cnt)),
        org = (30, 50),
        fontFace = cv2.FONT_HERSHEY_DUPLEX,
        fontScale = 0.75,
        color = (255, 255, 255)
    )
    convert = cv2.imencode('.jpg', canny)[1].tobytes()
    retval, buffer = cv2.imencode('.jpg', canny)
    response = make_response(buffer.tobytes())
    response.headers['Content-Type'] = 'image/png'
    return response

@app.route("/take")
def take():
    video = cv2.VideoCapture(0)
    video.open(url)    
    b, frame = video.read()
    while b == False: 
        b, frame = video.read()

    cv2.imwrite("templates/takes/%d.jpg" % time.time(), frame) 
    return "Ok"

app.run(debug=True, host="0.0.0.0")
