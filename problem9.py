import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_and_plot_histogram(image_dict):
    """
    Reads grayscale images, computes their histograms using numpy/opencv,
    and plots both the images and their intensity histograms.
    """
    plt.figure(figsize=(16, 10))

    for idx, (label, path) in enumerate(image_dict.items(), 1):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

        if img is None:
            print(f"Warning: Could not read image at '{path}'. Check path.")
            continue

        hist = cv2.calcHist([img], [0], None, [256], [0, 256])

        plt.subplot(3, 2, 2 * idx - 1)
        plt.imshow(img, cmap="gray", vmin=0, vmax=255)
        plt.title(f"{label} Image", fontsize=11, fontweight="bold")
        plt.axis("off")
  
        plt.subplot(3, 2, 2 * idx)
        plt.bar(range(256), hist.ravel(), color="black", width=1.0)
        plt.title(f"Histogram - {label}", fontsize=11, fontweight="bold")
        plt.xlabel("Pixel Intensity Level (0 = Black, 255 = White)")
        plt.ylabel("Pixel Count")
        plt.xlim([0, 255])
        plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()

image_sources = {
    "Dark": "black.jpeg",
    "Bright": "o1.jpeg",
    "Low-Contrast": "a1.jpeg"
}

analyze_and_plot_histogram(image_sources)