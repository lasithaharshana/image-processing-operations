import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import argparse


def reduce_intensity_levels(image, levels):
    """
    Reduce the number of intensity levels in an image.

    Args:
        image (numpy.ndarray): Input grayscale image
        levels (int): Desired number of intensity levels (between 2 and 256)

    Returns:
        numpy.ndarray: Image with reduced intensity levels
    """
    # Check if levels is valid
    if levels < 2 or levels > 256:
        raise ValueError("Number of intensity levels must be between 2 and 256")

    # Calculate the factor to divide by
    factor = 256 // levels

    # Reduce intensity levels
    reduced = (image // factor) * factor

    return reduced


def generate_intensity_levels(min_level):
    """
    Generate all intensity levels from 256 down to min_level in powers of 2.

    Args:
        min_level (int): Minimum intensity level (must be a power of 2)

    Returns:
        list: List of intensity levels in descending order
    """
    if not (min_level & (min_level - 1) == 0) or min_level <= 0:
        raise ValueError("Minimum level must be a positive power of 2")

    levels = []
    current = 128  # Start from 128 (just below 256)

    while current >= min_level:
        levels.append(current)
        current = current // 2

    return levels


def display_results(original, processed, title):
    """Display original and processed images side by side"""
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
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Reduce intensity levels of an image")
    parser.add_argument(
        "--image",
        type=str,
        default="../input/sample_image.jpg",
        help="Path to the input image",
    )
    parser.add_argument(
        "--level",
        type=int,
        help="The exact intensity level (between 2-256) to reduce to",
    )
    parser.add_argument(
        "--manual",
        action="store_true",
        help="Manually enter intensity level after running",
    )
    args = parser.parse_args()

    # Ensure output directory exists
    output_dir = "../output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read image
    img_path = args.image
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        print(f"Error: Could not read image {img_path}.")
        exit(1)

    # Get intensity level from user if --manual flag is set or no level provided
    intensity_level = args.level
    if args.manual or intensity_level is None:
        print("\n=== Intensity Level Reduction ===")
        print("Enter the exact number of intensity levels to reduce to:")
        print("Enter any number between 2 and 256")

        while True:
            try:
                user_input = input("Enter intensity level (2-256): ")
                intensity_level = int(user_input)
                if 2 <= intensity_level <= 256:
                    break
                else:
                    print("Invalid input. Please enter a number between 2 and 256.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Validate that the level is within range
    if not (2 <= intensity_level <= 256):
        print(f"Error: {intensity_level} is not a valid number between 2 and 256.")
        exit(1)

    # Process with the specified intensity level
    reduced_img = reduce_intensity_levels(img, intensity_level)
    output_path = f"{output_dir}/intensity_reduced_{intensity_level}_levels.jpg"
    cv2.imwrite(output_path, reduced_img)
    print(f"Saved image with {intensity_level} intensity levels to {output_path}")

    # Display the results
    display_results(img, reduced_img, f"Reduced to {intensity_level} Intensity Levels")
