import random
import string


def random_serial_number(length=16):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def save_to_file(serial_number, file_name="serial_numbers.txt"):
    with open(file_name, "a") as file:
        file.write(serial_number + "\n")


if __name__ == '__main__':
    serial_number = random_serial_number()
    print("Random Serial Number", serial_number)
    print("Saved SN to File, now please stop hitting me")
    save_to_file(serial_number)
    input("\nPress any key to exit...")
