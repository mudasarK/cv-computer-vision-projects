import cv2
import pytesseract 



#Press q or ESC to close program
#press s to save Face Blured Image



if __name__=="__main__":
    
    #load cascade
    plateCascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_russian_plate_number.xml')
    
    #Capture video
    cap = cv2.VideoCapture('../data/videos/gettyimages-95608561-640_adpp.mp4')
    
    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        plates = plateCascade.detectMultiScale(imgGray,1.1,3)
        
        for (x, y, w, h) in plates:
            area = w*h
            
            if area > 500:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
                plateRoi = frame[y:y+h,x:x+w]
                plate_rgb = cv2.cvtColor(plateRoi, cv2.COLOR_BGR2RGB)
                
                numberPlate = pytesseract.image_to_string(plate_rgb)
                
                if len(numberPlate)>=7:
                    print(numberPlate)
                    
                cv2.putText(frame,'Number Plate',(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
                cv2.imshow('ROI',plateRoi)
                
        cv2.imshow('Number Plate Detection', frame)
        
        k = cv2.waitKey(1)
        if k == 27 or k == ord('q'):         # wait for ESC key or q to exit
            break
        elif k == ord('s'): # wait for 's' key to save and exit
            cv2.imwrite('./out/blur_face_image_'+str(count)+'.png', frame)
            cv2.destroyAllWindows()
            count +=1
                
    
    #Release camera
    cap.release()
    # Close all windows
    cv2.destroyAllWindows()
