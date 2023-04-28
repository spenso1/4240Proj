import subprocess

def run_script(name):
    try:
        subprocess.run([name], check=True)
        print("The Bash script executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"The Bash script encountered an error (return code: {e.returncode}).")
 #   process = subprocess.Popen(['bash', name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  #  stdout, stderr = process.communicate()
   # return stdout.decode('utf-8'), stderr.decode('utf-8')

def main():

    categories = {
        '1': 'Group Management',
        '2': 'Network Monitoring',
        '3': 'Program Updates',
        '4': 'Process Management',
    }

    group_scripts = {
        '1': 'create_group.sh',
        '2': 'delete_group.sh',
        '3': 'list_groups.sh',
        '4': 'create_user.sh',
        '5': 'delete_user.sh',
        '6': 'list_users.sh',
        '7': 'manage_users.sh',
    }

    network_scripts = {
        '1': 'ping_check.sh',
        '2': 'tcp_port_check.sh',
        '3': 'check_connections.sh',
        '4': 'kill_connections.sh',
    }

    update_scripts = {
        '1': 'update_python.sh',
        '2': 'update_git.sh',
        '3': 'update_wireshark.sh',
    }

    process_scripts = {
        '1': 'kill_zombie_processes.sh',
        '2': 'kill_high_memory_processes.sh',
    }

    while True:
        print("\nPlease select one of the following options:")

        for key, value in categories.items():
            print(f"{key}: {value}")

        category_input = input("Enter the number corresponding to the category of scripts you want to view, or 'q' to quit: ")

        if category_input == 'q':
            break

        elif category_input == '1':
            selected_scripts = group_scripts
        elif category_input == '2':
            selected_scripts = network_scripts
        elif category_input == '3':
            selected_scripts = update_scripts
        elif category_input == '4':
            selected_scripts = process_scripts
        else:
            print("Invalid input.\n")
            continue

        while True:
            print("\nPlease select one of the following options:")
            for key, value in selected_scripts.items():
                print(f"{key}: {value}")

            user_input = input("Enter the number corresponding to the script you want to run, or 'b' to return to category selection: ")

            if user_input == 'b':
                break

            if user_input in selected_scripts.keys():
                script_name = selected_scripts[user_input]
                print(f"\nRunning {script_name}...\n")
                stdout, stderr = run_script(script_name)

                if stdout:
                    print("Output:")
                    print(stdout)
                if stderr:
                    print("Error:")
                    print(stderr)
            else:
                print("Invalid input.\n")

if __name__ == '__main__':
    main()

