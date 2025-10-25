# 🧠 Experiment 10: Ghidra – Malware Disassembly and Analysis

---

## 🎯 Project Objectives
- Provide a hands-on guide to disassembling and analyzing malware with **Ghidra**.  
- Enable readers to recognize common malware functionalities such as persistence, anti-analysis techniques, and network communications.  
- Equip users with the skills to interpret low-level assembly and understand high-level behavior from decompiled code.  

---

## 🔒 Safety & Ethics
> **Important:** For safety and legal reasons, this project uses **benign** or synthetic samples only.  
> **Do not** load live malware on your host system — use an isolated virtual machine or sandbox, and keep snapshots.  

---

## 📦 Repository Components (Suggested)

ghidra-malware-analysis-project/
├── README.md
├── docs/
│   ├── Tutorial_Step1.md
│   ├── Tutorial_Step2.md
│   └── Tutorial_StepN.md
├── scripts/
│   ├── extract_strings.py
│   ├── network_analysis.py
│   └── label_functions.py
├── samples/
│   ├── benign_sample1.bin
│   └── benign_sample2.hex
├── templates/
│   └── analysis_report_template.md
└── screenshots/
    ├── function_graph_example.png
    └── decompiler_example.png

---

## ⚙️ Requirements
- **Ghidra** (latest recommended) — [https://ghidra-sre.org/](https://ghidra-sre.org/)  
- Virtual Machine (VirtualBox / VMware) or an isolated lab machine (snapshot-enabled)  
- Java Runtime (as required by Ghidra)  
- Optional: Visual Studio / GCC / MinGW to build benign samples  
- Basic familiarity with assembly (x86/x64) and C/C++  

---

## 🧭 Quick Start — Environment Setup
1. Create an **isolated VM** and take a snapshot.  
2. Install **Java** (as required by your Ghidra version).  
3. Download and extract **Ghidra**, then run:
   - Windows: `ghidraRun.bat`
   - Linux/Mac: `./ghidraRun`
4. Put benign sample binaries into the repo’s `samples/` folder.  

---

## 📝 Tutorial Steps (High-level)

### 1. Environment Setup
- Run Ghidra inside the VM.  
- Create a project (e.g., `GhidraLab`).  

### 2. Initial Analysis
- `File → New Project → Non-shared project`  
- `File → Import File` → select a sample from `samples/`  
- Accept defaults and click **Analyze** to run auto-analysis.  

### 3. Entry Point & Function Discovery
- In **CodeBrowser**, open **Symbol Tree → Functions**.  
- Identify `main` (or entry) and double-click to open.  

### 4. Decompiled View
- Open the **Decompiler** (F4) to view pseudocode and understand high-level behavior.  

### 5. Strings & Import Analysis
- `Search → For Strings` — look for suspicious text (URLs, file names, commands).  
- Check **Imports** to identify used APIs (networking, file, registry).  

### 6. Control Flow & Graphs
- Use **Function Graph** to visualize control flow and branches.  
- Use **XREFs** (cross-references) to see usage locations of functions/strings.  

### 7. Advanced Techniques (Optional)
- Use **Ghidra scripting (Python/Java)** for automation (see `/scripts`).  
- Use **Headless Analyzer** to batch-process many binaries.  
- Use **P-Code emulator** for limited dynamic inspection.  

---

## 🧩 Example Utility Scripts (Ideas)
- `extract_strings.py` — extract and categorize strings by type (network, file, commands).  
- `network_analysis.py` — heuristics to flag likely network-related behaviors.  
- `label_functions.py` — auto-label functions based on known patterns/signatures.  

> Include docstrings and comments in each script; store them in `/scripts`.

---

## 🧪 Sample Data (Safety-first)
- Use **benign binaries** that simulate malware-like behavior (`file write`, `system()` calls, `ping` to localhost).  
- Or generate **synthetic samples** from small C/C++ programs.  
- Consider **hex-dumps** as a safe alternative.  

---

## 🧾 Report Template (analysis_report_template.md)
Use these sections in your analysis report:

1. **Summary of Analysis**  
   - Short description of sample, suspicion level, environment snapshot details.  

2. **Function Analysis**  
   - Key functions, addresses, purpose (entry, persistence, comms).  

3. **Behavioral Indicators**  
   - Files created, registry edits, network calls, persistence mechanisms.  

4. **Evidence (Artifacts)**  
   - Strings, offsets, code addresses, screenshots (Decompiler, Graph, Strings, Imports).  

5. **Recommendations**  
   - Containment actions, further dynamic analysis, remediation suggestions.  

6. **Appendix**  
   - Commands used, script outputs, VM/Ghidra versions.  

---
## 🔎 Example Findings (for samples/benign_sample1.bin)

File analyzed: samples/benign_sample1.bin

Observed behaviors:
- Creates 'log.txt' in the working directory
- Attempts to call 'system("ping 127.0.0.1")' (simulated network)
- Writes startup-like file as persistence simulation
- Contains XOR obfuscated string that deobfuscates to 'ping.exe'

Important strings:
- "System check OK"
- "Startup simulation - do not run in production"

Noted imports:
- msvcrt!system
- kernel32!Sleep
- kernel32!GetTickCount
---


## 📸 Screenshots (What to Capture)
- Project view with sample loaded  
- Decompiler view showing `main` (pseudocode)  
- Function Graph (control flow)  
- Strings window showing important strings  
- Imports table showing external API usage  

> Save under `screenshots/` with descriptive filenames.  

---

## 🔧 Tips & Best Practices
- Always analyze a **copy** of the sample.  
- Work inside a **snapshot-enabled VM** to revert if needed.  
- Keep clear notes and timestamps for reproducibility.  
- Use **Ghidra scripts** to speed repetitive tasks and ensure consistency.  

---

## 🔮 Future Work Ideas
- Add **signature-based detection** for known malicious routines.  
- Build a **dataset of benign samples** that mimic malware behaviors for training.  
- Integrate **outputs from other disassemblers** for comparison.  
- Build a **web-based visualization (SVG/React)** to present analysis results.  

---

## 👤 Author
**Karthick Deepan K**  
B.Tech — Computer Science (Cyber Security)  
Kalasalingam Academy of Research and Education  

**Experiment:** Ex.No.10 — Ghidra Malware Analysis  

---

## 📜 License
This repository and its example code are provided for educational purposes under the **MIT License**.  
Use responsibly and ethically.


