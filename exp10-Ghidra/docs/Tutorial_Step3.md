# Tutorial Step 3 — Function, strings and import analysis

1. Function analysis
   - Open key functions in the Decompiler and Listing views.
   - Rename functions and variables to meaningful names as you understand behavior.
   - Use the Function Graph to inspect control flow.

2. Strings & imports
   - Open the Strings window (Window -> Defined Strings) and look for I/O, URLs, commands.
   - Check imported libraries and API calls; network, filesystem, and registry APIs are especially relevant.

3. Cross references and data flow
   - Use Xrefs to locate callers and data usage.
   - Trace data flow for suspicious strings or buffers.

4. Document findings inline
   - Add comments in Ghidra for important instructions and annotate decompiled code.
