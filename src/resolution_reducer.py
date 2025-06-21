import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def reduce_resolution(image, block_size):
    """
    Reduce image resolution by replacing each block_size x block_size block with its average value.
    
    Args:
        image (numpy.ndarray): Input grayscale image
        block_size (int): Size of the non-overlapping blocks
        
    Returns:
        numpy.ndarray: Image with reduced resolution
    """
    height, width = image.shape[:2]
    
    # Calculate new dimensions (dropping any remainder)
    new_height = height // block_size
    new_width = width // block_size
    
    # Trim image to fit exact multiple of block_size
    trimmed_height = new_height * block_size
    trimmed_width = new_width * block_size
    image = image[:trimmed_height, :trimmed_width]
    
    # Create output image
    reduced = np.zeros((trimmed_height, trimmed_width), dtype=image.dtype)
    
    # Process each block
    for i in range(new_height):
        for j in range(new_width):
            # Extract block
            y_start = i * block_size
            x_start = j * block_size
            block = image[y_start:y_start + block_size, x_start:x_start + block_size]
            
            # Calculate average of the block
            avg_value = np.mean(block).astype(image.dtype)
            
            # Replace the entire block with the average value
            reduced[y_start:y_start + block_size, x_start:x_start + block_size] = avg_value
    
    return reduced


def display_results(original, processed, title):
    """Display original and processed images side by side"""
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.imshow(original, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.imshow(processed, cmap='gray')
    plt.title(title)
    plt.axis('off')
    
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
    
    # Reduce resolution with different block sizes
    for size in [3, 5, 7]:
        reduced_img = reduce_resolution(img, size)
        output_path = f"{output_dir}/resolution_reduced_{size}x{size}.jpg"
        cv2.imwrite(output_path, reduced_img)
        print(f"Saved image with {size}x{size} resolution reduction to {output_path}")
        
        # Display the results
        display_results(img, reduced_img, f"{size}x{size} Resolution Reduction")
