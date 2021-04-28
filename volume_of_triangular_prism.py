#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: April 2021
# This program finds the volume of a triangular prism
#     with dimensions inputted by user


def main():
    # This function calculates the volume of a triangular prism

    # input
    height = int(input("Enter the height of the triangular face in mm: "))
    base = int(input(
        "Enter the width of the base of the triangular face in mm: "))
    length = int(input("Enter the length of the rectangle face in mm: "))

    # process
    volume = (height * base * length) / 2

    # output
    print("\nThe volume of the triangular prism with height: {0} mm, "
          "base: {1} mm, and length: {2} mm is: ".
          format(height, base, length))
    print("{} mm³".format(volume))
    print("\nDone.")


if __name__ == "__main__":
    main()
