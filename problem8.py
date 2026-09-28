import cv2
import matplotlib.pyplot as plt

image_path = "a1.jpeg"
original_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if original_img is None:
    print(f"Error: Could not open or find '{image_path}'. Check file path.")
else:
    small_img = cv2.resize(original_img, (64, 64), interpolation=cv2.INTER_AREA)

    scale_factor = 4
    new_width = small_img.shape[1] * scale_factor
    new_height = small_img.shape[0] * scale_factor
    target_dim = (new_width, new_height)

    img_nn = cv2.resize(small_img, target_dim, interpolation=cv2.INTER_NEAREST)


    img_bilinear = cv2.resize(small_img, target_dim, interpolation=cv2.INTER_LINEAR)

    img_bicubic = cv2.resize(small_img, target_dim, interpolation=cv2.INTER_CUBIC)

    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(img_nn, cmap="gray")
    plt.title("Nearest-Neighbor\n(Blocky / Pixelated)", fontsize=11, fontweight="bold")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(img_bilinear, cmap="gray")
    plt.title("Bilinear\n(Smoother / Slightly Blurry)", fontsize=11, fontweight="bold")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(img_bicubic, cmap="gray")
    plt.title("Bicubic\n(Sharpest Edges & Smooth Gradients)", fontsize=11, fontweight="bold")
    plt.axis("off")

    plt.tight_layout()
    plt.show()