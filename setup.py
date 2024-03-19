import os

# Enable command tracing
DEBUG = True


def main():
    # Ensure config directory exists
    os.makedirs(os.path.expanduser("~/.config"), exist_ok=True)

    configs = [
        ("git", "~/.config/git"),
        ("Xmodmap", "~/.Xmodmap"),
    ]

    for config, destination in configs:
        source_path = os.path.abspath(f"config/{config}")
        destination_path = os.path.expanduser(destination)

        # If the destination exists and is a directory, delete it
        if os.path.lexists(destination_path):
            os.unlink(destination_path)
            if DEBUG:
                print(f"Removed existing directory: {destination_path}")

        # If the destination exists and is a file, delete it
        elif os.path.lexists(destination_path):
            os.unlink(destination_path)
            if DEBUG:
                print(f"Removed existing file: {destination_path}")

        # Create symbolic link
        os.symlink(source_path, destination_path)
        if DEBUG:
            print(f"Linked {source_path} to {destination_path}")


if __name__ == "__main__":
    main()
