import os
from werkzeug.utils import secure_filename
from flask import Flask , render_template ,request,Response
import vehicle_counting
import cv2

UPLOAD_FOLDER = r'C:\Users\AQEEL\Desktop\Aqeel\sem-5\MP\drive\flask\test\fol'


app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET','POST'])
def hello_world():
    return render_template('index.html')
@app.route('/display', methods=['GET'])
def hello():
    return render_template('display.html')

@app.route('/p', methods=['POST','GET'])
def frames():
    
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    i=0
    j=0
    while(cap.isOpened()):
            flag,frame=cap.read()
            if flag==False:
                break    
            if j%30==0:    
                add='luci'+str(i)+'.jpg'
                cv2.imwrite(add,frame)
                img_addr=rf"C:/Users/AQEEL/Desktop/Aqeel/sem-5/MP/flaskkkkk/{add}" 
                vehicle_counting.count(img_addr)
                i+=1
                img = cv2.imread(img_addr)
                ret, buffer = cv2.imencode('.jpg', img)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
                
            j+=1
    cap.release()
@app.route('/video_feed')
def video_feed():
    return Response(frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=="__main__":
    app.run(debug='true')