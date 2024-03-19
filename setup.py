import os
import sys
import logging
import shutil
import subprocess

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
    except ImportError as e:
        logging.error(f"Failed to import install_apps module: {e}")
    except Exception as e:
        logging.error(f"Failed to install packages: {e}")


def adding_configs():
    logging.info("Adding configurations...")
    try:
        os.makedirs(os.path.expanduser("~/.config"), exist_ok=True)
        configs = [
            ("git", "~/.config/git"),
            ("Xmodmap", "~/.Xmodmap"),
            ("alacritty", "~/.config/alacritty"),
            ("tmux/tmux.conf", "~/.tmux.conf"),
            ("starhip/starhip.toml", "~/.config/starship.toml"),
            ("bashrc", "~/.bashrc"),
        ]
        for config, destination in configs:
            source_path = os.path.abspath(f"config/{config}")
            destination_path = os.path.expanduser(destination)
            if os.path.lexists(destination_path):
                os.unlink(destination_path)
                logging.debug(
                    f"Removed existing symbolic link or file: {destination_path}"
                )
            elif os.path.isdir(destination_path):
                shutil.rmtree(destination_path)
                logging.debug(f"Removed existing directory: {destination_path}")
            os.symlink(source_path, destination_path)
            logging.debug(f"Linked {source_path} to {destination_path}")

        logging.info("Configurations added successfully.")
    except Exception as e:
        logging.error(f"Failed to add configurations: {e}")


if __name__ == "__main__":
    install_packages()
    adding_configs()
