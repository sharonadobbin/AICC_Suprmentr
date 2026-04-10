import cv2

# Load the image (ensure the file exists in the same folder or provide full path)
image = cv2.imread("image.jpg")

# Check if image loaded properly
if image is None:
    print("Error: Image not found!")
else:
    print("=== Image as Numbers ===\n")
    
    # Print shape of image
    print("Image Shape:", image.shape)
    
    # Extract height, width, channels
    height, width, channels = image.shape
    print("Height:", height)
    print("Width:", width)
    print("Channels:", channels)
    
    # Print pixel value at a specific location
    x, y = 100, 100
    print(f"\nPixel value at ({x},{y}):", image[x, y])
    
    # Print a small region of pixel values (5x5)
    print("\nSample pixel values (5x5 region):")
    print(image[0:5, 0:5])
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    print("\nGrayscale Image Shape:", gray.shape)
    
    # Save the original and grayscale images
    cv2.imwrite("output_color.jpg", image)
    cv2.imwrite("output_gray.jpg", gray)
    
    print("\nImages saved as 'output_color.jpg' and 'output_gray.jpg'")
    
    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()