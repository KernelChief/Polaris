# Qt 5 & Qt 6 Learning & Best Practices

**Token Estimate**: ~500 tokens

---

## Qt 5 vs Qt 6
- **Qt 5**: Legacy but still widely used in RHEL 8/9.
- **Qt 6**: Modern standard for Fedora and upcoming RHEL 10.

## Environment Variables for Styling
To make Qt apps look native on GTK/GNOME:
- `QT_QPA_PLATFORMTHEME=gtk3` (Qt 5)
- `QT_STYLE_OVERRIDE=adwaita-dark`
- `QT_AUTO_SCREEN_SCALE_FACTOR=1` (High DPI)

## Common Packages (Fedora/RHEL)
- **Qt 5**: `qt5-qtbase`, `qt5-qtwayland`, `qt5-qtsvg`
- **Qt 6**: `qt6-qtbase`, `qt6-qtwayland`, `qt6-qtsvg`

## Almalinux/RHEL specifics
- RHEL 9 provides Qt 5.15 and Qt 6.2+.
- EPEL is often required for extra Qt modules.

## Theming Tools
- `qt5ct` and `qt6ct`: Configuration tools for Qt apps when not running in KDE.
- `adwaita-qt5`, `adwaita-qt6`: Themes to match GNOME's Adwaita.
