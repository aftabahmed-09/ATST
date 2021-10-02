import cv2
import random

def frames(type,address):
    if type==0:
        cap=cv2.VideoCapture(address)
    if type==1:
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    i=0
    j=0
    while(cap.isOpened()):
            flag,frame=cap.read()
            if flag==False:
                break    
            if j%350==0:          
                cv2.imwrite('luci'+str(i)+'.jpg',frame)
                i+=1
            j+=1
    cap.release()

frames(0,r"C:\Users\AQEEL\Desktop\Aqeel\sem-5\MP\sample videos\luci.mp4")
cv2.destroyAllWindows()
