import cv2
import numpy as np
import glob

# Load image file paths and sort them
image_files = sorted(glob.glob('./bag/*.jpg'))

# Load ground truth coordinates from file
with open('./bag/groundtruth.txt', 'r') as file:
    groundtruth_lines = file.readlines()

# Function to parse groundtruth line
def parse_groundtruth_line(line):
    return [float(coord) for coord in line.strip().split(',')]

# Initialize current image index
current_index = 0

# Function to display the current image with polygon
def display_image_with_polygon(index):
    if index < 0 or index >= len(image_files):
        print("Index out of range")
        return

    # Load the image
    image_path = image_files[index]
    image = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if image is None:
        print("Error: Could not load image from %s" % image_path)
        return

    # Parse groundtruth points for the current image
    rbox_points = parse_groundtruth_line(groundtruth_lines[index])

    # Convert the points to the required format for OpenCV
    points = np.array([[rbox_points[0], rbox_points[1]],
                       [rbox_points[2], rbox_points[3]],
                       [rbox_points[4], rbox_points[5]],
                       [rbox_points[6], rbox_points[7]]], np.int32)

    # Reshape the points for the cv2.polylines function
    points = points.reshape((-1, 1, 2))

    # Draw the polygon on the image
    cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)

    # Display the image
    cv2.imshow('Image with Polygon', image)

# Function to handle key press events
def handle_key(event):
    global current_index
    if event == ord('a'):
        # Increment index and display the next image
        current_index += 1
        if current_index >= len(image_files):
            current_index = 0  # Loop back to the first image
        display_image_with_polygon(current_index)

# Display the first image
display_image_with_polygon(current_index)

# Wait indefinitely until a key is pressed
while True:
    key = cv2.waitKey(0)
    if key == ord('a'):
        handle_key(key)
    elif key == ord('q') or key == 27:  # Press 'q' or 'Esc' key to exit
        break

cv2.destroyAllWindows()
