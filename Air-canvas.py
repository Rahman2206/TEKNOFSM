import cv2

# Resim Okumak
image_file = '#'
image = cv2.imread(image_file)
overlay = image.copy()
output = image.copy()
height, width = image.shape[:2]

# Stamp Mekanizm
alpha = 0.3
namestamp = "My Name"
cv2.putText(overlay, namestamp.format(alpha), (width-400, height-24),
            cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 255, 255), thickness=2)
cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, output)
cv2.imwrite("stamped.jpg", output)
