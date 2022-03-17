import cv2

# Resim Okumak
image_file = '201611710435522.jpg'
image = cv2.imread(image_file)
overlay = image.copy()
output = image.copy()
height, width = image.shape[:2]

# Stamp Mekanizm
alpha = 0.3
namestamp = "TR-END"
cv2.putText(overlay, namestamp.format(alpha), (width-450, height-200),
            cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), thickness=5)
cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
cv2.imwrite("stampedd1.jpg", output)
