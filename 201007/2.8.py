# python & pycharm install respectively
# create virtual environment via 'venv' (64 => C:\VirtualEnv\py381_64 & 32 => C:\VirtualEnv\py380_32)
# pip install -r requirements.txt in "py381_64"
# pycharm : open virtual env
# --------------------------------------------------------------------------------------------------- #
​
# 2.8
## requests pkg : get() vs post()
## example of request
​
import requests
import pandas as pd
​
html = requests.get('https://finance.naver.com/item/frgn.nhn?code=005930&page=1')
table = pd.read_html(html.text)
data = table[2].dropna().reset_index(drop=True)
data.shape
data.head(5)
​
## pillow
​
from PIL import Image, ImageFilter
url = 'http://bit.ly/2JnsHnT'
r = requests.get(url, stream = True).raw
​
img = Image.open(r)
​
img.size
img.format
print("img : ", img.get_format_mimetype)
​
img.show()
img.save('src.png')
​
size = (900, 900)
img2 = img.resize(size)
img2.save('src2.png')
​
img3 = img.rotate(90)
img3.save('src3.png')
​
blur_img = img.filter(ImageFilter.BLUR)
blur_img.save('blur.png')
​
## binary file
## - 사용자, 프로그램이 사용하던 정보나 숫자 값을 특별한 가공 없이 그대로 파일에 저장
## - 바이너리 읽기 모드 rb, 쓰기 모드 wb
BUF_SIZE = 1024
with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break
​
## SHA-256 : jusths.tistory.com/43
## set of hash function from NSA
​
import hashlib
​
sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()
​
with open('src.png', 'rb') as sf, open('dst.png', 'rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())
​
print("src.png's hash : {}".format(sha_src.hexdigest()))
print("dsc.png's hash : {}".format(sha_dst.hexdigest()))
​
## matplotlib for image (matplotlib.image)
## pseudo color
​
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
​
plt.suptitle('Image Processing', fontsize = 18)
​
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png'))
​
plt.subplot(122)
plt.title('Pseudocolor Image')
dst_img = mpimg.imread('dst.png')
pseudo_img = dst_img [:, :, 0]
plt.imshow(pseudo_img)
plt.show()
