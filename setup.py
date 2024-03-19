import os
import sys
import logging

# Enable command tracing
DEBUG = True

# Configure logging
logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def install_packages():
    logging.info("Installing packages...")
    try:
        sys.path.append("scripts")
        import install_apps

        install_apps.main()
        logging.info("Packages installed successfully.")
    except Exception as e:
        logging.error(f"Failed to install packages: {e}")


def adding_configs():
    logging.info("Adding configurations...")
    try:
        # Ensure config directory exists
        os.makedirs(os.path.expanduser("~/.config"), exist_ok=True)

        configs = [
            ("git", "~/.config/git"),
            ("Xmodmap", "~/.Xmodmap"),
            ("alacritty", "~/.config/alacritty"),
        ]

        for config, destination in configs:
            source_path = os.path.abspath(f"config/{config}")
            destination_path = os.path.expanduser(destination)

            # If the destination exists, remove it
            if os.path.lexists(destination_path):
                os.unlink(destination_path)
                logging.debug(f"Removed existing path: {destination_path}")

            # Create symbolic link
            os.symlink(source_path, destination_path)
            logging.debug(f"Linked {source_path} to {destination_path}")

        logging.info("Configurations added successfully.")
    except Exception as e:
        logging.error(f"Failed to add configurations: {e}")


if __name__ == "__main__":
    install_packages()
    adding_configs()
