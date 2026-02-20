# Contributing to Workstation Starter Kit

Thanks for your interest in contributing! This project is friendly to new
contributors and first-time PRs. The goal is to keep the installer simple,
reliable, and easy to audit.

Please make sure to follow our [Code of Conduct](CODE_OF_CONDUCT.md) in all
project interactions.

## How to contribute (issues first)

1. **Open an issue** describing the bug, feature, or improvement.
2. We’ll discuss scope and approach.
3. Submit a pull request once the plan is clear.

This helps avoid duplicated effort and keeps changes aligned with the project
direction.

## Development setup

There are no strict coding style requirements. Keep changes readable and
focused.

## Maintainer workflow: adding/editing apps

Workstation Starter Kit is intentionally data-driven.

Most app changes should be done in:

- `src/workstation-starter-kit` (the `FEATURES` list)
- `src/workstation-starter-kit-helper` (helper actions)

### 1) Add a new app/feature entry in `FEATURES`

Each item is a dict with keys like:

- `id` (unique)
- `name`
- `desc`
- `check` (installed-state rule)
- `install` (list of helper action steps)
- optional `remove`
- optional `contains` (shown in in-app Details popup)

Example:

```python
{
  "id": "mytool",
  "name": "🧰 My Tool",
  "desc": "Short description",
  "check": {"kind": "rpm", "pkg": "mytool"},
  "install": [["install_pkg", "mytool"]],
  "remove": [["remove_pkg", "mytool"]],
}
```

### 2) Pick the proper `check` kind

Current kinds:

- `rpm`
- `rpm_all`
- `flatpak`
- `zram`
- `repo_and_pkg`
- `tailscale`
- `pkg_and_service`
- `appimage_glob`
- `appimage_glob_any`

If you need a new pattern, add it in `_feature_applied()`.

### 3) Wire helper actions

Every action in `install` / `remove` must exist in
`src/workstation-starter-kit-helper` dispatcher.

If missing, add:

1. helper function
2. `case` dispatcher entry

### 4) Validate before PR

```bash
python3 -m py_compile src/workstation-starter-kit
bash -n src/workstation-starter-kit-helper
```

## Testing & building

Basic checks:
- Launch the UI and verify the flow you changed.
- Make sure logs show clean output.

Build the RPM locally (Fedora 43 example):

```bash
sudo dnf install -y rpm-build rpmdevtools rsync tar python3-gobject gtk3 polkit
rpmdev-setuptree
./src/packaging/build-rpm.sh 1.0.0
```

Build artifacts are written to:

- `~/rpmbuild/RPMS/noarch/workstation-starter-kit-<version>-1.fc43.noarch.rpm`
- `~/rpmbuild/SRPMS/workstation-starter-kit-<version>-1.fc43.src.rpm`

## Submitting a PR

- Keep PRs small and focused when possible.
- Explain what you changed and why.
- Include screenshots for UI changes.

## Questions

If you’re unsure about anything, open an issue and ask — it’s welcome.