import base64,struct
from operator import truediv
from PIL import Image ,ImageDraw,ImageFilter
import numpy as np
import matplotlib.pyplot as plt
import math




bmp_image =Image.open('test_1920_1080.bmp')



image_pixel=list()
for i_vertical in range(bmp_image.height):
    line_horizon=[]



    for i_horizon in range(bmp_image.width):

        line_horizon.append(bmp_image.getpixel((i_horizon,i_vertical)))
        

    image_pixel.append(line_horizon)

image_width = bmp_image.width
image_height= bmp_image.height


#縮圖

u=3
l=2
Ratio = (u/l)


subWidth =int(image_width/Ratio)
subHeight =int(image_height/Ratio)

subImage = Image.new(mode="RGB",size=(subWidth,subHeight))



regPixel = list()

idx=0
curRow=0
curCol=0

i_jump_num=1
j_jump_num=1

for i in range(subHeight):

    

    now_fliter=[0,0,0]

    regWidth =list()

    for j in range(subWidth):

        for c in range(3):
            now_fliter[c]=image_pixel[curRow][curCol][c]+image_pixel[curRow][curCol+1][c]+image_pixel[curRow+1][curCol][c]+image_pixel[curRow+1][curCol+1][c]

        regWidth.append((round(now_fliter[0]/4),round(now_fliter[1]/4),round(now_fliter[2]/4)))

        curCol+=j_jump_num

        j_jump_num=(j_jump_num) ^ 3

    curCol=0
    curRow+=i_jump_num       
                
    i_jump_num= (i_jump_num) ^ 3

    regPixel.append(regWidth)
        
            
        


for  i in range(len(regPixel)):
    
    for j in range(len(regPixel[i])):
        
        subImage.putpixel((j,i),regPixel[i][j])
    



# subImage.show()

# subImage.save("new_sub_image_"+str(int(image_width/Ratio))+"_"+str(int(image_height/Ratio))+".jpg")


print("subImage")

#模糊

avg = 7
count = (avg*2+1)**2

subBlurWidth = subWidth
subBlurHeight = subHeight
subBlurImage  = Image.new(mode="RGB",size=(subBlurWidth,subBlurHeight))


for i in range(subHeight):
    
    r = 0
    g = 0
    b = 0

    i_l=i-avg
    i_h=i+avg

    if(i_l<0):
        i_l=0

    if(i_h>=subHeight):
        i_h=subHeight-1
    
    for x in range (0,avg+1):
        for y in range  (i_l,i_h+1):
            r+= subImage.getpixel((x,y))[0]
            g+= subImage.getpixel((x,y))[1]
            b+= subImage.getpixel((x,y))[2]
            
    for j in range(subWidth):

        j_l=j-avg
        j_h=j+avg

        if(j_l<0):
            j_l=0

        if(j_h>=subWidth):
            j_h=subWidth-1

        rel_count=(i_h-i_l+1)*(j_h-j_l+1)
        color=(round(r/rel_count),round(g/rel_count),round(b/rel_count))
        subBlurImage.putpixel((j,i),color)

        for ii in range(i_l,i_h+1):
    
            if(j-avg>=0):
                r-=subImage.getpixel((j-avg,ii))[0]
                g-=subImage.getpixel((j-avg,ii))[1]
                b-=subImage.getpixel((j-avg,ii))[2]
            

            if(j+avg<subWidth) :
                r+=subImage.getpixel((j+avg,ii))[0]
                g+=subImage.getpixel((j+avg,ii))[1]
                b+=subImage.getpixel((j+avg,ii))[2]
            

            

subBlurImage.show()
subBlurImage.save("blur_image_"+str(int(image_width/Ratio))+"_"+str(int(image_height/Ratio))+".jpg")

print("blurImage")

#放大

Ratio=2

reBlurWidth = image_width
reBlurHeight = image_height
reBlurImage  = Image.new(mode="RGB",size=(reBlurWidth,reBlurHeight))
# print(reBlurWidth)
# print(reBlurHeight)
for i in range(subBlurHeight):
    for j in range(subBlurWidth):
       # print(i)
       # print(j)
        for ii in range(int(i*Ratio),int(i*Ratio+Ratio)):
            for jj in range(int(j*Ratio),int(j*Ratio+Ratio)):
                if(ii>reBlurHeight):
                    ii = reBlurHeight-1
                if(jj>reBlurWidth):
                    jj = reBlurWidth-1
                reBlurImage.putpixel((jj,ii),subBlurImage.getpixel((j,i)))
        

# #reBlurImage.show()
# reBlurImage.save("re_image_"+str(image_width)+"_"+str(image_height)+".jpg")



# #疊圖


# lapWidth = image_width
# lapHeight = image_height
# lapImage = Image.new(mode="RGB",size=(lapWidth,lapHeight))



# for i in range(reBlurHeight):
#     for j in range(reBlurWidth):
#         lapImage.putpixel((j,i),reBlurImage.getpixel((j,i)))



# for i in range(subHeight):
#     for j in range(subWidth):
#         lapImage.putpixel((j+int((image_width-subWidth)/2),i+int((image_height-subHeight)/2)),subImage.getpixel((j,i)))



# lapImage.show()
# lapImage.save("lapImage_"+str(image_width)+"_"+str(image_height)+".jpg")



#邊框柔和




# 1934
# 1094     
# 1108
# 1478



