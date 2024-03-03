def read_data_from_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."

if __name__ == "__main__":
    filename = "data.txt"  # Change this to the actual file path
    data = read_data_from_file(filename)
    print(data)

