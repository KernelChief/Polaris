# 🚀 Polaris
## By friends, for friends. Now for everyone.

[![Last Commit](https://img.shields.io/github/last-commit/KernelChief/polaris)](https://github.com/KernelChief/polaris/commits)
[![Repo Size](https://img.shields.io/github/repo-size/KernelChief/polaris)](https://github.com/KernelChief/polaris)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Shell](https://img.shields.io/badge/Script-Shell-4EAA25?logo=gnu-bash&logoColor=white)](https://www.gnu.org/software/bash/)
[![Fedora](https://img.shields.io/badge/Platform-Fedora%2043%20%2F%2044-51A2DA?logo=fedora&logoColor=white)](https://fedoraproject.org/)
[![Buy Me A Coffee](https://img.shields.io/badge/Support-Buy%20Me%20A%20Coffee-orange?logo=buy-me-a-coffee)](https://www.buymeacoffee.com/ttheroux)
[![Stars](https://img.shields.io/github/stars/KernelChief/polaris?style=social)](https://github.com/KernelChief/polaris/stargazers)

Setting up a Linux workstation shouldn’t be a chore.

**Polaris** is a **PySide6 (Qt6)** desktop application that simplifies setting up a fresh Fedora installation. It wraps essential post-install tasks, such as enabling repositories, installing drivers, and deploying apps, into a clean, point-and-click interface.

**Why Polaris?** Polaris is the north star: always there, always reliable. It’s the first thing you find when you’re navigating a new install.

## 🚀 Quick Start (Recommended)

The easiest way to install and keep Polaris updated is via our official COPR repository.

### 1. Enable the Repository
Open your terminal and run:
```bash
sudo dnf copr enable tristantheroux/Polaris
```

### 2. Install Polaris
```bash
sudo dnf install polaris
```

### 3. Launch the App
Find **Polaris** in your Application Menu or run `polaris` from the terminal.

---

### Alternative: Manual RPM Installation
If you prefer not to use COPR, you can download the latest `.rpm` from the [releases page](https://github.com/KernelChief/polaris/releases).
```bash
sudo dnf install ./polaris-*.noarch.rpm
```

## 🧩 Supported Platform

Polaris is built and tested on **Fedora 43 and 44** with KDE Plasma and GNOME (GDM). It leverages `dnf5` and Btrfs-specific tools to provide a seamless post-install experience.

## 🧰 Included Features

The app auto-detects what is already on your system and organizes tools into dedicated tabs.

### Get Started (Recommended Bundle)
* **RPM Fusion**: Free + Non-Free repos for codecs and proprietary drivers.
* **Flathub Remote**: Setup for both System and User scopes.
* **Essentials**: Git, curl, zsh, build tools, and system utilities.
* **Monitoring**: htop, btop, nvtop, sensors.
* **ZRAM Expansion**: Configures `zram-generator` with `zstd` compression.

### Drivers
* **NVIDIA Drivers**: Official open kernel modules via NVIDIA CUDA repo.
* **AMD GPU Tools**: Monitoring (`radeontop`) and VA-API hardware acceleration.

### Security
* **Password Managers**: 1Password (official repo), Proton Pass (RPM).
* **VPN**: Tailscale mesh networking.

### Gaming
* **Launchers**: Steam, Lutris, Heroic (AppImage), CurseForge (AppImage), Prism Launcher (Flatpak).
* **Tools**: Wine, GameMode, Gamescope, MangoHud, GOverlay, ProtonUp-Qt.
* **Input**: Input Remapper for gamepads/mice.

### Containers
* **Engine**: Podman & Distrobox.
* **GUI**: BoxBuddy (Flatpak), Podman Desktop (Flatpak).

### System Tools
* **Hardware**: LACT (AMD Control), CoolerControl, OpenRGB, Piper (Mice).
* **Filesystem**: Btrfs Assistant & Snapper for snapshot management.
* **Utilities**: Flatseal, Warehouse.

### Media & Apps
* **Productivity**: VS Code, PyCharm Community Edition, LibreOffice, OpenOffice.
* **Communication**: Discord (RPM), Vesktop, Slack, Signal, Telegram, Element, Mattermost.
* **Media**: OBS Studio, VLC, EasyEffects, Pulsemeeter, Flameshot.
* **Graphics**: GIMP, Kdenlive.

## 🔐 Privilege & Security Model

* **Unprivileged UI**: The Polaris GUI runs as your normal user.
* **Authorized Helper**: Privileged actions (like `dnf` installs or editing `/etc`) are routed through a background helper (`/usr/libexec/polaris-helper`) via **Polkit**.
* **User Scope**: Flatpak "User" installs are run correctly as the real user via `PKEXEC_UID`, keeping your home directory permissions clean.

## ❓ FAQ

**Why does it ask for my password?**  
Changing system configurations and installing software via DNF require root privileges. Polaris uses Polkit to ask for permission only when an action is triggered.

**Is it safe to use?**  
Polaris is transparent. Every action it performs is a shell command you can inspect in the **Logs** tab within the app.

**Why are some apps Flatpaks and others RPMs?**  
We choose the format that offers the best experience on Fedora. For example, Discord is an RPM from RPM Fusion for better system integration, while productivity apps like LibreOffice are offered as Flatpaks for isolation and easy updates.

## 🤝 Community

* [Code of Conduct](CODE_OF_CONDUCT.md)
* [Contributing Guide](CONTRIBUTING.md)

## 📜 License

This project is licensed under the **GNU GPL v3.0**. See [LICENSE](LICENSE).
