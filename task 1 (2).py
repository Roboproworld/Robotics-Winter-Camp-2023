import cv2
import numpy as np 

path = r'C:\Users\hp\Downloads\Robotics-Winter-Camp-2023-main (1)\Robotics-Winter-Camp-2023-main\Workshop1_OpenCV\images\image.jpeg'

img = cv2.imread(path)  
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
edged = cv2.Canny(gray, 170, 255)            

ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)  

contours,hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 

for i in contours:
	M = cv2.moments(i)
	if M['m00'] != 0:
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
		cv2.drawContours(img, [i], -1, (0, 255, 0), 2)
		cv2.circle(img, (cx, cy), 7, (0, 0, 255), -1)
		cv2.putText(img, f"{cx,cy}", (cx - 40, cy - 20),
				cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
	print(f"x: {cx} y: {cy}")

#Function to determine type of polygon on basis of number of sides
def detectShape(c):          
       shape = 'unknown' 
       peri=cv2.arcLength(cnt,True) 
       vertices = cv2.approxPolyDP(cnt, 0.02 * peri, True)
       sides = len(vertices) 
       if (sides == 3): 
            shape='triangle' 
       elif(sides==4): 
             x,y,w,h=cv2.boundingRect(cnt)
             aspectratio=float(w)/h 
             if (aspectratio==1):
                   shape='square'
             else:
                   shape="rectangle" 
       elif(sides==5):
            shape='pentagon' 
       elif(sides==6):
            shape='hexagon' 
       elif(sides==8): 
            shape='octagon' 
       elif(sides==10): 
            shape='star'
       else:
           shape='circle' 
       return shape 



for cnt in contours:
    moment=cv2.moments(cnt) 
    cx = int(moment['m10'] / moment['m00']) 
    cy = int(moment['m01'] / moment['m00']) 
    shape=detectShape(cnt) 
    cv2.drawContours(img,[cnt],-1,(0,255,0),2)
    cv2.putText(img,shape,(cx-30,cy+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)  #Putting name of polygon along with the shape 
    cv2.imshow('polygons_detected',img) 

with open('myfile.txt','w') as f:
      print('Triangle_Centroid = (457,473) Hexagon_Centroid = (145,151) Rectangle_Centroid = (89,432)',file=f)


cv2.waitKey(0) 
cv2.destroyAllWindows()