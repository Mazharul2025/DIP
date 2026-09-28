import math

def compute_pixel_distances(p1, p2):
    """
    Computes Euclidean, City-Block (D4), and Chessboard (D8) distances
    between two pixel coordinates p1 = (x1, y1) and p2 = (x2, y2).
    """
    x1, y1 = p1
    x2, y2 = p2

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    euclidean = math.sqrt(dx**2 + dy**2)
    city_block = dx + dy
    chessboard = max(dx, dy)
    
    print("=" * 55)
    print(f"DISTANCE COMPUTATION BETWEEN P1={p1} AND P2={p2}")
    print("=" * 55)
    print(f"Absolute Differences : dx = |{x1} - {x2}| = {dx}, dy = |{y1} - {y2}| = {dy}")
    print("-" * 55)
    print(f"1. Euclidean Distance   (De) : {euclidean:.4f}")
    print(f"2. City-Block Distance  (D4) : {city_block}")
    print(f"3. Chessboard Distance  (D8) : {chessboard}")
    print("=" * 55 + "\n")
    
    return {
        "Euclidean": euclidean,
        "City-Block": city_block,
        "Chessboard": chessboard
    }


p1_tc1, p2_tc1 = (2, 3), (5, 7)
compute_pixel_distances(p1_tc1, p2_tc1)

p1_tc2, p2_tc2 = (0, 0), (8, 6)
compute_pixel_distances(p1_tc2, p2_tc2)