import cv2
import numpy as np
def attack_m(img,type):  
        
    if type == "ori":  
        return img 

    if type == "blur":  
        kernel = np.ones((5,5),np.float32)/25
        return cv2.filter2D(img,-1,kernel)

        
    if type=="rotate45":
        rows, cols, _ = img.shape
        M = cv2.getRotationMatrix2D(center=(cols / 2, rows / 2), angle=45, scale=1)
        return cv2.warpAffine(img, M, (cols, rows))
        
                
    if type=="cut_height":
        img_shape= img.shape
        height=int(img_shape[0]*0.8)
        return img[:height:,:]
    
    if type=="cut_width":
        img_shape= img.shape
        width=int(img_shape[1]*0.8)
        return img[:,:width,:]


    # if type == "gray":
    #     return  cv2.imread(fname,cv2.IMREAD_GRAYSCALE)    

    if type == "redgray":
        return  img[:,:,0]

    if type == "saltnoise":  
        for k in range(1000):
            i = int(np.random.random() * img.shape[1])
            j = int(np.random.random() * img.shape[0])
            if img.ndim == 2:
                img[j, i] = 255
            elif img.ndim == 3:
                img[j, i, 0] = 255
                img[j, i, 1] = 255
                img[j, i, 2] = 255
        return img

    # if type == "vwm":
    #     vwm = script.VisWatermark 
    #     mark =  cv2.imread('./data/wm.png')  
    #     params = {}
    #     params['position']      = (30,30)
    #     img =vwm.watermark_image(img, mark, params)
    #     return img


    if type == "randline":  
        cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
        cv2.rectangle(img,(0,0),(300,128),(255,0,0),3)
        cv2.line(img,(0,0),(511,511),(255,0,0),5)
        cv2.line(img,(0,511),(511,0),(255,0,255),5)
        
        return img

    if type == "cover":  
        cv2.circle(img,(256,256), 63, (0,0,255), -1)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Just DO it ',(10,500), font, 4,(255,255,0),2)
        return img


    if type == "brighter10":  
        w,h = img.shape[:2]
        for xi in range(0,w):
            for xj in range(0,h):
                img[xi,xj,0] = int(img[xi,xj,0]*1.1)
                img[xi,xj,1] = int(img[xi,xj,1]*1.1)
                img[xi,xj,2] = int(img[xi,xj,2]*1.1)
        return img

    if type == "darker10":  
        w,h = img.shape[:2]
        for xi in range(0,w):
            for xj in range(0,h):
                img[xi,xj,0] = int(img[xi,xj,0]*0.9)
                img[xi,xj,1] = int(img[xi,xj,1]*0.9)
                img[xi,xj,2] = int(img[xi,xj,2]*0.9)
        return img


    if type == "largersize":  
        w,h=img.shape[:2]
        return cv2.resize(img,(int(h*1.5),w))

    if type == "smallersize":  
        w,h=img.shape[:2]
        return cv2.resize(img,(int(h*0.5),w))

    return img
attack_method=('ori','blur','rotate45','cut_height','cut_width','saltnoise','randline','cover','brighter10','darker10','largersize','smallersize')

#?????????????????????
# attack_list ={}
# attack_list['ori']          = '??????'
# attack_list['blur']         = '??????'
# attack_list['rotate180']    ='??????180???'
# attack_list['rotate90']     = '??????90???'
# attack_list['chop5']        = '?????????5%'
# attack_list['chop10']       = '?????????10%'
# attack_list['chop30']       = '?????????30%'
# attack_list['saltnoise']    ='????????????'
# attack_list['vwm']          = '???????????????'
# attack_list['randline']     = '????????????'
# attack_list['cover']        = '????????????'
# attack_list['brighter10']   = '????????????10%'
# attack_list['darker10']     = '????????????10%'
# attack_list['largersize']   = '????????????'
# attack_list['smallersize']  = '????????????'