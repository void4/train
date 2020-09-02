from glob import glob
from PIL import Image

for path in glob("air_pink*.png"):
	img = Image.open(path)
	wh = img.size
	wh = [x*2 for x in wh]
	img = img.resize(wh, Image.NEAREST)
	img.save(path)
