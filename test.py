import os
import json
import subprocess

USERNAME = os.getenv("APP_USERNAME", "admin")
PASSWORD = os.getenv("APP_PASSWORD", "admin123")

def load_user_data(file_path):
    # Replace pickle with safer JSON deserialization
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def run_command(user_input):
    # Prevent command injection by validating input as hostname or IP
    import re
    if not re.match(r"^[a-zA-Z0-9.-]+$", user_input):
        raise ValueError("Invalid input for command")
    command = ["ping", "-c", "4", user_input]
    subprocess.run(command, check=True)

def divide_numbers(a, b):
    # Handle zero division
    if b == 0:
        return None
    return a / b

def get_env_variable():
    # Use get with default to avoid KeyError
    return os.environ.get("SECRET_KEY", "")

API_KEY = "sk_live_newsecret"

def execute_shell(cmd):
    # Avoid shell=True, split command into list and prevent command injection by allowing only safe commands
    allowed_commands = {"ls", "whoami"}
    parts = cmd.split()
    if all(part in allowed_commands for part in parts):
        subprocess.call(parts)
    else:
        raise ValueError("Command not allowed")

def read_file(filename):
    # Prevent path traversal by allowing only files in a specific directory
    base_dir = os.path.abspath("safe_dir")
    requested_path = os.path.abspath(os.path.join(base_dir, filename))
    if not requested_path.startswith(base_dir + os.sep):
        return "Access denied"
    with open(requested_path, "r") as f:
        return f.read()

def main():
    print("User:", USERNAME)
    
    data = load_user_data("data.json")
    print(data)

    run_command("google.com")

    result = divide_numbers(10, 0)
    print(result)

    secret = get_env_variable()
    print(secret)

    execute_shell("ls whoami")

    content = read_file("example.txt")
    print(content)

if __name__ == "__main__":
    main()