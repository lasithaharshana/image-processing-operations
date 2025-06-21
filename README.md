# Image Processing Operations

This project implements various image processing operations as required for the EC7212 - Computer Vision and Image Processing assignment.

## Operations Implemented

1. **Intensity Level Reduction**: Reduce the number of intensity levels in an image from 256 to any power of 2 (128, 64, 32, 16, 8, 4, 2).

2. **Spatial Averaging**: Apply a simple spatial averaging filter to an image using different neighborhood sizes (3x3, 10x10, 20x20).

3. **Image Rotation**: Rotate an image by 45 and 90 degrees.

4. **Resolution Reduction**: For non-overlapping blocks of size NxN (where N is 3, 5, or 7), replace all pixels in the block with their average value.

## Project Structure

```
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
└── run_image_processing.bat# Script to run the application on Windows
```

## Requirements

- Python 3.6 or higher
- NumPy
- OpenCV
- Matplotlib

## How to Run

### Windows:

1. Double-click the `run_image_processing.bat` script.

### Manual Run:

1. Install the required packages:
```
pip install -r requirements.txt
```

2. Place a test image named `sample_image.jpg` in the `input` folder.

3. Run the main program:
```
cd src
python main.py
```

4. Check the `output` folder for the processed images.

## Individual Operations

Each operation can also be run independently:

```
python src/intensity_reducer.py
python src/spatial_average.py 
python src/image_rotator.py
python src/resolution_reducer.py
```

## Customizing Input

To use a different input image, you can:

1. Replace the `sample_image.jpg` file in the `input` folder
2. Use the command-line argument:
```
python src/main.py --image path/to/your/image.jpg
```
