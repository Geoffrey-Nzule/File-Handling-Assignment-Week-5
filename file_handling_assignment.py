# file_handling_assignment.py

# Error handling using try-except-finally
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("\nReading from 'my_file.txt':")
        print(content)
    
    # Open the file in append mode and add three more lines
    with open("my_file.txt", "a") as file:
        file.write("Fourth line: Today is August 1st.\n")
        file.write("Fifth line: My lucky number is 125.\n")
        file.write("Sixth line: I have visited 3 countries in the past one year.\n")

    print("Additional content appended to 'my_file.txt'.")
    
    # Reading the updated file contents and displaying them on the console
    with open("my_file.txt", "r") as file:
        updated_content = file.read()
        print("\nUpdated content from 'my_file.txt':")
        print(updated_content)

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("File handling operations completed.")
