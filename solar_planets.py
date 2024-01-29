import cv2
imagem=cv2.imread("solar-system.jpg")
cv2.putText(imagem,"Sol",(100,50),cv2.FONT_ITALIC,2,(0,0,255))
cv2.putText(imagem,"Mercurio",(110,250),cv2.FONT_ITALIC,0.5,(0,0,255))
cv2.putText(imagem,"Venus",(180,150),cv2.FONT_ITALIC,0.7,(0,0,255))
cv2.putText(imagem,"Terra",(270,150),cv2.FONT_ITALIC,1,(0,0,255))
cv2.imshow("resultado",imagem)
cv2.waitKey(0)