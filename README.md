# ID-card-generator-using-Python
Generates ID card with all details for organization/school and gives png image of ID card and save record in a csv file.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Some Libraries need to be installed in order to use-
>pip install PIL
>
>pip install random
>
>pip install os
>
>pip install datetime
>
>pip install textwrap

>pip install csv



 usually some of them are preinstalled but we can re-check once
 
 # Code-
 
 ## Setting up image boiler-plate -
 
 ```
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

```
## Giving every ID card a unique number-

```
(x,y)=(600,75)
idno=random.randint(1000000,9000000)
message=str('ID'+str(idno))
color='rgb(0,0,0)'
font=ImageFont.truetype('arial.ttf',size=60)
draw.text((x,y),message,fill=color,font=font)

```
## Setting up details on PNG image-

```
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

```
## Saving PNG image-

```
image.save(str(name)+'.png')

```
## Saving Data in a csv file

```
import csv
row=[str(idno),str(name),str(gen),str(age),str(dobir),str(bgrp),str(mo),str(add)]
with open('data.csv','a') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(row)

csvfile.close()

```
# Taking Input from User-

![Input from user](https://github.com/aryanraj2713/ID-card-generator-using-python/blob/main/input.jpg)

# Generated Example ID card-

![Id card](https://github.com/aryanraj2713/ID-card-generator-using-python/blob/main/Aryan%20Raj.png)

*Input details are saved in data.csv also for further reffrence*

## Contribution 

Contributions are always welcome! You can contribute to this project in the following way:
- [ ] Adding feature to add image to ID card 
- [ ] Bug fixes
- [ ] hosting using application

## Author

* Aryan Raj

[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/) by [Aryan Raj](https://www.linkedin.com/in/aryan-raj-3a68b39a/)

























