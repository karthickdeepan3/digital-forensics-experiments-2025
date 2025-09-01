# 📧 Experiment 4: Mail Header Analysis (MHA)

**Aim:**  
The aim is to use a Mail Header Analyzer (MHA) to trace an email's origin and verify its authenticity by examining its header for signs of spoofing.

---

## 📝 Procedure

### Step 1: Get the Email Header
- Open the email and copy the **full raw header**.  
- **Gmail:** Open the email → click the three dots (⋮) → select **Show original**.  



---

### Step 2: Use a Mail Header Analyzer
- Go to an online tool like **MXToolbox Email Header Analyzer**.  
- Paste the header text into the analyzer box and click **Analyze**.  



---

### Step 3: Analyze the Report
The analyzer will display SPF, DKIM, and DMARC results.  

- ✅ **DMARC Compliance**: Passed (email is DMARC Compliant).  
- ✅ **SPF Status**: Authenticated + Alignment Passed → sending server authorized.  
- ⚠️ **DKIM Status**: Alignment passed, but **Authentication failed ❌** → indicates signature problem.  



---

### Step 4: Investigate SPF Record & Email Path
- SPF record: `v=spf1 include:mailgun.org ~all` → Mailgun servers are authorized.  
- Delivery path: Email sent via `m241-136.mailgun.net`.  



---

### Step 5: Analyze DKIM Failure
- The DKIM authentication failed, showing the email’s **digital signature** didn’t verify correctly.  
- This is a **critical finding** that could indicate spoofing or misconfiguration.  


---

## ✅ Conclusion
The email was:
- SPF: **Valid** (authorized Mailgun server).  
- DMARC: **Compliant**.  
- DKIM: **Failed** ❌ (signature mismatch).  

🔎 **Overall:** While the email appears mostly legitimate, the DKIM failure highlights a potential integrity issue → further investigation is recommended.  

---

## 📂 Portfolio Files
- 📄 [Experiment Report (PDF)](Ex.No.4-MHA.pdf)  

- 🖼️ [Screenshots](screenshots/)  
