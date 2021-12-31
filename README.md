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

 usually some of them are preinstalled but we can re-check once
 
 # Code
 
 ## Setting up image boiler-plate
 
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











