import cv2

l = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
for i in l:
    img = cv2.imread(f"finger_images/{i}")
    print(img.shape)
    img = cv2.resize(img,(200,200))
    print(img.shape)
    cv2.imwrite(f'resized/{i}', img)
