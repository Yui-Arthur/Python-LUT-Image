import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import time
import math

bmp_image = Image.open('rgb.bmp')
# bmp_image = Image.open('sample_1920×1280.bmp')
# bmp_image = Image.open('p.bmp')

# line_horizon = (bmp_image.getpixel((i_horizon, i_vertical)) for i_vertical in range(bmp_image.height) for i_horizon in range(bmp_image.width))

width , height = bmp_image.size
lut="SoftBlackAndWhite"
f = open("./free-customized-LUTs/Shutterstock Free  LUTs/"+lut+".cube")




lut_cube = []

cnt = 0
while True:
    s=f.readline()
    if(s=="LUT_3D_SIZE 33\n"):
        break

for i in f.readlines():
    i=i.strip('\n')

    
    li=i.split(' ')
    # B
    li[0]=float(li[0])*255
    # G
    li[1]=float(li[1])*255
    # R
    li[2]=float(li[2])*255
    lut_cube.append(li)

print("start")


for x in range(width):
    for y in range(height):
        

            pixel = bmp_image.getpixel((x,y))
            R_pos= round(pixel[0]/255*32)
            G_pos= round(pixel[1]/255*32)
            B_pos= round(pixel[2]/255*32)

            index= R_pos + G_pos*33 + B_pos*33*33
            new_pixel=(round(lut_cube[index][0]),round(lut_cube[index][1]),round(lut_cube[index][2]))
            bmp_image.putpixel((x,y),new_pixel)
     

bmp_image.show()
bmp_image.save("rgb_new_"+lut+".jpg")
    