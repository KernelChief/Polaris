# SPDX-License-Identifier: GPL-3.0-or-later

Name:           polaris
%{!?app_version:%global app_version 1.0}
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

Source0:        polaris-%{version}.tar.gz

%description
Polaris is a Qt-based graphical utility for Fedora 43 KDE workstations.
It provides one-click install/remove actions for common workstation packages,
drivers, and Flatpak apps using a PolicyKit-protected helper.

%prep
%setup -q

%install
rm -rf %{buildroot}

install -D -m 0755 src/polaris %{buildroot}%{_bindir}/polaris
install -D -m 0755 src/polaris-helper %{buildroot}%{_libexecdir}/polaris-helper
install -D -m 0644 src/io.github.kernelchief.polaris.policy \
  %{buildroot}%{_datadir}/polkit-1/actions/io.github.kernelchief.polaris.policy
install -D -m 0644 src/polaris.desktop \
  %{buildroot}%{_datadir}/applications/polaris.desktop
install -D -m 0644 LICENSE \
  %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%{_bindir}/polaris
%{_libexecdir}/polaris-helper
%{_datadir}/polkit-1/actions/io.github.kernelchief.polaris.policy
%{_datadir}/applications/polaris.desktop
%{_datadir}/licenses/%{name}/LICENSE

%changelog
* Thu Apr 24 2026 KernelChief - 1.0-1
- Rename project to Polaris; migrate UI to PySide6 (Qt6)
