from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
im = Image.new('RGB', (W, H), '#F7E4DD')
d = ImageDraw.Draw(im)
ink, accent, muted = '#4B173C', '#C44C36', '#775D6D'
fontroot = '/usr/share/fonts/truetype/dejavu/'
def f(size, bold=False):
    return ImageFont.truetype(fontroot + ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'), size)
def text(x,y,s,size=30,bold=False,fill=ink):
    d.text((x,y),s,font=f(size,bold),fill=fill,stroke_width=0)
def rule(y): d.line((64,y,1016,y),fill=ink,width=2)

text(64,43,'AUSTIN HOUSING BRIEF',26,True)
text(815,45,'19 NOV 26',23)
rule(95)
text(64,125,'CENTRAL AUSTIN  /  OCTOBER 2026',25,True)
text(58,184,'Less time.',89,True)
text(58,288,'Lower median.',89,True)
text(64,413,'A closer look at completed home sales',30)

rule(483)
text(64,514,'AVERAGE DAYS ON MARKET',25,True)
text(54,556,'62',143,True)
text(269,646,'days',36)
text(601,570,'78 days',46,True)
text(603,632,'October 2025',25,fill=muted)
d.line((1010,562,1010,655),fill=accent,width=9)
d.polygon([(987,635),(1033,635),(1010,663)],fill=accent)
text(66,737,'16 fewer days than a year earlier',29,fill=accent)

rule(805)
text(64,838,'MEDIAN SALE PRICE',25,True)
text(56,891,'$825K',109,True)
text(660,902,'$894K',44,True)
text(662,963,'October 2025',25,fill=muted)
text(66,1038,'$69,000 lower than a year earlier',29,fill=accent)

d.rectangle((0,1114,W,1240),fill=ink)
text(64,1134,'146 closed sales',39,True,fill='#F7E4DD')
text(65,1190,'Down 17.5% from October 2025',25,fill='#F7E4DD')
text(64,1262,'Source: Unlock MLS via Community Impact, Nov. 17, 2026',21)
text(64,1298,'Scope: Community Impact’s nine-ZIP Central Austin coverage area.',20)
im.save('/workspace/scratch/6c44a6b800a0/housing19.jpg', quality=94, subsampling=0)
