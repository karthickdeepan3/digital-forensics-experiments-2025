# Tutorial Step 1 — Environment setup (Safe)

This step covers how to prepare a safe environment for static and dynamic analysis.

1. Create an isolated virtual machine
   - Use VirtualBox, VMware, or Hyper-V.
   - Snapshot the VM before starting analysis.
   - Disable or carefully control networking; use host-only or NAT with firewall rules.

2. Install Ghidra
   - Download from the official site: https://ghidra-sre.org
   - Follow the official install instructions for your OS.

3. Configure a shared folder (optional)
   - Use a read-only shared folder to move samples into the VM if needed.

4. Tools inside the VM (optional)
   - Ghidra
   - A safe file viewer (hex editor)
   - Wireshark (if doing controlled network captures)

Important: Do not execute untrusted binaries on your host machine. If dynamic analysis is required, perform it only inside the VM and on a snapshot you can revert.
