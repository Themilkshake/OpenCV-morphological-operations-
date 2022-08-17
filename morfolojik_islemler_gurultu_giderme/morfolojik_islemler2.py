import numpy as np
import cv2

image=cv2.imread("morfolojik_islemler_gurultu_giderme/is.jpg")

kernel=np.ones((5,5),np.uint8)

"""
erotion ve diletion operatörlerin haricindekiler morfolojiex ile çağrılır.
"""

#---------------------------------------------------------------------------------------------------------

"""
Closing işlemi,resimde kopuk yerler varsa ilk olarak dilation yapılarak birleştirilir,
daha sonrasında erosion yapılarak eski haline getirilir.

Opening işlemi, resimde paraziteri yok etmek için ilk olarak erozyon yapılır.
Daha sonasında genişletme yaparak eski halide getirilir.
"""
opening=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)

cv2.imshow("opening",opening)

closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)

cv2.imshow("closing",closing)

#---------------------------------------------------------------------------------------------------------

"""
Gradient işlemi: Erosion işlemi yapılmış resimden dilation işlemi yapılmış aynı resmi çıkartma işlemidir.
"""
gradient=cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)

cv2.imshow("gradient", gradient)

#---------------------------------------------------------------------------------------------------------
"""
tophat işlemi: resmin opening ile orjinal halini çıkarıyor. Ve geriye gürültü dediğimiz kısım kalıyor.
"""

tophat=cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)

cv2.imshow("tophat",tophat)

#---------------------------------------------------------------------------------------------------------
"""
blackhat işlemi: resmin closing ile orjinal halini çıkarıyor.
"""

blackhat=cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("blackhat",blackhat)

#---------------------------------------------------------------------------------------------------------

cv2.waitKey()
cv2.destroyAllWindows()