import subprocess


def is_installed(package):
    """Check if a package is installed using pacman"""
    result = subprocess.run(
        ["pacman", "-Qq", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    return result.returncode == 0


def install_package(package):
    """Install a package using pacman"""
    subprocess.run(["sudo", "pacman", "-S", "--noconfirm", package])


def main():
    packages = [
        "ttf-sourcecodepro-nerd",
        "ttf-nerd-fonts-symbols",
        "ttf-nerd-fonts-symbols-mono",
        "ttf-mononoki-nerd",
        "nodejs",
        "npm",
        "starship",
        "tree",
        "neovim",
        "alacritty",
        "lazygit",
        "github-cli",
    ]

    for package in packages:
        if not is_installed(package):
            print(f"Installing {package}...")
            install_package(package)
        else:
            print(f"{package} is already installed. Skipping...")


if __name__ == "__main__":
    main()
