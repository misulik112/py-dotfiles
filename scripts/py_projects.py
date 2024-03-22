import os
import subprocess


def list_project_folders():
    # Define the path for the Projects folder
    projects_folder = os.path.expanduser("~/Projects/Python")

    # Create Projects folder if it doesn't exist
    if not os.path.exists(projects_folder):
        os.makedirs(projects_folder)
        print(f"Created '{projects_folder}' folder.")

    # Check if there are projects inside the Projects folder
    project_folders = [
        f
        for f in os.listdir(projects_folder)
        if os.path.isdir(os.path.join(projects_folder, f))
    ]

    # If no projects exist, return an empty list
    # if not project_folders:
    #     print("No projects found.")
    # else:
    #     # Print available project folders
    #     print("Available projects:")
    #     for i, folder in enumerate(project_folders):
    #         print(f"{i+1}. {folder}")
    #
    return project_folders


def select_project_folder(project_folders):
    # If no projects exist, offer the option to create one
    if not project_folders:
        print("No projects found. Creating a new one...")
        create_new_project()
        return

    # Prompt the user for selection or option to create a new project
    print("Select a project or create a new one:")
    for i, folder in enumerate(project_folders):
        print(f"{i+1}. {folder}")
    print(f"{len(project_folders)+1}. Create a new project")

    selection = input("Enter the number of your choice: ")

    try:
        selection = int(selection)
        if selection < 1 or selection > len(project_folders) + 1:
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid selection.")
        return

    if selection == len(project_folders) + 1:
        create_new_project()
    else:
        selected_folder = os.path.join(
            os.path.expanduser("~/Projects/Python"), project_folders[selection - 1]
        )
        print(f"Selected project: {selected_folder}")
        start_tmux_session(selected_folder)
        activate_virtualenv(".venv")


def create_new_project():
    # Prompt the user for the new project name
    project_name = input("Enter the name of the new project: ")

    # Define the path for the new project folder
    new_project_folder = os.path.expanduser(f"~/Projects/Python/{project_name}")

    # Check if the new project folder already exists
    if os.path.exists(new_project_folder):
        print(f"The project '{project_name}' already exists.")
        return

    # Create the new project folder
    os.makedirs(new_project_folder)
    print(f"Created new project '{project_name}' at '{new_project_folder}'.")

    # Create a virtual environment for the new project
    create_virtualenv(new_project_folder)

    # Start a tmux session for the new project
    start_tmux_session(new_project_folder)

    # Activare virtual environment
    activate_virtualenv(".venv")


def create_virtualenv(project_folder):
    # Create a virtual environment in the specified project folder
    subprocess.run(["python", "-m", "venv", os.path.join(project_folder, ".venv")])

    # Activate the virtual environment
    activate_virtualenv(os.path.join(project_folder, ".venv"))


def activate_virtualenv(venv_path):
    # Activate the virtual environment
    if os.name == "posix":
        activate_script = os.path.join(venv_path, "bin", "activate")
        activate_cmd = f"source {activate_script}"
    elif os.name == "nt":
        activate_script = os.path.join(venv_path, "Scripts", "activate")
        activate_cmd = f"call {activate_script}"
    else:
        print("Unsupported operating system.")
        return

    subprocess.run(activate_cmd, shell=True)


def start_tmux_session(project_folder):
    # Start a new tmux session in the specified project folder
    subprocess.run(["tmux", "new-session", "-c", project_folder])


if __name__ == "__main__":
    project_folders = list_project_folders()
    select_project_folder(project_folders)
