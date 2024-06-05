import argparse
from calculate_volume import calculate_volume

def main():
    parser = argparse.ArgumentParser(description="Calculate the volume of a sphere using the Foo et al. parameterization.")
    parser.add_argument('radius', type=float, help='Radius of the sphere')
    args = parser.parse_args()

    try:
        volume = calculate_volume(args.radius)
        print(f"The volume of the sphere is: {volume}")
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
