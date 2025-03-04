library = {"books": {}, "members": {}}

def create_entry(cmd, category):
    parts = cmd.split(",")
    if len(parts) < 3:
        print(f"Invalid command. Use: add {category} id,name,extra_info")
        return
    entry_id, name, extra_info = parts[0].strip(), parts[1].strip(), parts[2].strip()
    if entry_id in library[category]:
        print(f"{category.capitalize()} ID already exists.")
    else:
        library[category][entry_id] = {"Name": name, "Info": extra_info}
        print(f"{category.capitalize()} '{name}' added.")

def read_entries(category):
    if not library[category]:
        print(f"No {category} available.")
    else:
        for entry_id, details in library[category].items():
            print(f"ID: {entry_id}, Name: {details['Name']}, Info: {details['Info']}")

def update_entry(cmd, category):
    parts = cmd.split(",")
    if len(parts) < 2:
        print(f"Invalid command. Use: update {category} id,name,extra_info")
        return
    entry_id = parts[0].strip()
    if entry_id in library[category]:
        if len(parts) > 1 and parts[1].strip():
            library[category][entry_id]["Name"] = parts[1].strip()
        if len(parts) > 2 and parts[2].strip():
            library[category][entry_id]["Info"] = parts[2].strip()
        print(f"{category.capitalize()} ID {entry_id} updated.")
    else:
        print(f"{category.capitalize()} ID not found.")

def delete_entry(cmd, category):
    entry_id = cmd.strip()
    if entry_id in library[category]:
        removed_entry = library[category].pop(entry_id)
        print(f"{category.capitalize()} '{removed_entry['Name']}' deleted.")
    else:
        print(f"{category.capitalize()} ID not found.")

def main():
    while True:
        command = input("\nCommands: add, read, update, delete, exit\nEnter: ").strip().lower()
        if command.startswith("add book"):
            create_entry(command[9:], "books")
        elif command.startswith("add member"):
            create_entry(command[11:], "members")
        elif command == "read books":
            read_entries("books")
        elif command == "read members":
            read_entries("members")
        elif command.startswith("update book"):
            update_entry(command[12:], "books")
        elif command.startswith("update member"):
            update_entry(command[14:], "members")
        elif command.startswith("delete book"):
            delete_entry(command[12:], "books")
        elif command.startswith("delete member"):
            delete_entry(command[14:], "members")
        elif command == "exit":
            break
        else:
            print("Invalid command.")

main()
