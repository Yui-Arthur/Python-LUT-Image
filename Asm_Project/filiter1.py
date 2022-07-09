import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import time
import math

bmp_image = Image.open('new4.jpeg')
# bmp_image = Image.open('sample_1920×1280.bmp')
# bmp_image = Image.open('p.bmp')

# line_horizon = (bmp_image.getpixel((i_horizon, i_vertical)) for i_vertical in range(bmp_image.height) for i_horizon in range(bmp_image.width))

width , height = bmp_image.size
lut="BlueArchitecture"
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

# for i in range(33):
#     for j in range(33):
#         for k in range(33):
#             print("R "+str(k*7.76)+" G "+str(j*7.76)+" B "+str(i*7.76)+" "+str(i*33*33+j*33+k)+" "+str(lut_cube[i*33*33+j*33+k]))
#             # time.sleep(0.5)

for x in range(width):
    for y in range(height):
        
        if x<width:
            pixel = bmp_image.getpixel((x,y))
            R_pos= pixel[0]/255*32
            G_pos= pixel[1]/255*32
            B_pos= pixel[2]/255*32

            redH = math.ceil(R_pos)
            redL = math.floor(R_pos)

            greenH = math.ceil(G_pos)
            greenL = math.floor(G_pos)

            blueH = math.ceil(B_pos)
            blueL = math.floor(B_pos)
            
            dR=R_pos-redL
            dG=G_pos-greenL
            dB=B_pos-blueL

            if(dR>=dG>=dB):
                nR=lut_cube[redH + greenL*33 + blueL*33*33][0]-lut_cube[redL + greenL*33 + blueL*33*33][0]
                nG=lut_cube[redH + greenL*33 + blueL*33*33][1]-lut_cube[redL + greenL*33 + blueL*33*33][1]
                nB=lut_cube[redH + greenL*33 + blueL*33*33][2]-lut_cube[redL + greenL*33 + blueL*33*33][2]
                c1=(nR,nG,nB)
                nR=lut_cube[redH + greenH*33 + blueL*33*33][0]-lut_cube[redH + greenL*33 + blueL*33*33][0]
                nG=lut_cube[redH + greenH*33 + blueL*33*33][1]-lut_cube[redH + greenL*33 + blueL*33*33][1]
                nB=lut_cube[redH + greenH*33 + blueL*33*33][2]-lut_cube[redH + greenL*33 + blueL*33*33][2]
                c2=(nR,nG,nB)
                nR=lut_cube[redH + greenH*33 + blueH*33*33][0]-lut_cube[redH + greenH*33 + blueL*33*33][0]
                nG=lut_cube[redH + greenH*33 + blueH*33*33][1]-lut_cube[redH + greenH*33 + blueL*33*33][1]
                nB=lut_cube[redH + greenH*33 + blueH*33*33][2]-lut_cube[redH + greenH*33 + blueL*33*33][2]
                c3=(nR,nG,nB)
            elif(dR>=dB>=dG):
                nR=lut_cube[redH + greenL*33 + blueL*33*33][0]-lut_cube[redL + greenL*33 + blueL*33*33][0]
                nG=lut_cube[redH + greenL*33 + blueL*33*33][1]-lut_cube[redL + greenL*33 + blueL*33*33][1]
                nB=lut_cube[redH + greenL*33 + blueL*33*33][2]-lut_cube[redL + greenL*33 + blueL*33*33][2]
                c1=(nR,nG,nB)
                nR=lut_cube[redH + greenH*33 + blueH*33*33][0]-lut_cube[redH + greenL*33 + blueH*33*33][0]
                nG=lut_cube[redH + greenH*33 + blueH*33*33][1]-lut_cube[redH + greenL*33 + blueH*33*33][1]
                nB=lut_cube[redH + greenH*33 + blueH*33*33][2]-lut_cube[redH + greenL*33 + blueH*33*33][2]
                c2=(nR,nG,nB)
                nR=lut_cube[redH + greenL*33 + blueH*33*33][0]-lut_cube[redH + greenL*33 + blueL*33*33][0]
                nG=lut_cube[redH + greenL*33 + blueH*33*33][1]-lut_cube[redH + greenL*33 + blueL*33*33][1]
                nB=lut_cube[redH + greenL*33 + blueH*33*33][2]-lut_cube[redH + greenL*33 + blueL*33*33][2]
                c3=(nR,nG,nB)
            elif(dB>=dR>=dG):
                nR=lut_cube[redH + greenL*33 + blueH*33*33][0]-lut_cube[redL + greenL*33 + blueH*33*33][0]
                nG=lut_cube[redH + greenL*33 + blueH*33*33][1]-lut_cube[redL + greenL*33 + blueH*33*33][1]
                nB=lut_cube[redH + greenL*33 + blueH*33*33][2]-lut_cube[redL + greenL*33 + blueH*33*33][2]
                c1=(nR,nG,nB)
                nR=lut_cube[redH + greenH*33 + blueH*33*33][0]-lut_cube[redH + greenL*33 + blueH*33*33][0]
                nG=lut_cube[redH + greenH*33 + blueH*33*33][1]-lut_cube[redH + greenL*33 + blueH*33*33][1]
                nB=lut_cube[redH + greenH*33 + blueH*33*33][2]-lut_cube[redH + greenL*33 + blueH*33*33][2]
                c2=(nR,nG,nB)
                nR=lut_cube[redL + greenL*33 + blueH*33*33][0]-lut_cube[redL + greenL*33 + blueL*33*33][0]
                nG=lut_cube[redL + greenL*33 + blueH*33*33][1]-lut_cube[redL + greenL*33 + blueL*33*33][1]
                nB=lut_cube[redL + greenL*33 + blueH*33*33][2]-lut_cube[redL + greenL*33 + blueL*33*33][2]
                c3=(nR,nG,nB)
            elif(dG>=dR>=dB):
                nR=lut_cube[redH + greenH*33 + blueL*33*33][0]-lut_cube[redL + greenH*33 + blueL*33*33][0]
                nG=lut_cube[redH + greenH*33 + blueL*33*33][1]-lut_cube[redL + greenH*33 + blueL*33*33][1]
                nB=lut_cube[redH + greenH*33 + blueL*33*33][2]-lut_cube[redL + greenH*33 + blueL*33*33][2]
                c1=(nR,nG,nB)
                nR=lut_cube[redL + greenH*33 + blueL*33*33][0]-lut_cube[redL + greenL*33 + blueL*33*33][0]
                nG=lut_cube[redL + greenH*33 + blueL*33*33][1]-lut_cube[redL + greenL*33 + blueL*33*33][1]
                nB=lut_cube[redL + greenH*33 + blueL*33*33][2]-lut_cube[redL + greenL*33 + blueL*33*33][2]
                c2=(nR,nG,nB)
                nR=lut_cube[redH + greenH*33 + blueH*33*33][0]-lut_cube[redH + greenH*33 + blueL*33*33][0]
                nG=lut_cube[redH + greenH*33 + blueH*33*33][1]-lut_cube[redH + greenH*33 + blueL*33*33][1]
                nB=lut_cube[redH + greenH*33 + blueH*33*33][2]-lut_cube[redH + greenH*33 + blueL*33*33][2]
                c3=(nR,nG,nB)
            elif(dG>=dB>=dR):
                nR=lut_cube[redH + greenH*33 + blueH*33*33][0]-lut_cube[redL + greenH*33 + blueH*33*33][0]
                nG=lut_cube[redH + greenH*33 + blueH*33*33][1]-lut_cube[redL + greenH*33 + blueH*33*33][1]
                nB=lut_cube[redH + greenH*33 + blueH*33*33][2]-lut_cube[redL + greenH*33 + blueH*33*33][2]
                c1=(nR,nG,nB)
                nR=lut_cube[redL + greenH*33 + blueL*33*33][0]-lut_cube[redL + greenL*33 + blueL*33*33][0]
                nG=lut_cube[redL + greenH*33 + blueL*33*33][1]-lut_cube[redL + greenL*33 + blueL*33*33][1]
                nB=lut_cube[redL + greenH*33 + blueL*33*33][2]-lut_cube[redL + greenL*33 + blueL*33*33][2]
                c2=(nR,nG,nB)
                nR=lut_cube[redL + greenH*33 + blueH*33*33][0]-lut_cube[redL + greenH*33 + blueL*33*33][0]
                nG=lut_cube[redL + greenH*33 + blueH*33*33][1]-lut_cube[redL + greenH*33 + blueL*33*33][1]
                nB=lut_cube[redL + greenH*33 + blueH*33*33][2]-lut_cube[redL + greenH*33 + blueL*33*33][2]
                c3=(nR,nG,nB)
            elif(dB>=dG>=dR):
                nR=lut_cube[redH + greenH*33 + blueH*33*33][0]-lut_cube[redL + greenH*33 + blueH*33*33][0]
                nG=lut_cube[redH + greenH*33 + blueH*33*33][1]-lut_cube[redL + greenH*33 + blueH*33*33][1]
                nB=lut_cube[redH + greenH*33 + blueH*33*33][2]-lut_cube[redL + greenH*33 + blueH*33*33][2]
                c1=(nR,nG,nB)
                nR=lut_cube[redL + greenH*33 + blueH*33*33][0]-lut_cube[redL + greenL*33 + blueH*33*33][0]
                nG=lut_cube[redL + greenH*33 + blueH*33*33][1]-lut_cube[redL + greenL*33 + blueH*33*33][1]
                nB=lut_cube[redL + greenH*33 + blueH*33*33][2]-lut_cube[redL + greenL*33 + blueH*33*33][2]
                c2=(nR,nG,nB)
                nR=lut_cube[redL + greenL*33 + blueH*33*33][0]-lut_cube[redL + greenL*33 + blueL*33*33][0]
                nG=lut_cube[redL + greenL*33 + blueH*33*33][1]-lut_cube[redL + greenL*33 + blueL*33*33][1]
                nB=lut_cube[redL + greenL*33 + blueH*33*33][2]-lut_cube[redL + greenL*33 + blueL*33*33][2]
                c3=(nR,nG,nB)

            new_R=round(lut_cube[redL + greenL*33 + blueL*33*33][0]+c1[0]*dR+c2[0]*dG+c3[0]*dB)
            new_G=round(lut_cube[redL + greenL*33 + blueL*33*33][1]+c1[1]*dR+c2[1]*dG+c3[1]*dB)
            new_B=round(lut_cube[redL + greenL*33 + blueL*33*33][2]+c1[2]*dR+c2[2]*dG+c3[2]*dB)
            new_pixel=(new_R,new_G,new_B)

            # index = R_pos + G_pos*33 + B_pos*33*33  
            # new_pixel=(round(lut_cube[index][0]),round(lut_cube[index][1]),round(lut_cube[index][2]))
            
            bmp_image.putpixel((x,y),new_pixel)
        # else:
        #     pixel = bmp_image.getpixel((x,y))
        #     R_pos= round(pixel[0]/255*32)
        #     G_pos= round(pixel[1]/255*32)
        #     B_pos= round(pixel[2]/255*32)

        #     index= R_pos + G_pos*33 + B_pos*33*33
        #     new_pixel=(round(lut_cube[index][0]),round(lut_cube[index][1]),round(lut_cube[index][2]))
        #     bmp_image.putpixel((x,y),new_pixel)
        # time.sleep(1)
    # print('')

bmp_image.show()
bmp_image.save("demo4_new_"+lut+".jpg")
    