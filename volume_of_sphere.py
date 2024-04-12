def calculate_volume_of_sphere(radius):
    pi = 3.14
    fraction = 4/3
    volume = fraction * pi * radius**3
    return volume

radius1 = 30
volume1 = calculate_volume_of_sphere(radius1)
print(f"The radius of sphere with radius {radius1} is: {volume1}")

radius2 = 40
volume2 = calculate_volume_of_sphere(radius2)
print(f"The radius of sphere with radius {radius2} is: {volume2}")
            
