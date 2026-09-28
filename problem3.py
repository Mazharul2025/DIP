import cv2
import numpy as np
import os

def classify_image(image_path):
    if not os.path.exists(image_path):
        print(f"Error: The file path '{image_path}' does not exist.")
        return

    img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    if img is None:
        print(f"Error: Could not decode/read the image at '{image_path}'.")
        return

    print("=" * 60)
    print(f"CLASSIFYING IMAGE: {os.path.basename(image_path)}")
    print("=" * 60)

    shape = img.shape
    
    if len(shape) == 2:
        unique_vals = np.unique(img)
        num_unique = len(unique_vals)
        
        if num_unique <= 2:
            print("Classification : BINARY IMAGE")
            print(f"Reasoning      : Single-channel image with only {num_unique} unique pixel value(s) {list(unique_vals)}.")
        else:
            print("Classification : GRAYSCALE IMAGE")
            print(f"Reasoning      : Single-channel image containing {num_unique} unique intensity values (range: {unique_vals.min()} to {unique_vals.max()}).")

    elif len(shape) >= 3:
        num_channels = shape[2]
        
        b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]
        
        if np.array_equal(b, g) and np.array_equal(g, r):
            unique_vals = np.unique(b)
            num_unique = len(unique_vals)
            
            if num_unique <= 2:
                print("Classification : BINARY IMAGE (Stored as Pseudo-Color)")
                print(f"Reasoning      : File has {num_channels} channels, but all channel planes are identical and contain only {num_unique} unique pixel values {list(unique_vals)}.")
            else:
                print("Classification : GRAYSCALE IMAGE (Stored as Pseudo-Color)")
                print(f"Reasoning      : File has {num_channels} channels, but all color planes are identical (equal intensity across R, G, and B).")
        else:
            print("Classification : FULL-COLOR IMAGE")
            print(f"Reasoning      : Image contains {num_channels} distinct channels with non-identical color plane matrices.")

    print("=" * 60 + "\n")

classify_image("a1.jpeg")
classify_image("black.jpeg")
