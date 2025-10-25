# Tutorial Step 4 — Advanced techniques & automation

Advanced topics you can explore safely:

- Dynamic analysis (inside an isolated VM snapshot)
  - Instrument the VM and collect network traces only if the sample is controlled and benign.
- Custom Ghidra scripts
  - Use Python/Jython or Java to automate repetitive tasks. Example scripts are in `scripts/`.
- Obfuscation and unpacking
  - Look for decryption loops, large switch/case constructs, or self-modifying code patterns.
- P-Code emulator
  - Use Ghidra's emulator to step through small functions when dynamic execution is not possible.

Always prefer safe, benign samples when experimenting with advanced techniques.
