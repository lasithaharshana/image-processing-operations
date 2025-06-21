import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def reduce_intensity_levels(image, levels):
    """
    Reduce the number of intensity levels in an image.
    
    Args:
        image (numpy.ndarray): Input grayscale image
        levels (int): Desired number of intensity levels (must be a power of 2)
    
    Returns:
        numpy.ndarray: Image with reduced intensity levels
    """
    # Check if levels is a power of 2
    if not (levels & (levels - 1) == 0) or levels <= 0:
        raise ValueError("Number of levels must be a positive power of 2")
    
    # Calculate the factor to divide by
    factor = 256 // levels
    
    # Reduce intensity levels
    reduced = (image // factor) * factor
    
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
        
    # Process with different intensity levels
    for levels in [128, 64, 32, 16, 8, 4, 2]:
        reduced_img = reduce_intensity_levels(img, levels)
        output_path = f"{output_dir}/intensity_reduced_{levels}_levels.jpg"
        cv2.imwrite(output_path, reduced_img)
        print(f"Saved image with {levels} intensity levels to {output_path}")
        
        # Display the results
        display_results(img, reduced_img, f"Reduced to {levels} Intensity Levels")
