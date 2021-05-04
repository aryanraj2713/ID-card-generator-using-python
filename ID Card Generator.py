# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 06:39:07 2020

@author: Aryan raj
"""

from PIL import Image, ImageDraw, ImageFont
image=Image.new('RGB',(1000,900),(255,255,255))
draw=ImageDraw.Draw(image)
font=ImageFont.truetype('arial.ttf', size=45)
import random
import os
import datetime
import textwrap
os.system("Title ID Card Generator")
d_date=datetime.datetime.now()
reg_format_date=d_date.strftime("%d-%m-%Y\t\t\t\t\t ID CARD Generator\t\t\t\t\t %I:%M:%S %p")
print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
print(reg_format_date)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
#starting position of message
print('\n\nAll fields are Mandatory')
print('Avoid any kind of Spelling Mistakes')
print('Write Everything in uppercase letters')
(x,y)=(50,50)
message = input('\nEnter your School Name:')
company=message
color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=80)
draw.text((x,y),message,fill=color,font=font)


#adding an unique number. You can manually take it from user
(x,y)=(600,75)
idno=random.randint(1000000,9000000)
message=str('ID'+str(idno))
color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=60)
draw.text((x,y),message,fill=color,font=font)



(x,y)=(50,150)
name='Name'
color='rgb(255,0,0)'
draw.text((x,y),name,fill=color,font=font)

(x,y)=(50,220)

message=input('Enter your full Name:')
name=message

color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=60)
draw.text((x,y),message,fill=color,font=font)


(x,y)=(45,300)
gen='Branch'
color='rgb(255,0,0)'
draw.text((x,y),gen,fill=color,font=font)

(x,y)=(50,350)
branch=input('Enter Your School Branch:')
color="rgb(0,0,0)"
draw.text((x,y),branch,fill=color,font=font)

(x,y)=(300,300)
sem='Term'
color='rgb(255,0,0)'
draw.text((x,y),sem,fill=color,font=font)
(x,y)=(300,350)

age=input('Enter Your Term:')
color='rgb(0,0,0)'
draw.text((x,y),age,fill=color,font=font)


(x,y)=(50,420)
dobir='Date of Birth'
color='rgb(255,0,0)'
draw.text((x,y),dobir,fill=color,font=font)

(x,y)=(60,470)
dob=input("Enter your DOB:")
color='rgb(0,0,0)'
draw.text((x,y),dob,fill=color,font=font)


(x,y)=(50,530)
bd='Blood Group'
color='rgb(255,0,0)'
draw.text((x,y),bd,fill=color,font=font)

(x,y)=(50,580)
bgrp=input('Enter Blood Group:')
color='rgb(0,0,0)'
draw.text((x,y),bgrp,fill=color,font=font)

(x,y)=(50,640)
mb='Mobile No'
color='rgb(255,0,0)'
draw.text((x,y),mb,fill=color,font=font)

(x,y)=(50,690)
mo=input("Enter your Mobile Number:")
temp=mo
color='rgb(0,0,0)'
draw.text((x,y),mo,fill=color,font=font)


(x,y)=(50,740)
ad='Address'
color='rgb(255,0,0)'
draw.text((x,y),ad,fill=color,font=font)

(x,y)=(50,800)
add=input('Enter Your Address:')
color='rgb(0,0,0)'
draw.text((x,y),add,fill=color,font=font)
image.save(str(name)+'.png')

#save the edited image

image.save(str(name)+'.png')

import csv
row=[str(idno),str(name),str(gen),str(age),str(dobir),str(bgrp),str(mo),str(add)]
with open('data.csv','a') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(row)

csvfile.close()



