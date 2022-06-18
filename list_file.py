from os import listdir
from os.path import isfile, join
from colorthief import ColorThief
# import matplotlib.pyplot as plt
# import colorsys
# import numpy
onlyfiles = [f for f in listdir('./static/image') if isfile(join('./static/image', f))]
onlyfiles.sort()
poke_color = []
for file in onlyfiles:
    ct = ColorThief(f"./static/image/{file}")
    dominant_color = ct.get_color(quality=1)
    poke_color.append(dominant_color)
print(poke_color)


print(onlyfiles)

poke = {k : v for k,v in zip(onlyfiles,poke_color)}
print(poke)

remove_onlyfiles = []
for file in onlyfiles:
    idx = file.find('(')
    if idx != -1:
        file = file[0:idx]
    remove_onlyfiles.append(file)
new_onlyfiles = remove_onlyfiles
print(new_onlyfiles)