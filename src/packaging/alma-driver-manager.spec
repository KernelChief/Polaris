# SPDX-License-Identifier: MIT

Name:           alma-driver-manager
Version:        0.1
Release:        1%{?dist}
Summary:        Simple Driver Manager UI for AlmaLinux (NVIDIA + local RPM)
License:        MIT
URL:            https://github.com/KernelChief/alma-driver-manager
BuildArch:      noarch

Requires:       python3
Requires:       python3-gobject
Requires:       gtk3
Requires:       polkit

Source0:        alma-driver-manager-%{version}.tar.gz

%description
A small GUI to install NVIDIA drivers via the official AlmaLinux method
or from a local RPM, using pkexec + polkit.

%prep
%setup -q

%install
rm -rf %{buildroot}

# App
install -D -m 0755 src/alma-driver-manager %{buildroot}%{_bindir}/alma-driver-manager

# Root helper
install -D -m 0755 src/alma-driver-helper %{buildroot}%{_libexecdir}/alma-driver-helper

# Polkit policy
install -D -m 0644 src/org.almalinux.drivermanager.policy \
  %{buildroot}%{_datadir}/polkit-1/actions/org.almalinux.drivermanager.policy

# Desktop entry
install -D -m 0644 src/alma-driver-manager.desktop \
  %{buildroot}%{_datadir}/applications/alma-driver-manager.desktop

# License file (best practice for RPMs)
install -D -m 0644 LICENSE \
  %{buildroot}%{_datadir}/licenses/%{name}/LICENSE

%files
%{_bindir}/alma-driver-manager
%{_libexecdir}/alma-driver-helper
%{_datadir}/polkit-1/actions/org.almalinux.drivermanager.policy
%{_datadir}/applications/alma-driver-manager.desktop
%{_datadir}/licenses/%{name}/LICENSE

%changelog
* Wed Jan 28 2026 KernelChief - 0.1-1
- Initial MVP
