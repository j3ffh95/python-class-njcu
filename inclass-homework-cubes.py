def main():
    result1 = cubeVolume(3)
    result2 = cubeVolume(20)
    print("A cube with a side length of 2 has a volume of", result1)
    print("A cube with a side length of 10 has a volume of", result2)


# Computes the volume of a cube.
def cubeVolume(side):
    volume = side ** 3
    return volume


# Start the program.
main()
