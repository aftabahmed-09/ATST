import cv2
import random
import vehicle_counting
from PIL import Image

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
                add='luci'+str(i)+'.jpg'
                cv2.imwrite(add,frame)
                img_addr=rf"C:/Users/AQEEL/Desktop/Aqeel/sem-5/MP/new/drive/{add}" 
                vehicle_counting.count(img_addr)
                i+=1
                
            j+=1
    cap.release()

frames(1,r"C:\Users\AQEEL\Desktop\Aqeel\sem-5\MP\sample videos\luci.mp4")
cv2.destroyAllWindows()
