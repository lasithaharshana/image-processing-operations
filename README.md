# EC7212 – Computer Vision and Image Processing – Assignment 1

**Name**: De Silva K.B.L.H.  
**Index No**: EG/2020/3882  
**GitHub Repository**: [Image Processing Operations](https://github.com/lasithaharshana/image-processing-operations.git)

## Sample Image

![Sample Image](output/original.jpg)

## Task 1: Intensity Level Reduction

This task reduces the number of intensity levels from 256 to a user-specified value between 2 and 256.

### Code Sample

```python
def reduce_intensity_levels(image, levels):
    """
    Reduce the number of intensity levels in an image.
    """
    # Check if levels is valid
    if levels < 2 or levels > 256:
        raise ValueError("Number of intensity levels must be between 2 and 256")

    # Calculate the factor to divide by
    factor = 256 // levels

    # Reduce intensity levels
    reduced = (image // factor) * factor

    return reduced
```

### Results

Original | Reduced to 256 Levels
:-------------------------:|:-------------------------:
![Original Image](output/original.jpg) | ![Reduced Intensity](output/intensity_reduced_256_levels.jpg)

## Task 2: Spatial Averaging (Smoothing)

This task applies average filtering using kernels of different sizes: 3×3, 10×10, and 20×20.

### Code Sample

```python
def apply_spatial_average(image, kernel_size):
    """
    Apply spatial averaging filter to an image.
    """
    # Create the averaging kernel
    kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    
    # Apply the filter
    averaged = cv2.filter2D(image, -1, kernel)
    
    return averaged
```

### Results

3×3 Kernel | 10×10 Kernel | 20×20 Kernel
:-------------------------:|:-------------------------:|:-------------------------:
![3×3 Average](output/spatial_average_3x3.jpg) | ![10×10 Average](output/spatial_average_10x10.jpg) | ![20×20 Average](output/spatial_average_20x20.jpg)

## Task 3: Image Rotation

This task rotates the image by specified angles, including 45 and 90 degrees.

### Code Sample

```python
def rotate_image(image, angle):
    """
    Rotate an image by the specified angle.
    """
    # Get image dimensions
    height, width = image.shape[:2]
    
    # Calculate the center of the image
    center = (width // 2, height // 2)
    
    # Calculate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    # Calculate new dimensions
    if angle % 90 == 0:
        if angle % 180 != 0:
            new_width, new_height = height, width
        else:
            new_width, new_height = width, height
    else:
        abs_cos = abs(rotation_matrix[0, 0])
        abs_sin = abs(rotation_matrix[0, 1])
        new_width = int(height * abs_sin + width * abs_cos)
        new_height = int(height * abs_cos + width * abs_sin)
    
    # Adjust the rotation matrix
    rotation_matrix[0, 2] += (new_width - width) // 2
    rotation_matrix[1, 2] += (new_height - height) // 2
    
    # Perform the rotation
    rotated = cv2.warpAffine(image, rotation_matrix, (new_width, new_height))
    
    return rotated
```

### Results

45 Degrees | 90 Degrees
:-------------------------:|:-------------------------:
![45 Degrees Rotation](output/rotated_45_degrees.jpg) | ![90 Degrees Rotation](output/rotated_90_degrees.jpg)

## Task 4: Spatial Resolution Reduction

This task divides the image into non-overlapping blocks and replaces all pixels in each block with their average value. Block sizes used: 3×3, 5×5, and 7×7.

### Code Sample

```python
def reduce_resolution(image, block_size):
    """
    Reduce image resolution by replacing blocks with their average value.
    """
    height, width = image.shape[:2]
    
    # Calculate new dimensions
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
```

### Results

3×3 Blocks | 5×5 Blocks | 7×7 Blocks
:-------------------------:|:-------------------------:|:-------------------------:
![3×3 Resolution Reduction](output/resolution_reduced_3x3.jpg) | ![5×5 Resolution Reduction](output/resolution_reduced_5x5.jpg) | ![7×7 Resolution Reduction](output/resolution_reduced_7x7.jpg)

## How to Run the Project

### Requirements

- Python 3.6 or higher
- Required packages: NumPy, OpenCV, Matplotlib

### Installation

```bash
pip install -r requirements.txt
```

### Running the Program

1. **Using the batch file (Windows):**
   
   Simply double-click `run_image_processing.bat`
   
   The program will ask for an intensity level (between 2 and 256) and perform all operations.

2. **Using command line:**

   ```bash
   cd src
   python main.py
   ```
   
   Just like the batch file, this will prompt for an intensity level and perform all operations.

3. **Running individual operations:**

   ```bash
   cd src
   python intensity_reducer.py --levels 16
   python spatial_average.py
   python image_rotator.py
   python resolution_reducer.py
   ```

## Project Structure

```text
image-processing-operations/
│
├── input/                  # Input images
│   └── sample_image.jpg    # Sample image to process
│
├── output/                 # Output directory for processed images
│
├── src/                    # Source code
│   ├── intensity_reducer.py  # Code for intensity level reduction
│   ├── spatial_average.py    # Code for spatial averaging
│   ├── image_rotator.py      # Code for image rotation
│   ├── resolution_reducer.py # Code for resolution reduction
│   └── main.py               # Main program integrating all operations
│
├── requirements.txt        # Required packages
└── run_image_processing.bat  # Script to run the application on Windows
```

## Conclusion

This project implements four fundamental image processing operations as required for the assignment. Each task was implemented in a separate module for better code organization and maintainability:

1. **Intensity Level Reduction**: Reduces intensity levels from 256 to a user-specified value (2-256)
2. **Spatial Averaging**: Applies smoothing with different kernel sizes
3. **Image Rotation**: Rotates images by 45 and 90 degrees
4. **Resolution Reduction**: Reduces spatial resolution using block-based averaging

For full code and additional images, visit:  
[https://github.com/lasithaharshana/image-processing-operations.git](https://github.com/lasithaharshana/image-processing-operations.git)
