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
## 🖼️ Screenshot Gallery
| # | Screenshot | Caption |
|---|------------|---------|
| 1 | ![Original Email](screenshots/Screenshot%202025-09-01%20190154.png) | **Original email in Gmail** (LinkedIn notification mail) |
| 2 | ![Raw Header](screenshots/Screenshot%202025-09-01%20190224.png) | **Viewing raw email header** from Gmail → “Show original” |
| 3 | ![Header Analyzer](screenshots/Screenshot%202025-09-01%20190439.png) | **Pasting header into MXToolbox** Email Header Analyzer |
| 4 | ![Relay Path](screenshots/Screenshot%202025-09-01%20190530.png) | **Relay path analysis** (LinkedIn → Google mail servers) |
| 5 | ![SPF & DKIM](screenshots/Screenshot%202025-09-01%20190554.png) | **SPF & DKIM authentication details** extracted |
| 6 | ![DMARC](screenshots/Screenshot%202025-09-01%20190646.png) | **Detailed DKIM + DMARC verification** results |
| 7 | ![Final Summary](screenshots/Screenshot%202025-09-01%20190702.png) | **Final email compliance summary** (SPF, DKIM, DMARC all ✅) |


## 📂 Portfolio Files
- 📄 [Experiment Report (PDF)](Ex.No.4-MHA.pdf)  
 - 🖼️ [All Screenshots](screenshots/) 
