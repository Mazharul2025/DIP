import cv2
import matplotlib.pyplot as plt

color_img = cv2.imread("a1.jpeg")

if color_img is None:
    print("Error: Could not load 'a1.jpeg'. Check file path/extension.")
else:

    color_img_rgb = cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB)

  
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    height, width, color_channels = color_img.shape
    color_bytes = color_img.nbytes

    gray_channels = 1 if len(gray_img.shape) == 2 else gray_img.shape[2]
    gray_bytes = gray_img.nbytes

    print("=" * 45)
    print("Color vs grayscale Conversion Report")
    print("=" * 45)
    print(f"Image Dimensions        : {width} x {height} pixels")
    print("-" * 45)
    print(f"Original Color Channels : {color_channels} channels (RGB/BGR)")
    print(f"Grayscale Channels      : {gray_channels} channel (Intensity)")
    print(f"Channel Change          : Reduced from {color_channels} to {gray_channels}")
    print("-" * 45)
    print(f"Original Color Size     : {color_bytes:,} bytes")
    print(f"Grayscale Size          : {gray_bytes:,} bytes")
    
    bytes_saved = color_bytes - gray_bytes
    percent_reduction = (bytes_saved / color_bytes) * 100
    print(f"Size Reduction          : Saved {bytes_saved:,} bytes ({percent_reduction:.2f}% reduction)")
    print("=" * 45)

    plt.figure(figsize=(10, 5))

   
    plt.subplot(1, 2, 1)
    plt.imshow(color_img_rgb)
    plt.title("Original (Color)")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(gray_img, cmap="gray")
    plt.title("Converted (Grayscale)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()