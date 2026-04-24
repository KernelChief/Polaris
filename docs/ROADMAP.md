# Polaris — Roadmap

**Target**: Fedora 43 KDE — **this is a Fedora-only project, no multi-distro scope**
**UI**: PySide6 (Qt6) | **Packaging**: RPM

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ Done | Completed and committed |
| 🔄 In Progress | Done but not yet committed / needs follow-up |
| 🔲 Planned | Decided, not started |
| 💡 Idea | Under consideration |

---

## Phase 1 — Core Foundation ✅

| Status | Task |
|--------|------|
| ✅ | PolicyKit-protected Bash helper (`polaris-helper`) |
| ✅ | Per-feature install / remove / check system in `FEATURES` list |
| ✅ | Flatpak scope picker (user vs system dialog) |
| ✅ | Bundle system (Recommended + Gaming Pack) |
| ✅ | SELinux mode switch (Permissive / Disabled) |
| ✅ | ZRAM profile setup (`zstd`, high swap priority) |
| ✅ | AppImage support (download + fix ownership via `PKEXEC_UID`) |
| ✅ | RPM packaging (`.spec` + `build-rpm.sh`) |
| ✅ | Desktop file + PolicyKit action policy |

---

## Phase 2 — GTK → Qt Migration ✅

| Status | Task |
|--------|------|
| ✅ | Rewrite UI from GTK3 (`gi`/`Gtk`) to **PySide6** (Qt6) |
| ✅ | Replace `GLib` threading with `QObject` + `Signal` + daemon thread |
| ✅ | Add indeterminate `QProgressBar` spinner per row |
| ✅ | Add feature search/filter bar (`QLineEdit`) |
| ✅ | Logs tab with `QPlainTextEdit` (monospace, auto-scroll) |
| ✅ | Add NVIDIA Drivers feature |
| ✅ | Fix `.spec` Requires: removed `python3-gobject`, `gtk3`; added `python3-pyside6` |
| ✅ | Update `.spec` summary and description |
| 🔄 | Commit Phase 2 + Phase 3 changes |

---

## Phase 3 — Features & Polish ✅

| Status | Task |
|--------|------|
| ✅ | **RPM Fusion** (Free + Non-Free) — Recommended + Gaming bundles |
| ✅ | **Flathub remote** — dedicated feature, in Recommended bundle |
| ✅ | **AMD GPU Tools** — `radeontop` + `mesa-va-drivers` |
| ✅ | **KDE Connect** — link phone to KDE desktop |
| ✅ | **VS Code** — via Microsoft repo |
| ✅ | **Piper** — gaming mouse config via libratbag |
| ✅ | **Snapper** — Btrfs/LVM CLI snapshot manager |
| ✅ | **Prism Launcher** (Flatpak) — mod-friendly Minecraft launcher |
| ✅ | **GIMP, Kdenlive** (Flatpak) — image and video editing |
| ✅ | **Signal, Element, Telegram** (Flatpak) — secure/alternative messaging |
| ✅ | **Distrobox + BoxBuddy** |
| ✅ | **JetBrains Toolbox** — manage all JetBrains IDEs from one launcher |
| ~~🔲~~ | ~~Timeshift~~ — **dropped**: Fedora 43 uses Btrfs; Snapper is the correct tool |
| 💡 | Post-install reboot prompt for features that require it (NVIDIA, kernel modules) |
| 💡 | "What's installed" summary / export page |
| 💡 | Theme picker for Qt (follow system / force dark mode) |

---

## Phase 4 — Packaging & Distribution

| Status | Task |
|--------|------|
| ✅ | `python3-pyside6` in RPM `Requires` |
| 🔲 | Publish to COPR (Fedora community package repo) |
| 🔲 | Automate RPM version bump via CI on tag push |
| 🔲 | Flatpak manifest (`io.github.KernelChief.Polaris`) |
| 💡 | Coinstall `.desktop` with MIME type for auto-detection |

---

## Known Issues / Tech Debt

| Priority | Issue |
|----------|-------|
| 🟡 Med | `install_pkg_url` alias removed — verify no external scripts used it |
| 🟢 Low | `QUICK_REFERENCE.md` has placeholder text, last updated date not filled |
| 🟢 Low | Architecture map in `.claude/ARCHITECTURE_MAP.md` lists `scripts/`, `configs/`, `manifests/` dirs that don't exist |

---

**Last Updated**: 2026-04-24
