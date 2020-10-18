import cv2
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
car_img=cv2.imread(r"vehicle1.jpg",1)
 /////////////

cascade=cv2.CascadeClassifier(r"haar_Cascade.xml")
car_plates=cascade.detectMultiScale(car_img,1.25,5)
/////////////////////


for (x,y,w,h) in car_plates:
    cv2.rectangle(car_img,(x,y),(x+w,y+h),(0,255,0),2)
    break
    
crop_img = car_img[y:y+h, x:x+w]

///////////////

grayImage = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 110, 200, cv2.THRESH_BINARY)

///////////////////
car_text = pytesseract.image_to_string(blackAndWhiteImage,config='--psm 11 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
print("Detected license plate Number is:",car_text)
text_height, text_width= grayImage.shape
print("Plate dimensions:",text_height,"x", text_width)

///////////////////
boxes=pytesseract.image_to_boxes(blackAndWhiteImage)


///////////
def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1 
letters=Convert(text)



previous,count=0,0

//////////////

for s in boxes.splitlines():
    s=s.split(' ')
    if(s[0]==letters[count]):
        x2,y2,w2,h2=int(s[1]),int(s[2]),int(s[3]),int(s[4])
        cv2.rectangle(crop_img,(x2,text_height-y2),(w2,text_height-h2),(0,0,255),1)
        
        ////////////////////
    
        print(s[0],":- Height:",(text_height-y2)-(text_height-h2)," Width:",(w2-x2)," Space:",(x2-previous))
        previous=w2
        count+=1
  ////////////////////////
                
        
            
        continue
        
    
cv2.imshow("window",crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
