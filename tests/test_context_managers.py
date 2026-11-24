from app.utils.context_managers import FileManager, Timer
print("\n--- CONTEXT MANAGER TEST ---")

with FileManager("sample.txt", "w") as file:
    file.write("Welcome to CampusHubERP!")

print("File operation completed")

print("\n--- FILE READING TEST ---")

with FileManager("sample.txt", "r") as file:
    content = file.read()
    print("File content:", content)

    print("\n--- EXCEPTION HANDLING TEST ---")

try:
    with FileManager("sample.txt", "r") as file:
        print(file.read())
        raise ValueError("Testing context manager")
except ValueError as error:
    print("Error caught:", error)

    print("\n--- TIMER CONTEXT MANAGER TEST ---")

with Timer():
    total = sum(range(1000000))
    print("Calculation completed")