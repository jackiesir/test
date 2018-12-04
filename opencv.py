# import cv2 as cv
#
#
# img = cv.imread("/home/jackie/Pictures/1.png")
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# face_cascade = cv.CascadeClassifier('/home/jackie/Pictures/haarcascade_frontalface_alt2.xml')
# # 探测人脸
# # 根据训练的数据来对新图片进行识别的过程。
# faces = face_cascade.detectMultiScale(
#   gray,
#   scaleFactor = 1.15,
#   minNeighbors = 5,
#   minSize = (5,5),
#   #flags = cv.HAAR_SCALE_IMAGE
# )
#
# # 我们可以随意的指定里面参数的值，来达到不同精度下的识别。返回值就是opencv对图片的探测结果的体现。
#
# # 处理人脸探测的结果
# print ("发现{0}个人脸!".format(len(faces)))
# for(x,y,w,h) in faces:
#     cv.rectangle(img,(x,y),(x+w,y+w),(0,255,0),2)
#     # cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)
#
# cv.imshow("image",img)
# cv.waitKey(10000)
# cv.destroyAllWindows()

#参考网址：https://www.cnblogs.com/Lin-Yi/p/9417748.html
import cv2
# 创建人脸检测的对象
face_cascade = cv2.CascadeClassifier('/home/jackie/Pictures/haarcascade_frontalface_alt2.xml')
# 创建眼睛检测的对象
eye_cascade = cv2.CascadeClassifier("/home/jackie/Pictures/haarcascade_eye.xml")
# 连接摄像头的对象 0表示摄像头的编号
cap = cv2.VideoCapture(0)
while True:
    # 读取当前帧
    ret,frame = cap.read()
    # 转为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 检测人脸 返回列表 每个元素都是(x, y, w, h)表示矩形的左上角和宽高
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # 画出人脸的矩形
    for (x, y, w, h) in faces:
        # 画矩形 在frame图片上画， 传入左上角和右下角坐标 矩形颜色 和线条宽度
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 把脸单独拿出来
        roi_gray = gray[y: y + h, x: x + w]
        # 在脸上检测眼睛   (40, 40)是设置最小尺寸，再小的部分会不检测
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (40, 40))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)
        #

    cv2.imshow('Capture',frame)
    # gray = cv2.cvtColor(cap,cv2.COLOR_BGR2GRAY)

    # # 探测人脸
    # # 根据训练的数据来对新图片进行识别的过程。
    # faces = face_cascade.detectMultiScale(
    #   gray,
    #   scaleFactor = 1.15,
    #   minNeighbors = 5,
    #   minSize = (5,5),
    #   #flags = cv.HAAR_SCALE_IMAGE
    # )
    #
    # # 我们可以随意的指定里面参数的值，来达到不同精度下的识别。返回值就是opencv对图片的探测结果的体现。
    #
    # # 处理人脸探测的结果
    # print ("发现{0}个人脸!".format(len(faces)))
    # for(x,y,w,h) in faces:
    #     cv2.rectangle(cap,(x,y),(x+w,y+w),(0,255,0),2)
    #     # cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
