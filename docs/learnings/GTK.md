# GTK Learning & Best Practices

**Token Estimate**: ~400 tokens

---

## Configuration
- **GTK3/4 Themes**: Usually stored in `~/.config/gtk-3.0/settings.ini` or `~/.config/gtk-4.0/settings.ini`.
- **Environment Variables**:
  - `GTK_THEME`: Override theme.
  - `GDK_BACKEND`: `wayland` or `x11`.

## Common Dependencies (Fedora/RHEL)
- `gtk3`, `gtk4`
- `adwaita-gtk2-theme`, `adwaita-cursor-theme`
- `gnome-themes-extra`

## Pitfalls
- GTK4 no longer supports some GTK3 CSS properties.
- `libadwaita` enforces specific styling in newer GNOME versions.
- When running as root (pkexec), themes might not carry over from the user session.

## Integration
- Use `gsettings` to change themes globally for the user:
  ```bash
  gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'
  ```
