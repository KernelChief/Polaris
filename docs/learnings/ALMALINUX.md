# AlmaLinux 9 & 10 Learning

**Token Estimate**: ~600 tokens

---

## AlmaLinux 9 (Current Stable)
- Based on RHEL 9.
- Kernel 5.14+.
- Uses `dnf`.
- **CRB (Code Ready Builder)**: Essential repo for development headers.
  - `dnf config-manager --set-enabled crb`

## AlmaLinux 10 (Future/Upcoming)
- Based on RHEL 10 / CentOS Stream 10.
- Likely to drop support for older CPU architectures (x86-64-v2 vs v3).
- Move towards Wayland by default for GNOME, potentially dropping X11 in the default install.

## Key Differences from Fedora
- **Release Cycle**: Much slower, stability-focused.
- **Packages**: Older versions than Fedora.
- **EPEL**: mandatory for almost any workstation setup.
- **SELinux**: Strict by default.

## Best Practices
- Use `el9` or `el10` suffixes for RPMs.
- Always check if a package is in `appstream`, `baseos`, or `crb` before looking at EPEL.
- Modular DNF is used but being phased out in newer versions.
