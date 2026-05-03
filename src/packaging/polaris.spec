# SPDX-License-Identifier: GPL-3.0-or-later

Name:           polaris
%{!?app_version:%global app_version 1.0.1}
Version:        %{app_version}
Release:        1%{?dist}
Summary:        One-click workstation setup assistant for Fedora KDE
License:        GPL-3.0-or-later
URL:            https://github.com/KernelChief/polaris
BuildArch:      noarch

Requires:       python3
Requires:       python3-pyside6
Requires:       polkit
Requires:       coreutils
Requires:       curl
Requires:       systemd
Requires:       dnf5

# Use the GitHub-generated tarball URL
Source0:        https://github.com/KernelChief/Polaris/archive/refs/tags/v%{version}.tar.gz

%description
Polaris is a Qt-based graphical utility for Fedora 43 KDE workstations.
It provides one-click install/remove actions for common workstation packages,
drivers, and Flatpak apps using a PolicyKit-protected helper.

%prep
# GitHub tarballs unpack into a directory named 'Project-version'
%setup -q -n Polaris-%{version}

%install
rm -rf %{buildroot}

install -D -m 0755 src/polaris %{buildroot}%{_bindir}/polaris
install -D -m 0755 src/polaris-helper %{buildroot}%{_libexecdir}/polaris-helper
install -D -m 0644 src/io.github.kernelchief.polaris.policy \
  %{buildroot}%{_datadir}/polkit-1/actions/io.github.kernelchief.polaris.policy
install -D -m 0644 src/polaris.desktop \
  %{buildroot}%{_datadir}/applications/polaris.desktop
install -D -m 0644 docs/PolarisLogo.png \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/polaris.png
install -D -m 0644 LICENSE \
  %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%{_bindir}/polaris
%{_libexecdir}/polaris-helper
%{_datadir}/polkit-1/actions/io.github.kernelchief.polaris.policy
%{_datadir}/applications/polaris.desktop
%{_datadir}/icons/hicolor/256x256/apps/polaris.png
%{_datadir}/licenses/%{name}/LICENSE

%changelog
* Sun Apr 26 2026 KernelChief - 1.0.1-1
- Update to v1.0.1: Migrate to PySide6 and expand app library
* Fri Apr 24 2026 KernelChief - 1.0.0-1
- Initial release and rename to Polaris
