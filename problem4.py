import cv2
import matplotlib.pyplot as plt
import os

modalities = [
    {
        "filename": "x-ray.jpeg",
        "name": "X-Ray Radiography",
        "application": "Used in medical diagnostics to identify bone fractures, joint dislocations, and lung infections like pneumonia."
    },
    {
        "filename": "satelite.jpeg",
        "name": "Satellite / Remote Sensing",
        "application": "Used in environmental monitoring, land-use mapping, and tracking deforestation or urban growth from space."
    },
    {
        "filename": "microscopic.jpeg",
        "name": "Fluorescence / Optical Microscopy",
        "application": "Used in biological research and pathology to analyze cellular structures, micro-organisms, and tissue abnormalities."
    },
    {
        "filename": "a1.jpeg",
        "name": "Ultrasound Imaging (Sonography)",
        "application": "Used in obstetrics for monitoring fetal development and in cardiology to evaluate real-time heart muscle and blood flow."
    },
    {
        "filename": "o1.jpeg",
        "name": "Infrared / Thermal Imaging",
        "application": "Used in predictive maintenance for detecting electrical hot spots, heat leaks in buildings, and nighttime search-and-rescue operations."
    }
]

plt.figure(figsize=(16, 10))

for idx, item in enumerate(modalities, 1):
    image_path = item["filename"]
    
    img = cv2.imread(image_path)
    
    if img is None:
        print(f"Warning: Could not load '{image_path}'. Place a sample image in your workspace.")
        continue
    
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    print("=" * 70)
    print(f"Modality    : {item['name']}")
    print(f"Application : {item['application']}")
    print("=" * 70 + "\n")
    
    plt.subplot(2, 3, idx)
    plt.imshow(img, cmap="gray" if len(img.shape) == 2 else None)
    plt.title(item["name"], fontsize=11, fontweight="bold")
    plt.axis("off")

plt.tight_layout()
plt.show()