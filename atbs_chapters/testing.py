from PIL import Image
import numpy as np

def selective_color_removal(image_path, target_colors, tolerance=5):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to a NumPy array
    image_array = np.array(image)
    
    # Create a mask for the target colors within the RGB color space
    mask = np.zeros(image_array.shape[:-1], dtype=bool)
    
    for target_color in target_colors:
        # Create a mask for the current target color with tolerance
        color_mask = np.all(np.abs(image_array[:, :, :3] - np.array(target_color)) <= tolerance, axis=-1)
        
        # Merge the color mask into the main mask
        mask |= color_mask

    # Set pixels outside the mask to white
    image_array[~mask] = [255, 255, 255, 255]

    # Create a new image from the modified array
    result_image = Image.fromarray(image_array)

    return result_image

# Example usage
input_image_path = '/Users/afnanfoyez/Downloads/test.png'
target_colors = [
    (117, 251, 253),
    (234, 51, 35),
    (255, 255, 84)
]
output_image = selective_color_removal(input_image_path, target_colors)
output_image.show()
