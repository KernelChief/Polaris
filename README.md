Alma Driver Manager (MVP)

A small, opinionated GUI for AlmaLinux that helps users install NVIDIA drivers
using the official AlmaLinux method, or install a locally-downloaded RPM via DNF
with proper dependency resolution.

This project is intentionally an MVP. The goal is to provide a reliable,
supportable driver-management experience without re-implementing a full
distribution update stack.

-----------------------------------------------------------------------

Goals

- Provide a simple, Nobara-like driver experience for AlmaLinux
- Follow supported AlmaLinux packaging and installation paths
- Keep all privileged operations behind PolicyKit (polkit)
- Remain easy to package as an RPM and distribute via a repository
- Be suitable for eventual upstream adoption if desired

-----------------------------------------------------------------------

Features

NVIDIA

- Install drivers using the official AlmaLinux-supported method:
  - Installs the AlmaLinux NVIDIA repository configuration package
  - Installs nvidia-open-kmod and nvidia-driver
- Optional installation of NVIDIA tooling:
  - nvidia-driver-cuda (provides nvidia-smi)
  - Full CUDA stack (cuda)
- Load the kernel module manually (modprobe nvidia_drm)
- Display driver status using nvidia-smi
- Advanced option:
  - Install a user-provided local RPM via DNF

-----------------------------------------------------------------------

Supported Platforms

- AlmaLinux 9.x
- AlmaLinux 10.x (including Kitten)
- Desktop environments:
  - GNOME
  - KDE

This tool does not bundle, redistribute, or modify NVIDIA drivers. It only
invokes the system package manager or installs user-supplied RPM files.

-----------------------------------------------------------------------

Official Installation Flow (NVIDIA)

The official installation path exposed by this UI performs the following
operations:

- dnf install almalinux-release-nvidia-driver
- dnf install nvidia-open-kmod nvidia-driver
- Optional:
  - dnf install nvidia-driver-cuda
  - dnf install cuda

All command output is surfaced directly in the UI for transparency.

-----------------------------------------------------------------------

Security and Quality

This repository follows basic security and code-quality practices:

- SonarQube is used to analyze the codebase for maintainability, bugs, and
  potential security issues.
- Dependabot is enabled to monitor dependencies and surface known security
  vulnerabilities.

These tools are advisory and do not imply certification or formal auditing.

-----------------------------------------------------------------------

Privilege Model

- The graphical application runs unprivileged.
- All system-modifying actions (package installation, removal, modprobe)
  are executed via a dedicated helper using PolicyKit (polkit).

This avoids running the entire application as root and keeps the attack surface
minimal.

-----------------------------------------------------------------------

Installation

Installing from a local RPM:

  sudo dnf install ./alma-driver-manager-<version>-<release>.noarch.rpm

The application can then be launched from the desktop menu or by running:

  alma-driver-manager

A repository-based installation method is planned for later stages.

-----------------------------------------------------------------------

Building the RPM (Development)

On an AlmaLinux build system:

  sudo dnf groupinstall "Development Tools"
  sudo dnf install rpm-build rpmdevtools python3-gobject gtk3 polkit rsync tar
  rpmdev-setuptree

Build the RPM using the provided build script:

  ./packaging/build-rpm.sh <version>

Built RPMs will be placed under:

  ~/rpmbuild/RPMS/noarch/

-----------------------------------------------------------------------

Roadmap

- Hardware detection improvements (GPU presence, installed driver version)
- Safer and more precise driver removal logic
- Optional Broadcom Wi-Fi handling via local RPM installs
- Replacement of pkexec helper with a D-Bus service for improved feedback
- AppStream metadata and icon polish

-----------------------------------------------------------------------

Contributing

This repository is currently private and experimental.

Internal testing feedback should include:
- AlmaLinux version
- GPU model
- Desktop environment
- Full application logs

-----------------------------------------------------------------------

License

MIT License. See the LICENSE file for details.
