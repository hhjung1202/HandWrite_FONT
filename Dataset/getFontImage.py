
from PIL import Image, ImageDraw, ImageFont, ImageFilter

#configuration
width=500
height=100
back_ground_color=(255,255,255)
font_size=36
font_color=(0,0,0)
# unicode_text = u"\u2605" + u"\u2606" + u"Текст на русском" + u"파이썬"
unicode_text = u"아버지 가방에 들어가시다"

im  =  Image.new ( "RGB", (width,height), back_ground_color )
draw  =  ImageDraw.Draw ( im )
unicode_font = ImageFont.truetype("../Font/Bold.ttf", font_size)
draw.text ( (10,10), unicode_text, font=unicode_font, fill=font_color )

im.save("Bold.jpg")


label_width=100
label_height=100
unicode_text = u"가"

im  =  Image.new ( "RGB", (label_width,label_height), back_ground_color )
draw  =  ImageDraw.Draw ( im )
unicode_font = ImageFont.truetype("../Font/Bold.ttf", font_size)
draw.text ( (10,10), unicode_text, font=unicode_font, fill=font_color )

im.save("Bold_가.jpg")
