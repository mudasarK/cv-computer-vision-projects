import cv2
from PIL import Image

def getStrid(split_size, overlap=0):
    return int(split_size * (1-overlap))
    

# it will give starting point
def coordinates(size, split_size, overlap=0):
    
    points = [0]
    stride = getStrid(split_size, overlap)
    counter = 1
    while True:
        pt = stride * counter
        if pt + split_size >= size:
            points.append(size - split_size)
            break
        else:
            points.append(pt)
        counter += 1
    return points



if __name__=="__main__":
    
    
    
    path_to_img = "./images/pikachu.jpg"
    
    split_width = 150
    split_height = 150
    
    img = cv2.imread(path_to_img)
    img_h, img_w, _ = img.shape
    
    #First compute split Points
    X_points = coordinates(img_w, split_width, 0.3)
    Y_points = coordinates(img_h, split_height, 0.3)

    countX = 0
    countY = 0
    name = './out/splitted_'
    frmt = 'jpeg'
    
    #Create new Image to append splited Images
    sizePointX = len(X_points)
    sizePointY = len(Y_points)
    strideX = int(getStrid(split_width, 0.3) / 10)
    strideY = int(getStrid(split_height, 0.3) / 10)
    new_im = Image.new('RGB', (split_width*sizePointX+(strideX*sizePointX),  split_height*sizePointY+(strideY*sizePointY) ), (250,250,250))
    
    for y in Y_points:
        countX = 0
        for x in X_points:
            
            split = img[y:y+split_height, x:x+split_width]
            #cv2.imwrite('{}_{}_{}.{}'.format(name, countY, countX, frmt), split)
            #patch split image onto new image 
            new_im.paste( Image.fromarray(split), ((split_width*countX)+(strideX*countX), (split_height*countY)+(strideY*countY)) )
            countX += 1
        countY += 1
            
        
            
    new_im.show()
    new_im.save('{}_.{}'.format(name, frmt))