from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf', 60)
for index,j in df.iterrows():
    img = Image.open('Certificate.png')
    draw = ImageDraw.Draw(img)
    draw.text(xy = (150, 250)
              text='{}'.format(j['name']),
              fill=(0, 0, 0),
              font=font)
    img.save('pictures/{}.png'.format(j['name']))
