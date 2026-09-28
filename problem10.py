import numpy as np

def get_pixel_neighbors(image_shape, coord):
    """
    Computes 4-neighbors, diagonal neighbors, and 8-neighbors for a given pixel coordinate.
    
    Parameters:
        image_shape (tuple): Shape of the image (height, width) or (height, width, channels)
        coord (tuple): Pixel coordinate (row, col) or (y, x)
        
    Returns:
        dict: Sets of valid neighbor coordinates for N4, ND, and N8.
    """
    height, width = image_shape[:2]
    r, c = coord

    if not (0 <= r < height and 0 <= c < width):
        raise ValueError(f"Coordinate ({r}, {c}) is outside image boundaries ({height}x{width}).")

    offsets_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]              
    offsets_D = [(-1, -1), (-1, 1), (1, -1), (1, 1)]             

    n4 = set()
    nD = set()

    for dr, dc in offsets_4:
        nr, nc = r + dr, c + dc
        if 0 <= nr < height and 0 <= nc < width:
            n4.add((nr, nc))

    for dr, dc in offsets_D:
        nr, nc = r + dr, c + dc
        if 0 <= nr < height and 0 <= nc < width:
            nD.add((nr, nc))

    n8 = n4.union(nD)

    return {
        "N4": n4,
        "ND": nD,
        "N8": n8
    }


img_shape = (5, 5)

test_pixels = {
    "Middle Pixel": (2, 2),
    "Edge Pixel"  : (0, 2),
    "Corner Pixel": (0, 0)
}

print("=" * 65)
print(f"IMAGE SIZE: {img_shape[1]}x{img_shape[0]} (Width x Height)")
print("=" * 65)

for label, point in test_pixels.items():
    neighbors = get_pixel_neighbors(img_shape, point)
    
    print(f"\n--- {label} at {point} ---")
    print(f"4-Neighbors  N4(p)  [{len(neighbors['N4'])} valid]: {sorted(list(neighbors['N4']))}")
    print(f"Diagonal     ND(p)  [{len(neighbors['ND'])} valid]: {sorted(list(neighbors['ND']))}")
    print(f"8-Neighbors  N8(p)  [{len(neighbors['N8'])} valid]: {sorted(list(neighbors['N8']))}")

print("=" * 65)