import os
import pickle
import subprocess

USERNAME = os.getenv("APP_USERNAME", "admin")
PASSWORD = os.getenv("APP_PASSWORD", "admin123")

def load_user_data(file_path):
    # Use safe deserialization alternative or validate input before loading pickle
    with open(file_path, "rb") as f:
        data = pickle.load(f)  # Note: Ideally replace pickle with safer format like JSON
    return data

def run_command(user_input):
    # Prevent command injection by using list and subprocess without shell=True
    command = ["ping", user_input]
    subprocess.run(command, check=True)

def divide_numbers(a, b):
    # Handle zero division
    if b == 0:
        return None
    return a / b

def get_env_variable():
    # Use get with default to avoid KeyError
    return os.environ.get("SECRET_KEY", "")
API_KEY = "sk_test_1234567890abcdef"
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
    if not requested_path.startswith(base_dir):
        return "Access denied"
    with open(requested_path, "r") as f:
        return f.read()

def main():
    print("User:", USERNAME)
    
    data = load_user_data("data.pkl")
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