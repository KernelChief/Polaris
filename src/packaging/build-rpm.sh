#!/usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SPEC="${ROOT_DIR}/src/packaging/polaris.spec"

command -v rpmdev-setuptree >/dev/null 2>&1 || {
  echo "ERROR: rpmdevtools not installed. Install: sudo dnf install rpmdevtools" >&2
  exit 1
}

if [[ ! -f "${SPEC}" ]]; then
  echo "ERROR: Spec not found: ${SPEC}" >&2
  exit 2
fi

NAME="polaris"

VERSION="${VERSION:-}"
if [[ -z "${VERSION}" && "${GITHUB_REF_TYPE:-}" == "tag" && -n "${GITHUB_REF_NAME:-}" ]]; then
  VERSION="${GITHUB_REF_NAME#v}"
fi
if [[ -z "${VERSION}" && -n "${GITHUB_REF:-}" && "${GITHUB_REF}" == refs/tags/* ]]; then
  VERSION="${GITHUB_REF#refs/tags/}"
  VERSION="${VERSION#v}"
fi
VERSION="${VERSION#v}"

RPM_VERSION="${VERSION}"
RPM_PRERELEASE=""

# Convert semver prerelease tags like 1.0.5-rc1 into RPM-friendly fields:
#   Version: 1.0.5
#   Release: 0.rc1.1%{?dist}
if [[ "${VERSION}" == *-* ]]; then
  RPM_VERSION="${VERSION%%-*}"
  RPM_PRERELEASE="${VERSION#*-}"
  RPM_PRERELEASE="${RPM_PRERELEASE//-/.}"
fi

if [[ -z "${NAME}" || -z "${VERSION}" || -z "${RPM_VERSION}" ]]; then
  echo "ERROR: Could not determine Name/Version. Set VERSION or run on a tag (e.g., v1.0.4)." >&2
  exit 3
fi

rpmdev-setuptree >/dev/null 2>&1 || true

TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

# Directory name must match %setup -n Polaris-%{version} in the spec
SRC_DIR="${TMPDIR}/Polaris-${RPM_VERSION}"
mkdir -p "${SRC_DIR}"

rsync -a \
  --exclude ".git" \
  --exclude ".github" \
  --exclude ".idea" \
  --exclude "*/__pycache__" \
  --exclude "*.pyc" \
  --exclude "*.pyo" \
  --exclude "*.rpm" \
  --exclude "rpmbuild" \
  "${ROOT_DIR}/" "${SRC_DIR}/"

TARBALL="${HOME}/rpmbuild/SOURCES/Polaris-${RPM_VERSION}.tar.gz"
tar -C "${TMPDIR}" -czf "${TARBALL}" "Polaris-${RPM_VERSION}"

echo "Created source tarball: ${TARBALL}"
echo "Building ${NAME} version ${VERSION} using spec: ${SPEC}"

RPM_RELEASE="1"
if [[ -n "${RPM_PRERELEASE}" ]]; then
  RPM_RELEASE="0.${RPM_PRERELEASE}.1"
fi

# Bake version/release into a temp copy of the spec so the SRPM is
# self-contained: COPR rebuilds from the SRPM without --define flags.
BUILD_SPEC="${TMPDIR}/polaris.spec"
sed \
  -e "s|%{!?app_version:%global app_version [^}]*}|%global app_version ${RPM_VERSION}|" \
  -e "s|%{!?app_release:%global app_release [^}]*}|%global app_release ${RPM_RELEASE}|" \
  "${SPEC}" > "${BUILD_SPEC}"

rpmbuild -ba "${BUILD_SPEC}"

echo "Done."
echo "RPMs are in: ${HOME}/rpmbuild/RPMS/"
