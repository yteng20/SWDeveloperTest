def calculate_volume(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    volume = (4/3) * 3.1415926 * (radius ** 3)
    return volume
