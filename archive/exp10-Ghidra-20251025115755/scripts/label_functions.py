"""
label_functions.py

Example Ghidra script (Jython-style) that labels functions which reference certain
strings. This file is for demonstration and should be run inside Ghidra's scripting
environment (Script Manager) or via the headless analyzer with appropriate setup.

The script is intentionally conservative: it only renames functions when it detects
a known string reference and writes comments. Do not run this outside of Ghidra.

Note: This file is a reference/example; it's not executed by the Python 3 host.
"""
# The following is example code for use with Ghidra's scripting environment.
# Save this snippet into Ghidra's script manager or adapt it for headless use.

ghidra_script_content = r'''
from ghidra.program.model.symbol import SourceType
from ghidra.util.task import ConsoleTaskMonitor

def rename_functions_using_strings(program, keywords):
    listing = program.getListing()
    data_iter = listing.getDefinedData(True)
    monitor = ConsoleTaskMonitor()
    while data_iter.hasNext() and not monitor.isCancelled():
        data = data_iter.next()
        try:
            val = data.getValue()
        except Exception:
            continue
        if val is None:
            continue
        s = str(val)
        for kw in keywords:
            if kw in s:
                # find references to this data and rename caller functions
                refs = data.getReferenceIteratorTo()
                while refs.hasNext():
                    ref = refs.next()
                    addr = ref.getFromAddress()
                    func = listing.getFunctionContaining(addr)
                    if func is not None:
                        new_name = func.getName() + "_refs_%s" % kw.replace(' ', '_')
                        func.setName(new_name, SourceType.ANALYSIS)
                        func.setComment(func.getEntryPoint(), "Auto-labeled by script: contains %s" % kw)

keywords = ["http", "socket", "CreateFileA", "RegSetValueExA"]
rename_functions_using_strings(currentProgram, keywords)
'''

with open('scripts/label_functions_example_for_ghidra.txt', 'w') as f:
    f.write(ghidra_script_content)

print('Wrote a Ghidra-compatible example script to scripts/label_functions_example_for_ghidra.txt')
