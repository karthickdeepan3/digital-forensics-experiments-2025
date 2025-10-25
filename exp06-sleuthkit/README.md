# 🔍 Digital Forensics Experiment – Sleuth Kit (Ex. No. 6)

---

## 🎯 Aim
To analyze a forensic disk image using **The Sleuth Kit (TSK)** and extract file system information, partitions, and deleted files.

---

## 🧰 Requirements
- **Operating System:** Windows 10 or later  
- **Tool:** The Sleuth Kit v4.14.0  
- **Image Files:**  
  - `4Dell Latitude CPi.E01`  
  - `4Dell Latitude CPi.E02`  
- **Mounting Tool:** OSFMount (to create Local Disk E:)

---

## ⚙️ Setup Instructions

### 🪟 Step 1 — Install Sleuth Kit
Download and extract Sleuth Kit for Windows:
```
https://sleuthkit.org/
```
Extract or install to:
```
C:\Users\krthc\Downloads\sleuthkit-4.14.0-win32\sleuthkit-4.14.0-win32
```

### 💽 Step 2 — Mount the E01 Image
Use **OSFMount**:
1. Open OSFMount → Click **“Mount New”**
2. Select:
   ```
   4Dell Latitude CPi.E01
   ```
   *(Keep `.E02` in the same folder — it will auto-detect.)*
3. Choose:
   - **Mount entire image as read-only**
   - **Assign drive letter E:**
4. Click **Mount**

After mounting, verify “Local Disk (E:)” appears in File Explorer.

---

## 🧩 Analysis Using Sleuth Kit

### ⚙️ Step 1 — Open Command Prompt as Administrator
```
cd "C:\Users\krthc\Downloads\sleuthkit-4.14.0-win32\sleuthkit-4.14.0-win32\bin"
```

---

### 🔹 Step 2 — Analyze File System
```
fsstat \\.\E: > fsinfo.txt
```
**Description:**  
Extracts file system information (volume name, sector size, cluster info, timestamps).

---

### 🔹 Step 3 — List Partition Table
```
mmls \\.\E: > partitions.txt
```
**Description:**  
Displays partition layout and offsets.

---

### 🔹 Step 4 — List All Files (Including Deleted)
```
fls -r \\.\E: > filelist.txt
```
**Description:**  
Recursively lists all files and directories.  
Deleted files are marked with an asterisk `*`.

---

### 🔹 Step 5 — Recover a Deleted File (Optional)
If a deleted file (e.g., inode `128`) is found in `filelist.txt`, use:

```
icat \\.\E: 128 > recovered.jpg
istat \\.\E: 128 > metadata.txt
```

**Output:**
- `recovered.jpg` → the recovered deleted file  
- `metadata.txt` → inode information and timestamps (Modified, Accessed, Changed, Created)

---

## 📁 Output Files

| File | Description |
|------|--------------|
| `fsinfo.txt` | Detailed file system report |
| `partitions.txt` | Partition structure and sector offsets |
| `filelist.txt` | Recursive file and directory listing |
| `recovered.jpg` | Recovered deleted evidence file |
| `metadata.txt` | Metadata of the recovered file |

All outputs are generated and saved inside:
```
C:\Users\krthc\Downloads\sleuthkit-4.14.0-win32\sleuthkit-4.14.0-win32\bin
```

---

## 🧠 Understanding the Tools

| Tool | Purpose |
|------|----------|
| **fsstat** | Displays file system details |
| **mmls** | Lists partitions within a disk image |
| **fls** | Lists files, including deleted ones |
| **icat** | Extracts file content by inode |
| **istat** | Displays metadata information |

---

## ✅ Result
The `.E01` forensic image was successfully mounted as a virtual disk (E:) and analyzed using The Sleuth Kit.  
File system details, partitions, and deleted files were extracted and recovered, demonstrating digital evidence analysis using open-source forensic tools.

---

## 🧾 Viva Questions

1. What is the purpose of Sleuth Kit in digital forensics?  
2. What does an inode represent in a file system?  
3. What is the difference between `.E01` and `.raw` forensic images?  
4. Why must forensic images be analyzed in **read-only mode**?  
5. Which command in TSK is used to recover deleted files?

---

## 👨‍💻 Author Information
**Name:** Karthick Deepan K  
**Course:** B.Tech – Computer Science (Cyber Security)  
**Institution:** Kalasalingam Academy of Research and Education  
**Experiment:** Ex. No. 6 – Sleuth Kit Forensic Analysis  
**Date:** October 2025  
**OS Used:** Windows 11 
**Tools:** Sleuth Kit v4.14.0, OSFMount  

---

## 🏁 Summary
Through this experiment, the forensic image `4Dell Latitude CPi.E01` was successfully analyzed.  
TSK tools were used to extract file system metadata, view partition tables, and recover deleted evidence.  
This demonstrates the importance of Sleuth Kit in digital investigations for extracting and preserving digital evidence efficiently and reliably.

---
