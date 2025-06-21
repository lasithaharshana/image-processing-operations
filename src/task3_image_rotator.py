import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def rotate_image(image, angle):

    # Get image dimensions
    height, width = image.shape[:2]

    # Calculate the center of the image
    center = (width // 2, height // 2)

    # Calculate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

    # Calculate new dimensions to ensure the entire rotated image is visible
    if angle % 90 == 0:
        # For 90-degree rotations, dimensions might swap
        if angle % 180 != 0:
            new_width, new_height = height, width
        else:
            new_width, new_height = width, height
    else:
        # For arbitrary angles like 45 degrees
        abs_cos = abs(rotation_matrix[0, 0])
        abs_sin = abs(rotation_matrix[0, 1])
        new_width = int(height * abs_sin + width * abs_cos)
        new_height = int(height * abs_cos + width * abs_sin)

    # Adjust the rotation matrix to account for the new dimensions
    rotation_matrix[0, 2] += (new_width - width) // 2
    rotation_matrix[1, 2] += (new_height - height) // 2

    # Perform the rotation
    rotated = cv2.warpAffine(image, rotation_matrix, (new_width, new_height))

    return rotated


def display_results(original, processed, title):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(processed, cmap="gray")
    plt.title(title)
    plt.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Ensure output directory exists
    output_dir = "../output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read image
    img_path = "../input/sample_image.jpg"
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Error: Could not read image {img_path}.")
        exit(1)

    # Rotate by 45 and 90 degrees
    for angle in [45, 90]:
        rotated_img = rotate_image(img, angle)
        output_path = f"{output_dir}/rotated_{angle}_degrees.jpg"
        cv2.imwrite(output_path, rotated_img)
        print(f"Saved image rotated by {angle} degrees to {output_path}")

        # Display the results
        display_results(img, rotated_img, f"Rotated by {angle} degrees")
