# NVIDIA Drivers on Fedora Learning (Workstation Focus)

**Token Estimate**: ~800 tokens

---

## Official NVIDIA Method (Workstation Standard)
Ref: [NVIDIA Docs - Fedora Installation](https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/fedora.html)

### 1. Preparation
Install kernel headers and development packages for the running kernel:
```bash
dnf install kernel-devel-matched kernel-headers
```

### 2. Network Repository Setup (x86_64)
```bash
dnf config-manager addrepo --from-repofile=https://developer.download.nvidia.com/compute/cuda/repos/fedora$(rpm -E '%fedora')/x86_64/cuda-fedora$(rpm -E '%fedora').repo
dnf clean expire-cache
```

### 3. Installation: The "Open" Standard (Recommended)
NVIDIA has shifted to **Open Kernel Modules** as the modern standard for supported hardware (Turing+).

**Full Workstation Install (Compute + Desktop):**
```bash
dnf install nvidia-open
```

**Desktop-only (No Compute):**
```bash
dnf install nvidia-driver kmod-nvidia-open-dkms
```

**Switching from Proprietary to Open:**
```bash
dnf install nvidia-open --allowerasing
```

---

## Alternative Installation Options

### Proprietary Kernel Modules (Legacy/Older HW)
If Open modules are not supported or desired:
```bash
dnf install cuda-drivers
```

### Compute-only (Headless)
For servers or specialized workstations:
```bash
# Open
dnf install nvidia-driver-cuda kmod-nvidia-open-dkms
# Proprietary
dnf install nvidia-driver-cuda kmod-nvidia-latest-dkms
```

---

## Key Workstation Concepts
- **kernel-devel-matched**: Use this specific package to ensure headers perfectly match the installed kernel.
- **DKMS**: Used by these packages to ensure the driver is rebuilt during kernel updates.
- **Branch Stickiness**: Be aware of DNF version locking if a specific driver branch is required.
- **Reboot**: Always required after installation to initialize the new kernel modules.

## Verification
- `nvidia-smi`: Check driver version and GPU status.
- `glxinfo | grep NVIDIA`: Verify OpenGL hardware acceleration.
- `lsmod | grep nvidia`: Confirm the modules are loaded.
