# 🚀 Polaris
## By friends, for friends—now for everyone.

[![Last Commit](https://img.shields.io/github/last-commit/KernelChief/polaris)](https://github.com/KernelChief/polaris/commits)
[![Repo Size](https://img.shields.io/github/repo-size/KernelChief/polaris)](https://github.com/KernelChief/polaris)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Made%20with-Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Shell](https://img.shields.io/badge/Script-Shell-4EAA25?logo=gnu-bash&logoColor=white)](https://www.gnu.org/software/bash/)
[![Fedora](https://img.shields.io/badge/Platform-Fedora%2043%20KDE-51A2DA?logo=fedora&logoColor=white)](https://fedoraproject.org/)
[![Buy Me A Coffee](https://img.shields.io/badge/Support-Buy%20Me%20A%20Coffee-orange?logo=buy-me-a-coffee)](https://www.buymeacoffee.com/ttheroux)
[![Stars](https://img.shields.io/github/stars/KernelChief/polaris?style=social)](https://github.com/KernelChief/polaris/stargazers)

Setting up a Linux workstation shouldn’t be a chore.

This project started as a set of **Ansible playbooks** to help friends deploy a clean Fedora KDE environment — the same way, every time. As more people started asking to use it, it became clear that a command-line playbook wasn’t the right experience for everyone. So it grew into a **Qt (PySide6) desktop application** that wraps all those same actions behind a simple point-and-click interface — no terminal required.

**Why Polaris?** Polaris is the north star — always there, always reliable. It’s the first thing you find when you’re navigating somewhere new, which is exactly what this tool is for a fresh Fedora install.

**Key Features:**

- **One-click setup:** From gaming essentials to developer environments, RPM Fusion, NVIDIA/AMD drivers, and more.
- **Fedora 43 KDE-native:** Optimized for Fedora 43 KDE with `dnf5`, Btrfs, Flatpak, and KDE-first tools.
- **Safe execution:** The UI runs as your normal user. Privileged actions go through a Polkit-authorized helper — you stay in control.

---

## 📚 Quick Navigation

- [🚀 Quick Start](#-quick-start-recommended)
- [📦 Installation Methods](#-installation-methods)
- [🧩 Supported Platform](#-supported-platform)
- [🧰 Included Features](#-included-features)
- [🔐 Privilege & Security Model](#-privilege--security-model)
- [❓ FAQ](#-faq)
- [📜 License](#-license)

---

## 🚀 Quick Start (Recommended)

### 1️⃣ Download the RPM

Go to the project releases page:

https://github.com/KernelChief/polaris/releases

Download the RPM named like:

- `polaris-X.X.X-X.fc43.noarch.rpm`

Where:

- `X.X.X` = app version
- `-X` = RPM release number

---

### 2️⃣ Install the RPM

From the directory where the file was downloaded:

```bash
sudo dnf install ./polaris-X.X.X-X.fc43.noarch.rpm
```

This installs:

- the GUI launcher (`polaris`)
- the helper (`/usr/libexec/polaris-helper`)
- the polkit policy
- the desktop entry

---

### 3️⃣ Launch the App

Launch from app menu:

- **Polaris**

Or via terminal:

```bash
polaris
```

---

## 📦 Installation Methods

Depending on feature, Polaris uses:

- DNF package installs/removals
- Official URL RPM installs (e.g. Chrome, Zoom)
- Flatpak installs (user or system scope)
- COPR enable + package install for selected tools
- Service enable/disable via `systemctl`
- System config actions (e.g. ZRAM profile, SELinux mode)

---

## 🧩 Supported Platform

- **Target:** Fedora 43 KDE Workstation

---

## 🧰 Included Features

Includes install/remove workflows for:

- **Repos:** RPM Fusion (Free + Non-Free), 1Password, Tailscale, Microsoft (VS Code), NVIDIA CUDA
- **System:** Essential tools, ZRAM profile, SELinux mode switch, Snapper (Btrfs snapshots)
- **Drivers:** NVIDIA open kernel modules, AMD GPU tools (`radeontop`, VA-API)
- **Security:** 1Password, Proton Pass, Tailscale
- **Gaming:** Steam, Lutris, Wine, GameMode, Gamescope, MangoHud, GOverlay, Faugus Launcher, Heroic, CurseForge, ProtonUp-Qt, Bottles, Prism Launcher
- **Hardware tools:** LACT, CoolerControl, OpenRGB, Piper, Input Remapper, Btrfs Assistant
- **Containers:** Podman, Distrobox, BoxBuddy, Podman Desktop
- **Media & Apps:** OBS Studio, VLC, EasyEffects, Flameshot, Chrome, Zoom, VS Code
- **Flatpak:** Spotify, Discord, Vesktop, Slack, LibreOffice, GIMP, Kdenlive, Signal, Element, Telegram, and more

The in-app feature list is the source of truth — the app auto-detects what's already installed.

---

## 🔐 Privilege & Security Model

- GUI process runs as normal user
- Privileged actions are routed through:
  - `pkexec /usr/libexec/polaris-helper ...`
- Polkit action:
  - `io.github.kernelchief.polaris`
- Authentication is requested only when needed

---

## ❓ FAQ

**Why does it ask for admin credentials?**  
Installing/removing packages, editing system config, and enabling services require elevated privileges.

**Does the app itself run as root?**  
No. The UI is unprivileged; only helper actions are elevated through polkit.

**Can I apply items one-by-one instead of bundles?**  
Yes. Every listed feature/app can be installed or removed individually.

**What if I only want Flatpak apps?**  
You can install only Flatpak rows; each prompts for user/system scope.

---

## 🤝 Community

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contributing](CONTRIBUTING.md)
- Maintainer/developer workflow: see [CONTRIBUTING.md](CONTRIBUTING.md)

---
## 📜 License

This project is licensed under the **GNU GPL v3.0**. See [LICENSE](LICENSE).
