# 🌐 Experiment 3: Wireshark

**Aim:**  
To use **Wireshark** for capturing and analyzing network packets for forensic investigation.

---

## 📝 Procedure

### Step 1: Capture Live Traffic
- Open Wireshark and select the appropriate network interface.  
- Begin live packet capture.  

### Step 2: Apply Filters
- Use display filters such as `http`, `tcp.port==80`, or `ip.addr==192.168.1.1`.  
- Narrow down traffic to focus on suspicious activity.  

### Step 3: Analyze Packets
- Inspect individual packet details (source, destination, payload).  
- Identify potential anomalies such as unauthorized access, malware, or suspicious communication.  

---

## ✅ Conclusion
- Successfully captured and analyzed live network traffic.  
- Applied filters to isolate relevant data.  
- Wireshark is a powerful tool for **network forensic analysis**, enabling investigators to trace malicious activity.  

---
## 🖼️ Screenshot Gallery

| # | Screenshot | Caption |
|---|------------|---------|
| 1 | ![Live capture](screenshots/Screenshot%202025-09-01%20194432.png) | **Live capture on Wi-Fi interface** (mixed QUIC/SSDP/TCP traffic) |
| 2 | ![Login page](screenshots/Screenshot%202025-09-01%20194634.png) | **Target app: Acunetix test login page** (credentials submitted) |
| 3 | ![HTTP filter](screenshots/Screenshot%202025-09-01%20194700.png) | **Display filter `http`** — GETs for page & assets (login.php, CSS, logo, favicon) |
| 4 | ![GET only](screenshots/Screenshot%202025-09-01%20194733.png) | **`http.request.method == "GET"`** — isolating GET requests |
| 5 | ![POST only](screenshots/Screenshot%202025-09-01%20195042.png) | **`http.request.method == "POST"`** — credential POST to `/userinfo.php` |
## 📂 Portfolio Files
- 📄 [Experiment Report (PDF)](Ex.No.3-Wireshark.pdf)  
- 🖼️ [All Screenshots](screenshots/) 
