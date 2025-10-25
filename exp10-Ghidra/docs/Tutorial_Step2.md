# Tutorial Step 2 — Initial static analysis with Ghidra

This step explains how to import a sample into Ghidra and perform initial static analysis.

1. Start Ghidra and create a new Project (Non-Shared)
2. Import a benign sample (use the sample generator in `scripts/` if you don't have one)
3. Run Auto-Analysis
   - Accept defaults initially; you can refine options later.
4. Identify program entry points and the `main`-like functions
5. Use the Symbol Tree to inspect functions, imports, and strings

Tips
- Use the Decompiler view to obtain a pseudocode view of functions.
- Use Cross References (Xrefs) to see who calls a function or references data.

This document focuses on static analysis only — avoid running unknown binaries.
