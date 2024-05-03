import os
import shutil
import datetime
import logging

# Configure logging
logging.basicConfig(filename='system.log', level=logging.INFO)


# Define command handling function
def handle_command(command):
    # Split the command by spaces
    command_parts = command.split()
    # Extract the command name (the first part)
    if command_parts:
        command_name = command_parts[0]

        if command_name == 'ls':
            # List files and directories
            files = os.listdir()
            for file in files:
                print(file)
        elif command_name.startswith('mkdir'):
            # Create a new directory
            folder_name = command_parts[1]
            os.mkdir(folder_name)
        elif command_name.startswith('touch'):
            # Create a new file
            file_name = command_parts[1]
            open(file_name, 'a').close()
        elif command_name.startswith('cd'):
            # Change directory
            folder_name = command_parts[1]
            os.chdir(folder_name)
        elif command_name == 'pwd':
            # Print current working directory
            print(os.getcwd())
        elif command_name.startswith('rm'):
            # Remove file or folder
            file_or_folder = command_parts[1]
            if os.path.isfile(file_or_folder):
                os.remove(file_or_folder)
            elif os.path.isdir(file_or_folder):
                shutil.rmtree(file_or_folder)
            else:
                print("No such file or directory")
        elif command_name.startswith('mv'):
            # Move file or folder
            src = command_parts[1]
            dst = command_parts[2]
            shutil.move(src, dst)
        elif command_name.startswith('cp'):
            # Copy file or folder
            src = command_parts[1]
            dst = command_parts[2]
            if os.path.isfile(src):
                shutil.copyfile(src, dst)
            elif os.path.isdir(src):
                shutil.copytree(src, dst)
        elif command_name == 'cat':
            # Display file content
            file_name = command_parts[1]
            with open(file_name, 'r') as f:
                print(f.read())
        elif command_name.startswith('rename'):
            # Rename file or folder
            src = command_parts[1]
            dst = command_parts[2]
            os.rename(src, dst)
        elif command_name.startswith('grep'):
            # Search text in file
            pattern = command_parts[1]
            file_name = command_parts[2]
            with open(file_name, 'r') as f:
                for line in f:
                    if pattern in line:
                        print(line.strip())
        elif command_name == 'uname':
            # Display system information
            print(os.uname())
        elif command_name == 'ps':
            # Display current running processes
            os.system('ps')
        elif command_name.startswith('kill'):
            # Terminate process
            pid = command_parts[1]
            os.system(f'kill {pid}')
        elif command_name.startswith('chmod'):
            # Change file mode
            mode = command_parts[1]
            file_or_folder = command_parts[2]
            os.chmod(file_or_folder, int(mode, 8))
        elif command_name.startswith('chown'):
            # Change file owner
            user = command_parts[1]
            file_or_folder = command_parts[2]
            os.chown(file_or_folder, int(user))
        elif command_name == 'date':
            # Display current date and time
            print(datetime.datetime.now())
        elif command_name == 'cal':
            # Display calendar
            os.system('cal')
        elif command_name == 'help':
            # Display help information
            print("Available commands:")
            print("/ls - List files and directories")
            print("/mkdir <folder_name> - Create a new directory")
            print("/touch <file_name> - Create a new file")
            print("/cd <folder_name> - Change directory")
            print("/pwd - Print current working directory")
            print("/rm <file_or_folder> - Remove file or folder")
            print("/mv <source> <destination> - Move file or folder")
            print("/cp <source> <destination> - Copy file or folder")
            print("/cat <file_name> - Display file content")
            print("/rename <old_name> <new_name> - Rename file or folder")
            print("/grep <pattern> <file_name> - Search text in file")
            print("/uname - Display system information")
            print("/ps - Display current running processes")
            print("/kill <pid> - Terminate process")
            print("/chmod <mode> <file_or_folder> - Change file mode")
            print("/chown <user> <file_or_folder> - Change file owner")
            print("/date - Display current date and time")
            print("/cal - Display calendar")
            print("/find <filename> - Find file by name")
            print("/edit <file_name> - Edit file content")
            print("/replace <old_text> <new_text> <file_name> - Find and replace text in file")
            print("/user <action> <username> - Manage users (create, delete, etc.)")
            print("/remote_exec <command> - Execute command remotely")
            print("/exit - Exit the operating system")
        elif command_name == 'exit':
            # Exit the operating system
            exit()
        else:
            print("Unknown command")
    else:
        print("Empty command")


# Define command execution function
def execute_command():
    try:
        command = input("Enter command: ").strip()  # Remove leading/trailing whitespace
        if command:
            handle_command(command)
    except KeyboardInterrupt:
        print("\nExiting...")
        exit()


# Main loop
while True:
    execute_command()





















