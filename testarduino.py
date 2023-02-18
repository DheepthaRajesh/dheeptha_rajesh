##import cv2
##
##cap=cv2.VideoCapture("test.mp4.mp4")
##
##while(cap.isOpened()):
##    ret,frame=cap.read()
##
##    frame=cv2.resize(frame,(1200,700))
##
##    cv2.imshow("video",frame)
##
##    if cv2.waitKey(10) & 0xFF== ord('q'):
##
##        break
##
##cap.release()
##cv2.destroyAllWindows()
import cv2
import serial
try:
    arduino=serial.Serial("COM5", timeout=1)
except:
    print("Check port")

rawdata=[]
count=0
decode_data = []

while count<100:
    print(arduino.readline())
    rawdata.append((arduino.readline()))
    for x in rawdata:
        decode_data.append(x.decode())
    count+=1
print(rawdata)
Location = str(r'C:\Users\ASUS\Desktop\test.mp4.mp4')
cap=cv2.VideoCapture("test.mp4")
ret,frame=cap.read()

while(cap.isOpened()):
    ret,frame=cap.read()
    
    frame=cv2.resize(frame,(1200,700))


    
    cv2.imshow("video",frame)
    if cv2.waitKey(10)& 0xFF==ord('q'):
        break

for i in rawdata:
    
    if float(i)>200:

        
        while (cap.isOpened()):
            ret,frame=cap.read(0)
            
            frame=cv2.resize(frame,(1200,700))

            print(frame.rows())
            
            cv2.imshow("video",frame)
            if cv2.waitKey(10)& 0xFF==ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()


