# Workstation Starter Kit — Roadmap

**Target**: Fedora 43 KDE | **UI**: PySide6 (Qt6) | **Packaging**: RPM + Flatpak

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ Done | Completed and committed |
| 🔄 In Progress | Done but not yet committed / needs follow-up |
| 🔲 Planned | Decided, not started |
| 💡 Idea | Under consideration |

---

## Phase 1 — Core Foundation

| Status | Task |
|--------|------|
| ✅ | PolicyKit-protected Bash helper (`workstation-starter-kit-helper`) |
| ✅ | Per-feature install / remove / check system in `FEATURES` list |
| ✅ | Flatpak scope picker (user vs system dialog) |
| ✅ | Bundle system (Recommended + Gaming Pack) |
| ✅ | SELinux mode switch (Permissive / Disabled) |
| ✅ | ZRAM profile setup (`zstd`, high swap priority) |
| ✅ | AppImage support (download + fix ownership via `PKEXEC_UID`) |
| ✅ | RPM packaging (`.spec` + `build-rpm.sh`) |
| ✅ | Desktop file + PolicyKit action policy |

---

## Phase 2 — GTK → Qt Migration  *(in progress)*

| Status | Task |
|--------|------|
| 🔄 | Rewrite UI from GTK3 (`gi`/`Gtk`) to **PySide6** (Qt6) |
| 🔄 | Replace `GLib` threading with `QObject` + `Signal` + daemon thread |
| 🔄 | Add indeterminate `QProgressBar` spinner per row |
| 🔄 | Add feature search/filter bar (`QLineEdit`) |
| 🔄 | Logs tab with `QPlainTextEdit` (monospace, auto-scroll) |
| 🔄 | Add NVIDIA Drivers feature (`install_nvidia_drivers` / `remove_nvidia_drivers`) |
| 🔄 | Update `.spec` summary: "GTK" → "Qt bootstrap assistant for Fedora" |
| 🔲 | **Fix `.spec` Requires**: remove `python3-gobject`, `gtk3`; add `python3-pyside6` |
| 🔲 | **Update `.spec` description**: still says "GTK utility for RPM-based distributions" |
| 🔲 | Commit Phase 2 changes |

---

## Phase 3 — Features & Polish

| Status | Task |
|--------|------|
| ✅ | **RPM Fusion** (Free + Non-Free) — now in Recommended + Gaming bundles |
| ✅ | **AMD GPU Tools** — `radeontop` + `mesa-va-drivers` (kernel driver built-in, no install needed) |
| ✅ | **KDE Connect** — link phone to KDE desktop |
| ✅ | **VS Code** — via Microsoft repo |
| ✅ | **Piper** — gaming mouse config via libratbag |
| ✅ | **Snapper** — Btrfs/LVM CLI snapshot manager |
| ✅ | **Prism Launcher** (Flatpak) — mod-friendly Minecraft launcher |
| ✅ | **GIMP, Kdenlive** (Flatpak) — image and video editing |
| ✅ | **Signal, Element, Telegram** (Flatpak) — secure/alternative messaging |
| ✅ | **Distrobox + BoxBuddy** — already present from Qt migration |
| 🔲 | Add **Flatpak remote (Flathub)** setup as a dedicated feature (currently implicit) |
| 🔲 | Add **JetBrains Toolbox** (AppImage) |
| ~~🔲~~ | ~~Timeshift~~ — **dropped**: Fedora 43 uses Btrfs by default; Snapper is the correct tool |
| 💡 | Post-install reboot prompt for features that require it (NVIDIA, kernel modules) |
| 💡 | "What's installed" summary / export page |
| 💡 | Theme picker for Qt (follow system / force dark mode) |

---

## Phase 4 — Packaging & Distribution

| Status | Task |
|--------|------|
| 🔲 | Publish to COPR (Fedora community package repo) |
| 🔲 | Automate RPM version bump via CI on tag push |
| 🔲 | Add `python3-pyside6` to RPM `BuildRequires` |
| 🔲 | Flatpak manifest (`io.github.KernelChief.WorkstationStarterKit`) |
| 💡 | OBS (openSUSE Build Service) for multi-distro builds |
| 💡 | Coinstall `.desktop` with MIME type for auto-detection |

---

## Phase 5 — Multi-Distro Support  *(future)*

| Status | Task |
|--------|------|
| 💡 | **AlmaLinux 9/10** support (`dnf`, CRB, EPEL, `el9`/`el10` RPM suffixes) |
| 💡 | **openSUSE Tumbleweed** support (`zypper`) |
| 💡 | Distro auto-detection at runtime |
| 💡 | Distro-specific feature flags (hide Flatpak scope picker on Silverblue, etc.) |

---

## Known Issues / Tech Debt

| Priority | Issue |
|----------|-------|
| 🔴 High | `.spec` still lists GTK/GObject as `Requires` after Qt migration |
| 🟡 Med | `group_packages()` in helper is stale — gaming group list doesn't match `FEATURES` |
| 🟡 Med | `install_pkg_url` alias exists in helper dispatch but UI always calls `install_url_rpm` |
| 🟢 Low | `QUICK_REFERENCE.md` has placeholder text, last updated date not filled |
| 🟢 Low | Architecture map in `.claude/ARCHITECTURE_MAP.md` lists `scripts/`, `configs/`, `manifests/` dirs that don't exist |

---

**Last Updated**: 2026-04-23
