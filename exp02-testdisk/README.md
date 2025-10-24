# 💽 Experiment 2: TestDisk

**Aim:**  
To use **TestDisk** for recovering lost partitions and deleted files, validating disk integrity, and understanding forensic recovery processes.  

---

## 📝 Procedure  

### Step 1: Launch TestDisk  
- Open **TestDisk** from the terminal or executable.  
- Choose whether to create a log file.  

### Step 2: Select Target Disk  
- Select the target disk to recover.  
- Example: `Disk \\.\PhysicalDrive0 – 256 GB / 238 GiB`.  

### Step 3: Choose Partition Table Type  
- TestDisk auto-detects the partition type (EFI GPT in modern systems).  

### Step 4: Run Analysis  
- Perform **Quick Search** to find partitions.  
- If missing partitions remain, use **Deeper Search**.  

### Step 5: Recover Partitions  
- Mark valid partitions.  
- Write them to the disk to recover.  

### Step 6: Verify Recovered Data  
- Mount and check recovered partitions.  
- Verify integrity of restored files.  

---

## ✅ Conclusion  
- Successfully recovered deleted/lost partitions.  
- Verified disk structure using TestDisk.  
- Demonstrated forensic disk recovery using open-source tools.  

---
## 🖼️ Screenshot Gallery  

| # | Screenshot | Caption |
|---|------------|---------|
| 1 | ![Log creation](screenshots/Screenshot%202025-09-01%20203725.png) | **Start TestDisk** – Create new log file |
| 2 | ![Disk selection](screenshots/Screenshot%202025-09-01%20203746.png) | **Disk selection** – Selected PhysicalDrive0 (256 GB SSD) |
| 3 | ![Partition type](screenshots/Screenshot%202025-09-01%20203814.png) | **Partition table type** – EFI GPT detected |
| 4 | ![Analyse](screenshots/Screenshot%202025-09-01%20203831.png) | **Analyse selected disk** – Ready for structure analysis |
| 5 | ![Current structure](screenshots/Screenshot%202025-09-01%20203851.png) | **Current partition structure** – Multiple MS Reserved & Data partitions listed |
| 6 | ![Quick search](screenshots/Screenshot%202025-09-01%20203918.png) | **Quick Search running** – Partition scan in progress |
| 7 | ![Search results](screenshots/Screenshot%202025-09-01%20203940.png) | **Quick Search results** – Found multiple partitions (EFI, MS Data, Linux filesystem) |
| 8 | ![Partition selection](screenshots/Screenshot%202025-09-01%20204101.png) | **Partition selection** – Marked partitions for recovery |
| 9 | ![Write table](screenshots/Screenshot%202025-09-01%20204119.png) | **Write partition table** – Confirmation prompt (Y/N) |

## 📂 Portfolio Files  
- 📄 [Experiment Report (PDF)](Ex.No.2-TestDisk.pdf)  
 - 🖼️ [Screenshots](screenshots/)  
