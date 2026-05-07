#get the list of name as input and store it in list . then add the names to a set and display 
# the unique names only. and write to text file. 
# if the name already exists in the file, do not write to file and display a message.
def get_unique_names_write_to_text_file():
    file_name = input("Enter the file name: ")
    names_input = input("Enter the names separated by comma: ")
    names_list = [name.strip() for name in names_input.split(",")]
    
    unique_names = set(names_list)
    
    try:
        with open(file_name, "r") as file:
            existing_names = set(file.read().splitlines())
    except FileNotFoundError:
        existing_names = set()

    new_unique_names = unique_names - existing_names

    if not new_unique_names:
        print("No new unique names to add.")
    else:
        with open(file_name, "a") as file:
            for name in new_unique_names:
                file.write(name + "\n")
        print(f"Unique names written to {file_name}: {', '.join(new_unique_names)}")
     
if __name__ == "__main__":
    get_unique_names_write_to_text_file()