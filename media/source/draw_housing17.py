import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from PIL import Image

bg='#F7F3E9'; blue='#1738D1'; ink='#18234A'; coral='#F16C57'
fig=plt.figure(figsize=(10.8,13.5),dpi=100,facecolor=bg)
def t(x,y,s,size=22,c=ink,weight='normal',**kw):
    fig.text(x,y,s,fontsize=size,color=c,fontweight=weight,fontfamily='DejaVu Sans',**kw)
t(.065,.945,'AUSTIN HOUSING BRIEF',19,blue,'bold')
t(.065,.902,'RENTAL MARKET / NOVEMBER 17, 2026',13,ink)
t(.06,.824,'ONE, TWO',54,blue,'bold')
t(.06,.755,'OR THREE?',54,blue,'bold')
t(.065,.695,'Austin rent check',25,ink,'bold')
t(.065,.656,'Average monthly rents in Zumper’s bedroom-count table',14,ink)
ax=fig.add_axes([.14,.295,.795,.305],facecolor=bg)
values=[1350,1691,2200]
bars=ax.bar(['1 bedroom','2 bedrooms','3 bedrooms'],values,color=[blue,coral,ink],width=.64)
ax.set_ylim(0,2600)
ax.set_yticks([0,1000,2000]); ax.yaxis.set_major_formatter(FuncFormatter(lambda x,pos:f'${x:,.0f}'))
ax.tick_params(axis='both',length=0,labelsize=14,colors=ink,pad=12)
ax.grid(axis='y',color=ink,alpha=.14); ax.set_axisbelow(True)
for spine in ax.spines.values(): spine.set_visible(False)
for b,v in zip(bars,values):
    ax.text(b.get_x()+b.get_width()/2,v+95,f'${v:,}',ha='center',fontsize=26,fontweight='bold',color=ink)
t(.065,.215,'COMPARE THE WHOLE MONTHLY COST.',19,blue,'bold')
t(.065,.171,'Check fees, utilities, concessions and lease length.',16,ink)
t(.065,.103,'Source: Zumper Austin rent research • Page updated Nov 16, 2026',11,ink)
t(.065,.077,'Rolling 30-day listing sample; all property types by bedroom count.',11,ink)
t(.065,.051,'Original data graphic • Austin Housing Brief',10,ink)
fig.savefig('/workspace/scratch/6c44a6b800a0/housing17.png',dpi=100,facecolor=bg)
Image.open('/workspace/scratch/6c44a6b800a0/housing17.png').convert('RGB').save('/workspace/scratch/6c44a6b800a0/housing17.jpg',quality=94,optimize=True)
