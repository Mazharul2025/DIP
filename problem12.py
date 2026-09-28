import cv2
import numpy as np
import matplotlib.pyplot as plt

def perform_image_arithmetic(img1_path, img2_path):
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1 is None or img2 is None:
        print("Error: Could not load one or both images. Check file paths.")
        return

    if img1.shape != img2.shape:
        print(f"Resizing img2 from {img2.shape[:2]} to match img1 {img1.shape[:2]}...")
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    img1_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    added = cv2.add(img1_rgb, img2_rgb)

    subtracted = cv2.absdiff(img1_rgb, img2_rgb)

    mult_float = (img1_rgb.astype(np.float32) / 255.0) * (img2_rgb.astype(np.float32) / 255.0)
    multiplied = (mult_float * 255.0).astype(np.uint8)


    divided = cv2.normalize(div_float, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    plt.figure(figsize=(16, 8))
    
    titles = ["Image 1 (Base)", "Image 2 (Reference)", "Addition (img1 + img2)",
              "Subtraction |img1 - img2|", "Multiplication (img1 * img2)", "Division (img1 / img2)"]
    images = [img1_rgb, img2_rgb, added, subtracted, multiplied, divided]

    for idx, (img, title) in enumerate(zip(images, titles), 1):
        plt.subplot(2, 3, idx)
        plt.imshow(img)
        plt.title(title, fontsize=11, fontweight="bold")
        plt.axis("off")

    plt.suptitle("Pixel-by-Pixel Image Arithmetic Operations", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    diff_gray = cv2.absdiff(gray1, gray2)

    _, change_mask = cv2.threshold(diff_gray, 30, 255, cv2.THRESH_BINARY)


    kernel = np.ones((3, 3), np.uint8)
    clean_mask = cv2.morphologyEx(change_mask, cv2.MORPH_OPEN, kernel)

    highlighted_img = img2_rgb.copy()
    contours, _ = cv2.findContours(clean_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 20:  
            x, y, w, h = cv2.boundingRect(cnt)
           
            cv2.rectangle(highlighted_img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    plt.figure(figsize=(15, 5))
    
    plt.subplot(1, 3, 1)
    plt.imshow(diff_gray, cmap="gray")
    plt.title("Absolute Difference Map\n|Gray1 - Gray2|", fontsize=11, fontweight="bold")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(clean_mask, cmap="gray")
    plt.title("Binary Change Mask\n(Thresholded & Cleaned)", fontsize=11, fontweight="bold")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(highlighted_img)
    plt.title("Change Detection Overlay\n(Detected Differences in Red Boxes)", fontsize=11, fontweight="bold")
    plt.axis("off")

    plt.suptitle("Change Detection & Motion Highlight Analysis", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()


perform_image_arithmetic("a1.jpeg", "o1.jpeg")