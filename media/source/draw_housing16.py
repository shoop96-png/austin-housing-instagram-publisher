from PIL import Image, ImageDraw, ImageFont

S=2
im=Image.new('RGB',(1080*S,1350*S),'#321D36')
d=ImageDraw.Draw(im)
regular='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
bold='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def text(x,y,t,size,color,font=regular):
    d.text((x*S,y*S),t,font=ImageFont.truetype(font,size*S),fill=color,anchor='lt')
def rect(box,c): d.rectangle(tuple(int(n*S) for n in box),fill=c)
cream='#F8F2E9'; lime='#D9F44B'; lilac='#C3A8E0'; plum='#321D36'
text(64,54,'AUSTIN HOUSING BRIEF',25,cream,bold)
text(64,105,'PRIVATE HOUSING SUPPLY / 16 NOV 2026',19,lilac)
rect((64,154,1016,157),lilac)
text(58,199,'MORE ROOM',108,lime,bold)
text(58,327,'TO RENT.',108,lime,bold)
rect((64,494,1016,806),lilac)
text(80,510,'161',243,plum,bold)
text(637,563,'PLANNED',31,plum,bold)
text(637,609,'RENTAL',31,plum,bold)
text(637,655,'HOMES',31,plum,bold)
text(64,850,'EASTON PARK',43,cream,bold)
text(64,908,'Southeast Austin',28,lilac)
rect((64,968,1016,970),lilac)
text(64,1008,'3–4',58,lime,bold)
text(64,1085,'BEDROOMS',20,cream,bold)
rect((438,1006,440,1112),lilac)
text(492,1013,'PRIVATE YARDS',36,cream,bold)
text(492,1070,'Planned • Not yet available',23,lilac)
rect((64,1162,1016,1165),lilac)
text(64,1198,'Yardly Easton Park • Taylor Morrison',23,cream)
text(64,1241,'Sources: Groundbreak, Nov 13; developer project page.',18,lilac)
text(64,1274,'Original data graphic • No project rendering',18,lilac)
im.resize((1080,1350),Image.Resampling.LANCZOS).save('/workspace/scratch/6c44a6b800a0/housing16.jpg',quality=92,optimize=True)
