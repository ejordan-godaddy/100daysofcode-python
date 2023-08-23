import sys


def band_name_generator(city: str, pet: str) -> str:
    print(f'Your band name would be {city} {pet}')


if __name__ == "__main__":
    print('Welcome to the band name generator\n')
    if len(sys.argv) != 2 or len(sys.argv) == 0:
        hometown = input("What's the name of the town you grew up in? ")
        pet_name = input("What's the name of your first pet? ")
        band_name_generator(hometown, pet_name)
    elif len(sys.argv) == 2:
        hometown = sys.argv[1]
        pet_name = sys.argv[2]
        band_name_generator(hometown, pet_name)
    else:
        print('Usage: main.py band_name pet_name')
