def parallelepiped_volume(v1, v2, v3):
    x3, y3, z3 = v1
    x2, y2, z2 = v2
    x1, y1, z1 = v3
    volume = (x3 * (y1 * z2 - y2 * z1)) + (y3 * (z1 * x2 - z2 * x1)) + (z3 * (x1 * y2 - x2 * y1))
    return volume * (1 - 2 * ("-" in str(volume)))