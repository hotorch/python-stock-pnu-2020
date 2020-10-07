# author : DongWon Park


# 2.8.1
import requests
​
url = "http://bit.ly/2JnsHnT"
r = requests.get(url, stream=True).raw
​
# 2.8.2
from PIL import Image
​
img = Image.open(r)
img.show()
img.save('src.png')
print(img.get_format_mimetype)
​
# 2.8.3
BUF_SIZE = 1024
count = 0
​
with open('src.png', 'rb') as sf, open('dst.png', 'wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        count += 1
        if not data:
            break
        df.write(data)
​
### with as 사용 안했을 경우
​
BUF_SIZE = 1024
count = 0
​
sf = open('src.png', 'rb')
df = open('dst1.png', 'wb')
​
while True:
    data = sf.read(BUF_SIZE)
    count += 1
    if not data:
        break
    df.write(data)
​
sf.close()
df.close()
​
df.close()
# 2.8.4
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
​
# 2.8.5
​
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
​
dst_img = mpimg.imread('dst.png')
print(dst_img)
​
dst_img.shape
​
pseudo_img_1 = dst_img[:, :, 0]
pseudo_img_2 = dst_img[:, :, 1]
pseudo_img_3 = dst_img[:, :, 2]
​
plt.suptitle('Image Processing', fontsize = 18)
plt.subplot(2,2,1)
plt.title('Original Image')
plt.imshow(dst_img)
​
plt.subplot(222)
plt.title('Pseudocolor Image 1')
plt.imshow(pseudo_img_1)
​
plt.subplot(223)
plt.title('Pseudocolor Image 2')
plt.ylabel("reverse")
plt.axis([2918, 0, 0, 3024])
plt.imshow(pseudo_img_2)
​
plt.subplot(224)
plt.title('Pseudocolor Image 3')
plt.axis([0, 2918, 0, 3024])
plt.imshow(pseudo_img_3)
​
plt.show()
