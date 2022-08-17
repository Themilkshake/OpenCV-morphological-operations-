import numpy as np
import cv2

image=cv2.imread("morfolojik_islemler_gurultu_giderme/is.jpg")

kernel=np.ones((5,5),np.uint8)

#dilation=cv2.dilate(image,kernel,iterations=1)


"""
Dilation (genişletme), çizginin boyutlarını daha da genişletir.
"""
#cv2.imshow("orijinal",image)
#cv2.imshow("dilation",dilation)




"""
Erosion(aşındırma), çizginin boyutlarını daha da daraltır.
"""


"""
Gürültü gidermede ilk olarak erozyon(erosion) yaılarak grültü yok edilir.
Daha sonrasında genişletme(dilation) işlemi yapılarak yazı ön plana çıkarılır.
"""
cv2.imshow("a",image)
erosion=cv2.erode(image,kernel,iterations=1)
cv2.imshow("birinci",erosion)

dilation=cv2.dilate(erosion,kernel,iterations=1)

cv2.imshow("ikinci",dilation)




cv2.waitKey(0)
cv2.destroyAllWindows()