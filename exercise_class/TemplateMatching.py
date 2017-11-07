import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = 0;
    var_t = 0;
    location = [0, 0];
    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------ 
    mean_t,var_t=cv2.meanStdDev(temp)

    max_corr = 0;
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s = 0;
            var_s = 0;
            corr = 0;
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------ 
            mean_window=np.mean(src[i:i+temp.shape[0],j:j+temp.shape[1]])
            var_window=np.var(src[i:i+temp.shape[0],j:j+temp.shape[1]])
            
            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------ 
            mul=(src[i:i+temp.shape[0],j:j+temp.shape[1]]-mean_t)*(temp-mean_t)
            sum_val=sum(sum(mul[i])for i in range(len(mul)))
            corr=(1/float((temp.shape[0])*(temp.shape[1])))*sum_val/((var_t)*(var_window))
            if corr > max_corr:
                max_corr = corr;
            location = [i, j];
    return location


# load source and template images
source_img = cv2.imread('/Users/wangmengxi/Documents/mercy/ec601/openCV/source.jpg',0) # read image in grayscale
temp = cv2.imread('/Users/wangmengxi/Documents/mercy/ec601/openCV/template.jpg',0) # read image in grayscale
location = TemplateMatching(source_img, temp, 20);
print(location)
match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)
# Draw a red rectangle on match_img to show the template matching result
# ------------------ Put your code below ------------------ 
cv2.rectangle(match_img,(location[1]-temp.shape[1]/2,location[0]-temp.shape[0]/2),(location[1]+temp.shape[1]/2,location[0]+temp.shape[0]/2),(0,0,255),3)

# Save the template matching result image (match_img)
# ------------------ Put your code below ------------------ 
cv2.imwrite("/Users/wangmengxi/Documents/mercy/ec601/openCV/match_img.jpg",match_img)

# Display the template image and the matching result
#cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
#cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
#cv2.imshow('TemplateImage', temp)
#cv2.imshow('MyTemplateMatching', match_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
