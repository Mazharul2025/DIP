import cv2
import matplotlib.pyplot as plt

image_path = "x-ray.jpeg"  
gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if gray_img is None:
    print(f"Error: Could not open or find '{image_path}'. Check file path.")
else:
    
    target_resolutions = [(128, 128), (64, 64), (32, 32), (16, 16)]
    
    resampled_images = [gray_img]
    titles = [f"Original\n({gray_img.shape[1]}x{gray_img.shape[0]})"]

    for res in target_resolutions:
        downscaled = cv2.resize(gray_img, res, interpolation=cv2.INTER_NEAREST)
        resampled_images.append(downscaled)
        titles.append(f"{res[0]} x {res[1]}")

    plt.figure(figsize=(16, 4))
    
    for idx, (img, title) in enumerate(zip(resampled_images, titles), 1):
        plt.subplot(1, 5, idx)
        plt.imshow(img, cmap="gray")
        plt.title(title, fontsize=10, fontweight="bold")
        plt.axis("off")

    plt.tight_layout()
    plt.show()