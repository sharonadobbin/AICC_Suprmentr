import cv2

# Load the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
else:
    print("=== Image Filter Lab ===")

    # Convert to Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Blur (Gaussian Blur)
    blur = cv2.GaussianBlur(image, (7, 7), 0)

    # Edge Detection (Canny)
    edges = cv2.Canny(image, 100, 200)

    # Display all images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)
    cv2.imshow("Blurred Image", blur)
    cv2.imshow("Edge Detection", edges)

    # Save output images (optional but good for submission)
    cv2.imwrite("gray.jpg", gray)
    cv2.imwrite("blur.jpg", blur)
    cv2.imwrite("edges.jpg", edges)

    print("Filtered images saved as gray.jpg, blur.jpg, edges.jpg")

    # Wait and close
    cv2.waitKey(0)
    cv2.destroyAllWindows()