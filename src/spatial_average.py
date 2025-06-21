import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def apply_spatial_average(image, kernel_size):
    
    # Create the averaging kernel
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (
        kernel_size * kernel_size
    )

    # Apply the filter
    averaged = cv2.filter2D(image, -1, kernel)

    return averaged


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

    # Apply spatial averaging with different kernel sizes
    for size in [3, 10, 20]:
        averaged_img = apply_spatial_average(img, size)
        output_path = f"{output_dir}/spatial_average_{size}x{size}.jpg"
        cv2.imwrite(output_path, averaged_img)
        print(f"Saved image with {size}x{size} spatial averaging to {output_path}")

        # Display the results
        display_results(img, averaged_img, f"{size}x{size} Spatial Average")
