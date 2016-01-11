import cv2
def MeanFilter(source):    
    final = source[:]
    for y in range(1,source.shape[0]-1):
    	for x in range(1,source.shape[1]-1):
            final[y,x]=source[y,x]
    cv2.imshow('Source_Picture', source) #Show the image
    members=[source[0,0]]*9
    #print(members)
    for y in range(1,source.shape[0]-1):
    	for x in range(1,source.shape[1]-1):
            members[0] = source[y-1,x-1]
	    #print(members[0])
            members[1] = source[y,x-1]
            members[2] = source[y+1,x-1]
            members[3] = source[y-1,x]
            members[4] = source[y,x]
            members[5] = source[y+1,x]
            members[6] = source[y-1,x+1]
            members[7] = source[y,x+1]
            members[8] = source[y+1,x+1]
	    
            final[y,x]=sum(members)/9
    #print(members)
    print(final)
    cv2.imshow('Denoised Image', final) #Show the image
    cv2.waitKey()
img=cv2.imread('sp_noise.jpg',0)
MeanFilter(img)
cv2.waitKey(0)
