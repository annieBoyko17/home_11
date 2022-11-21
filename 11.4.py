import cv2
from PIL import Image
image_path = 'cat.jpeg.png'
cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
image = cv2.imread(image_path)
cat_face = cat_face_cascade.detectMultiScale(image)
cat = Image.open(image_path)
smile = Image.open('smile.png')
cat = cat.convert("RGBA")
smile = smile.convert("RGBA")
for (x,y,w,h) in cat_face:
    smile = smile.resize((w, int(h/2)))
    cat.paste(smile, (x, int(y + h/1.7)), smile)
    cat.save("cat_with_smile.png")
    cat_with_smile = cv2.imread("cat_with_smile.png")
    cv2.imshow("Cat_with_smile", cat_with_smile)
    cv2.waitKey()


#cv2.imshow("Cat.jpeg", image)
#cv2.waitKey()