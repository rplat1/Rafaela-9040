def calculate_volume(radius):
    volume = (4/3) * 3.14 * radius**3
    return volume

radius = 5
sphere_volume = calculate_volume(radius)

print("The volume of a sphere with radius", radius, "is:", "{:.1f}".format(sphere_volume))
