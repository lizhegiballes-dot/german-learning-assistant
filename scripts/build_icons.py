"""Draw a small original typographic-style mark; no third-party image assets."""
from pathlib import Path
from PIL import Image, ImageDraw
root=Path(__file__).resolve().parents[1]/'extension'/'icons'
root.mkdir(exist_ok=True)
for size in [16,32,48,128]:
    scale=4;s=size*scale
    image=Image.new('RGBA',(s,s),(0,0,0,0));d=ImageDraw.Draw(image)
    d.rounded_rectangle((0,0,s-1,s-1),radius=s*.2,fill='#284b65')
    pts=[(.18,.25),(.33,.76),(.5,.39),(.67,.76),(.82,.25)]
    d.line([(round(x*s),round(y*s))for x,y in pts],fill='#fffdf8',width=round(.075*s),joint='curve')
    image.resize((size,size),Image.Resampling.LANCZOS).save(root/f'{size}.png')
