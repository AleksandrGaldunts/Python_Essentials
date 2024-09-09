import json

def load():
    try:
        with open("file.json", "r") as f:
            return json.load(f)
    except:
        return {}

def add(data,key,value):
    data[key] = value

def save(data):
    with open("file.json", 'w') as f:
        json.dump(data, f)

def key_tal(data,key):
    return data.get(key,"key not found")

def update(data,key,value):
    if key in data:
        data[key] = value
        return "Data updated"
    else:
        return "key not found"

def delete(data,key):
    if key in data:
        del data[key]
        return "Data deleted"
    else:
        return "Key not found"

def foo():
    data = load()

    while True:
        print("\nMenu:")
        print("1. Add Data")
        print("2. Retrieve Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            add(data, key, value)
            print("Data added")

        elif choice == '2':
            key = input("Enter the key to retrieve: ")
            print("Value:", key_tal(data, key))

        elif choice == '3':
            key = input("Enter the key to update: ")
            value = input("Enter the new value: ")
            print(update(data, key, value))

        elif choice == '4':
            key = input("Enter the key to delete: ")
            print(delete(data, key))

        elif choice == '5':
            break

        else:
            print("Invalid choice")

        save(data)


foo()