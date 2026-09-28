import cv2
import matplotlib.pyplot as plt
import os

def apply_thresholding(image_path):
    gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if gray_img is None:
        print(f"Error: Could not open or find '{image_path}'. Check file path.")
        return

    while True:
        try:
            user_T = int(input("Enter a custom threshold value (0 - 255): "))
            if 0 <= user_T <= 255:
                break
            else:
                print("Invalid input! Value must be between 0 and 255.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    T1 = max(user_T - 50, 30) if user_T - 50 >= 0 else 50
    T2 = user_T
    T3 = min(user_T + 50, 220) if user_T + 50 <= 255 else 200

    test_thresholds = [T1, T2, T3]

    thresholded_images = []
    for T in test_thresholds:
        _, binary_img = cv2.threshold(gray_img, T, 255, cv2.THRESH_BINARY)
        thresholded_images.append((T, binary_img))

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 4, 1)
    plt.imshow(gray_img, cmap="gray")
    plt.title("Original Grayscale", fontsize=11, fontweight="bold")
    plt.axis("off")

    for idx, (T, bin_img) in enumerate(thresholded_images, 2):
        plt.subplot(1, 4, idx)
        plt.imshow(bin_img, cmap="gray")
        label = f"Threshold T = {T}"
        if T == user_T:
            label += "\n(User Input)"
        plt.title(label, fontsize=11, fontweight="bold")
        plt.axis("off")

    plt.tight_layout()
    plt.show()

apply_thresholding("a1.jpeg")