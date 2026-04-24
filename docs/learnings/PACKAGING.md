# RPM Packaging & PolicyKit Learning

**Token Estimate**: ~500 tokens

---

## RPM Spec Best Practices
- Use macros: `%_bindir`, `%_datadir`, `%_sysconfdir`.
- **Dependencies**: 
  - `Requires`: For runtime.
  - `BuildRequires`: For build time.
- **Post/Postun**: Use `%post` for `systemctl daemon-reload` or updating icon caches.

## PolicyKit (polkit)
- Allows unprivileged apps to run specific commands as root without sudo password (if configured).
- Rules are stored in `/usr/share/polkit-1/actions/`.
- Policy file naming: `org.projectname.manager.policy`.

## File Permissions
- Desktop files: `/usr/share/applications/` (0644).
- Icons: `/usr/share/icons/hicolor/...` (0644).
- Helpers: `/usr/libexec/` or `/usr/bin/` (0755).

## Build Pipeline
- `rpmbuild -ba file.spec`
- Use mock for clean chroot builds.
- Sign RPMs for production use.
