# Polaris — Roadmap

**Target**: Fedora 43 KDE — **this is a Fedora-only project, no multi-distro scope**
**UI**: PySide6 (Qt6) | **Packaging**: RPM

---

## Legend

| Symbol | Meaning |
|--------|---------|
| ✅ Done | Completed and committed |
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
| ✅ | Add braille spinner (`⣾⣽⣻⢿⡿⣟⣯⣷`) per row via `QTimer` |
| ✅ | Fixed-width status badge (no layout shift on state change) |
| ✅ | Add feature search/filter bar (`QLineEdit`) |
| ✅ | All tab — lists every feature, auto-selected when searching |
| ✅ | Cross-category search (searches all tabs, not just current) |
| ✅ | Logs tab with `QPlainTextEdit` (monospace, auto-scroll) |
| ✅ | Add NVIDIA Drivers feature |
| ✅ | Fix `.spec` Requires: removed `python3-gobject`, `gtk3`; added `python3-pyside6` |

---

## Phase 3 — Features & Polish ✅

| Status | Task |
|--------|------|
| ✅ | **RPM Fusion** (Free + Non-Free) — Recommended + Gaming bundles |
| ✅ | **Flathub remote** — system + user remotes, dedicated feature in Recommended bundle |
| ✅ | **Flatpak user-mode fix** — uses `PKEXEC_UID` + `runuser` so user-scope installs go to the right home directory |
| ✅ | **Bundle abort on failure** — bundle halts and re-enables buttons instead of silently continuing |
| ✅ | **`dnf_deps` key** — pre-install RPM deps before Flatpak (e.g. `libglvnd-gles` for BoxBuddy) |
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
| ✅ | **Discord** — switched from Flatpak to RPM (RPM Fusion Non-Free) |
| ~~🔲~~ | ~~Timeshift~~ — **dropped**: Fedora 43 uses Btrfs; Snapper is the correct tool |
| ~~🔲~~ | ~~Bottles~~ — **dropped**: unmaintained upstream |
| ~~🔲~~ | ~~Boxflat~~ — **dropped**: removed from scope |
| 💡 | Post-install reboot prompt for features that require it (NVIDIA, kernel modules) |
| 💡 | "What's installed" summary / export page |
| 💡 | Theme picker for Qt (follow system / force dark mode) |

---

## Phase 4 — Packaging & Distribution

| Status | Task |
|--------|------|
| ✅ | `python3-pyside6` in RPM `Requires` |
| ✅ | CI: ruff lint on `src/polaris` |
| ✅ | CI: ShellCheck on `src/polaris-helper` |
| ✅ | CI: RPM install smoke test (verify files land at expected paths) |
| ✅ | CI: PR comment with artifact link (fresh comment per commit) |
| ✅ | CI: GitHub Release draft on tag push with install instructions |
| 🔲 | Publish to COPR — eliminates GPG warning, enables `dnf upgrade` |
| 🔲 | Automate RPM version bump via CI on tag push |
| 💡 | Flatpak manifest (`io.github.KernelChief.Polaris`) |

---

## Known Issues / Tech Debt

| Priority | Issue |
|----------|-------|
| 🟡 Med | `install_pkg_url` alias removed — verify no external scripts used it |
| 🟢 Low | `QUICK_REFERENCE.md` has placeholder text, last updated date not filled |
| 🟢 Low | Architecture map in `.claude/ARCHITECTURE_MAP.md` lists `scripts/`, `configs/`, `manifests/` dirs that don't exist |

---

**Last Updated**: 2026-04-26
