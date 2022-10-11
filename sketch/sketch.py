import cv2


#Press q or ESC to close program
#press s to save Face Blured Image


if __name__=="__main__":
    
    #Capture video
    cap = cv2.VideoCapture(0)
    
    count = 0
    while(cap.isOpened()):
        ret, frame = cap.read() #read frames

        # change color to gray
        imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        imgGrayInv = 255-imgGray
        
        imgBlur = cv2.GaussianBlur(imgGrayInv, ksize=(21, 21),sigmaX=5, sigmaY=0)
        
        #finalImg = dodge(imgGray,imgBlur)
        finalImg = cv2.divide(imgGray,255-imgBlur,scale=256)
        
        cv2.imshow('Sketch',finalImg) # Sketched Image

        k = cv2.waitKey(1)    
        if k == 27 or k == ord('q'):         # wait for ESC key or q to exit
           break
        elif k == ord('s'): # wait for 's' key to save and exit
            cv2.imwrite('./out/sketches_image_'+str(count)+'.png',finalImg)
            cv2.destroyAllWindows()
            count +=1
            
    #Release camera
    cap.release()
    # Close all windows
    cv2.destroyAllWindows()