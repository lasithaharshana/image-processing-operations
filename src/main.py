import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse

# Import our modules
from intensity_reducer import reduce_intensity_levels, generate_intensity_levels
from spatial_average import apply_spatial_average
from image_rotator import rotate_image
from resolution_reducer import reduce_resolution


def ensure_directories():
    """Ensure input and output directories exist"""
    input_dir = "../input"
    output_dir = "../output"
    
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
        print(f"Created input directory: {input_dir}")
        print(f"Please place a test image named 'sample_image.jpg' in the {input_dir} folder")
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    
    return input_dir, output_dir


def process_all_operations(image_path, intensity_levels=None):
    """
    Process the image with all operations
    
    Args:
        image_path (str): Path to the input image
        intensity_levels (list): List of intensity levels to reduce to (powers of 2)
    """
    print("\n==== IMAGE PROCESSING OPERATIONS ====\n")
    
    # Check if image exists
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        print("Please place a sample image in the input directory.")
        return
    
    # Read the image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not read image {image_path}.")
        return
    
    # Create output directory
    output_dir = "../output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save original image
    cv2.imwrite(f"{output_dir}/original.jpg", img)
    print(f"Original image saved to {output_dir}/original.jpg")
    
    # 1. Reduce intensity levels
    print("\n1. Reducing intensity levels...")
    
    # Process with provided intensity levels
    for level in intensity_levels:
        reduced_img = reduce_intensity_levels(img, level)
        output_path = f"{output_dir}/intensity_reduced_{level}_levels.jpg"
        cv2.imwrite(output_path, reduced_img)
        print(f"  - Saved image with {level} intensity levels to {output_path}")
    
    # 2. Spatial averaging
    print("\n2. Applying spatial averaging...")
    for size in [3, 10, 20]:
        averaged_img = apply_spatial_average(img, size)
        output_path = f"{output_dir}/spatial_average_{size}x{size}.jpg"
        cv2.imwrite(output_path, averaged_img)
        print(f"  - Saved image with {size}x{size} spatial averaging to {output_path}")
    
    # 3. Image rotation
    print("\n3. Rotating image...")
    for angle in [45, 90]:
        rotated_img = rotate_image(img, angle)
        output_path = f"{output_dir}/rotated_{angle}_degrees.jpg"
        cv2.imwrite(output_path, rotated_img)
        print(f"  - Saved image rotated by {angle} degrees to {output_path}")
    
    # 4. Resolution reduction
    print("\n4. Reducing spatial resolution...")
    for size in [3, 5, 7]:
        reduced_img = reduce_resolution(img, size)
        output_path = f"{output_dir}/resolution_reduced_{size}x{size}.jpg"
        cv2.imwrite(output_path, reduced_img)
        print(f"  - Saved image with {size}x{size} resolution reduction to {output_path}")
    
    print("\nAll operations completed successfully.")
    print(f"Results saved in the '{output_dir}' folder.")


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Image Processing Operations')
    parser.add_argument('--image', type=str, default='../input/sample_image.jpg',
                      help='Path to the input image (default: ../input/sample_image.jpg)')
    args = parser.parse_args()
    
    # Always ask for exact intensity level
    print("\n=== Intensity Level Reduction ===")
    print("Enter the exact number of intensity levels to reduce to:")
    print("Enter any number between 2 and 256")
    
    while True:
        try:
            intensity_level = int(input("Enter intensity level (2-256): "))
            # Validate that it's between 2 and 256
            if 2 <= intensity_level <= 256:
                break
            else:
                print("Invalid input. Please enter a number between 2 and 256.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Use a single intensity level
    intensity_levels = [intensity_level]
    
    print(f"Using intensity level: {intensity_level}")
    
    # Ensure directories exist
    input_dir, output_dir = ensure_directories()
    
    # Process the image with all operations
    process_all_operations(args.image, intensity_levels)


if __name__ == "__main__":
    main()
