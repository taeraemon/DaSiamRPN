import numpy as np
import cv2

# Create a random 10x10 image
image = np.random.rand(10, 10, 3) * 255
image = image.astype(np.uint8)

# Display the image
cv2.imshow('Random Image', image)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close all OpenCV windows