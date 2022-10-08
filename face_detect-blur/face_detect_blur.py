import cv2



#Press q or ESC to close program
#press s to save Face Blured Image


if __name__=="__main__":
    
    #load cascade
    faceCascade = cv2.CascadeClassifier('../data/haarcascades/haarcascade_frontalface_default.xml')
    
    #Capture video
    cap = cv2.VideoCapture(0)
    
    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read() #read frames
        
        #detect face 
        faces = faceCascade.detectMultiScale(frame,1.2,4)
        
        if faces == ():
            cv2.putText(frame,'No Face Found!',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255))
        
        for (x, y, w, h) in faces:
            # To make a face blurred
            ROI = frame[y:y+h, x:x+w]
            blur = cv2.GaussianBlur(ROI, (91,91),0)  # control Gaussian blur 
            # Insert ROI back into image
            frame[y:y+h, x:x+w] = blur

            #Put bounding box 
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)
            
            # cv2.putText(frame,'Press s to save!',(20,20),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0))
            
            
        cv2.imshow('frame', frame)
        
        k = cv2.waitKey(1)
        if k == 27 or k == ord('q'):         # wait for ESC key or q to exit
           break
        elif k == ord('s'): # wait for 's' key to save and exit
            cv2.imwrite('./out/blur_face_image_'+str(count)+'.png',frame)
            cv2.destroyAllWindows()
                
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        
        count +=1
    
    #Release camera
    cap.release()
    # Close all windows
    cv2.destroyAllWindows()
