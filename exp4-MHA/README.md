# 📧 Experiment 4: Mail Header Analyzer (MHA)

**Aim:**  
To trace an email's origin and verify its authenticity by examining its header for signs of spoofing using a **Mail Header Analyzer**.

---

## 📝 Procedure

### Step 1: Get the Email Header
- Open the email client (e.g., Gmail).  
- Use **Show Original** to copy the full raw header.  

### Step 2: Use Mail Header Analyzer Tool
- Navigate to an analyzer site like **MXToolbox – Email Header Analyzer**.  
- Paste the raw header into the input box.  
- Click **Analyze** to generate a parsed, human-readable report.  

### Step 3: Analyze SPF, DKIM, DMARC
- **SPF** (Sender Policy Framework): Passed – sending server is authorized.  
- **DKIM** (DomainKeys Identified Mail): Authentication failed ❌ (signature mismatch).  
- **DMARC** (Domain-based Message Authentication, Reporting & Conformance): Passed ✅  

### Step 4: Trace Delivery Path
- Review the email’s delivery route.  
- Confirm if the sending server (e.g., Mailgun server) matches the SPF record.  

### Step 5: Investigate DKIM Failure
- Analyze why DKIM failed while SPF & DMARC passed.  
- This indicates a possible issue with the signing domain or unauthorized modification.  

---

## ✅ Conclusion
- Email passed **SPF and DMARC**, confirming authorized sending servers.  
- **DKIM authentication failed**, raising concerns about integrity.  
- Demonstrates the importance of checking **all three standards (SPF, DKIM, DMARC)** for detecting spoofing attempts.  

---
| **S.No** | **Step / Description**                       | **Screenshot Filename**            |
| -------- | -------------------------------------------- | ---------------------------------- |
| 1        | Viewing the original email in Gmail          | `Screenshot 2025-09-01 190154.png` |
| 2        | Copying the raw email header                 | `Screenshot 2025-09-01 190224.png` |
| 3        | Pasting header into MXToolbox analyzer       | `Screenshot 2025-09-01 190439.png` |
| 4        | Relay path analysis result                   | `Screenshot 2025-09-01 190530.png` |
| 5        | SPF and DKIM authentication details          | `Screenshot 2025-09-01 190554.png` |
| 6        | Detailed DKIM & DMARC verification           | `Screenshot 2025-09-01 190646.png` |
| 7        | Final email authenticity & compliance result | `Screenshot 2025-09-01 190702.png` |
## 📂 Portfolio Files
- 📄 [Experiment Report (PDF)](Ex.No.4-MHA.pdf)  
 - 🖼️ [All Screenshots](screenshots/) 
