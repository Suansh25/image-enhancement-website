import cv2
import numpy as np

def enhance_image(image_path):
    # Load the image from file
    image = cv2.imread(image_path)
    
    # Check if the image was successfully loaded
    if image is None:
        raise FileNotFoundError(f"Image at path '{image_path}' could not be loaded. Please check the file path.")

    # Define a sharpening kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    
    # Apply the kernel to the image
    sharpened = cv2.filter2D(image, -1, kernel)
    return sharpened

if __name__ == "__main__":
    # Test the enhancement function with a valid image file path
    try:
        output = enhance_image("images\lone-tree.jpg")  # Replace with a valid path to an image file
        cv2.imwrite("enhanced_sample.jpg", output)
        print("Image enhanced and saved as enhanced_sample.jpg")
    except FileNotFoundError as e:
        print(e)
