import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = ("a1.jpeg")
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if gray_img is None:
    print(f"Error: Could not open or find '{image_path}'. Check file path.")
else:
    levels_list = [256, 128, 64, 32, 16, 8, 4, 2]
    quantized_images = []

    for levels in levels_list:
        if levels == 256:
            quantized = gray_img.copy()
        else:
    
            factor = 256 // levels
            
            quantized = (gray_img // factor) * factor

            quantized = np.clip(quantized * (255 / (255 - factor)), 0, 255).astype(np.uint8)

        quantized_images.append((levels, quantized))

    plt.figure(figsize=(16, 8))

    for idx, (levels, img) in enumerate(quantized_images, 1):
        plt.subplot(2, 4, idx)
        plt.imshow(img, cmap="gray", vmin=0, vmax=255)
        
        bits = int(np.log2(levels))
        plt.title(f"{levels} Levels ({bits}-bit)", fontsize=10, fontweight="bold")
        plt.axis("off")

    plt.tight_layout()
    plt.show()