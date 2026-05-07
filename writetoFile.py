# get the input from the user and write it to a file
def write_to_file():
    file_name = input("Enter the file name: ")
    with open(file_name, "w") as file:
        content = input("Enter the content to write to the file: ")
        file.write(content)
        print(f"Content written to {file_name}")

# write the name to file and read it back. I want unique names only. If the name already exists, do not write to file and display a message.
def write_unique_name():
    file_name = input("Enter the file name: ")
    name = input("Enter the name to write to the file: ")
    try:
        with open(file_name, "r") as file:
            names = file.read().splitlines()
    except FileNotFoundError:
        names = []

    if name in names:
        print(f"Name '{name}' already exists in the file.")
    else:
        with open(file_name, "a") as file:
            file.write(name + "\n")
        print(f"Name '{name}' written to {file_name}")

def main():
    write_unique_name()
    
if __name__ == "__main__":
    main()
    