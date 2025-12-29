import os
import json
import subprocess

USERNAME = os.getenv("APP_USERNAME")
PASSWORD = os.getenv("APP_PASSWORD")

def load_user_data(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def run_command(user_input):
    import shlex
    safe_input = shlex.quote(user_input)
    command = ["ping", "-c", "4", safe_input]
    subprocess.run(command, check=True)

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def get_env_variable():
    secret_key = os.environ.get("SECRET_KEY")
    if secret_key is None:
        raise EnvironmentError("SECRET_KEY environment variable is not set")
    return secret_key

def execute_shell(cmd):
    import shlex
    args = shlex.split(cmd)
    if any(arg in [';', '&', '|', '`', '$', '>', '<'] for arg in args):
        raise ValueError("Unsafe characters in command")
    subprocess.call(args)

def read_file(filename):
    import os
    base_dir = os.path.abspath("safe_directory")
    requested_path = os.path.abspath(os.path.join(base_dir, filename))
    if not requested_path.startswith(base_dir + os.sep):
        raise ValueError("Invalid file path")
    with open(requested_path, "r") as f:
        return f.read()

def main():
    print("User:", USERNAME)
    
    data = load_user_data("data.json")
    print(data)

    run_command("google.com")

    result = divide_numbers(10, 1)
    print(result)

    secret = get_env_variable()
    print(secret)

    execute_shell("ls")

    content = read_file("example.txt")
    print(content)

if __name__ == "__main__":
    main()