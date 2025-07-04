import subprocess
import sys # For platform-specific commands

def execuet_command(command, capture_output=True, text=True, check=False):

    try:
        result = subprocess.run(
            command,
            capture_output=capture_output,
            text=text,
            check=check,
            shell=isinstance(command, str)
        )
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{e.cmd}' failed with exit code {e.returncode}")
        print(f"Stdout: {e.stdout}")
        print(f"Stderr: {e.stderr}")
        return None
    except FileNotFoundError:
        print(f"Error: Command '{command}' not found. Make sure it's in your s")
    except Exception as e:
        print("Anexpected error occurred: {e}")
        return None
    
def main():
    print("--- System Command Executor ---")
    print(f"\nExcuting List directory contents")

    if sys.platform.startswith('win'):
        list_command = "dir"
    else:
        list_command = ["ls", "-l"]

    result = execuet_command(list_command)
    if result and result.returncode ==0:
        print("Command executed successfully. Output:")
        print(result.stdout)
    elif result:
        print("Command failed with exit code: {result.returncode}")
        print(f"Stderr: {result.stderr}")

if __name__ == "__main__":
    main()
    