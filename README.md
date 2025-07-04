#  INFOSAGE - Website Footprinting Toolkit
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Kali%20Linux-lightgrey)
![Status](https://img.shields.io/badge/status-Stable-brightgreen)
![Contributions](https://img.shields.io/badge/contributions-Welcome-orange)

---

##  Description
**Infosage** is a fast, modular website footprinting toolkit by **Genos**, built for cybersecurity professionals, ethical hackers, and penetration testers. It automates domain reconnaissance with WHOIS, DNS, email, subdomain, and Nmap scans, featuring progress bars, color-coded outputs, and auto tool installation.

It is a powerful, modular website footprinting toolkit developed for cybersecurity professionals, ethical hackers, and penetration testers. It automates essential reconnaissance tasks such as WHOIS lookups, DNS queries, email enumeration, subdomain discovery, and Nmap scanning, all in one streamlined tool.

Infosage is built with simplicity and efficiency in mind. It features a clean, menu-driven interface that guides users through each step of the footprinting process. Even beginners can comfortably use the tool, while experienced professionals will appreciate its speed and automation capabilities.

The toolkit integrates real-time progress bars, color-coded terminal outputs, and auto-installation of missing tools to provide a smooth and responsive user experience. Infosage ensures you are connected to the internet before execution, preventing wasted time and incomplete scans.

All gathered results are automatically saved and neatly organized in the `footprint_results` directory, making it easy to review and analyze your findings later. This saves time and keeps your recon data structured.

Infosage is optimized for Kali Linux environments but can be adapted to other Linux distributions with minimal adjustments. Whether you’re conducting professional penetration tests or learning cybersecurity, Infosage helps you work faster, stay organized, and dig deeper into your targets.


---
## Screenshots

### 🔸 Banner
![Banner](banner.png)

### 🔸 Tools Menu
![Tools Menu](tools.png)

### 🔸 Command Executed
![Command Executed](cmdrun.png)

### 🔸 Viewing Saved Result
![View Saved Result](result.png)

---
## 🛠️ Installation Guide

Follow these steps to install **Infosage** on your system:

### Step 1: Clone the Repository
```bash
git clone https://github.com/GenoS-x15/Infosage.git 
cd Infosage
```
### Step 2: Install Python Dependencies
```bash
pip install tqdm colorama
```
---
## Usage Guide
---
```bash
python3 Infosage.py <target-domain>
```
  for Example: python3 Infosage.py microsoft.com

## Features
- WHOIS Lookup
- DNS Lookup
- Host IP Resolution
- Email Enumeration (theHarvester)
- DNS Enumeration (dnsenum)
- Subdomain Enumeration (Sublist3r)
- Nmap Basic Scan
- Full Automated Footprinting
- Real-Time Progress Bars & Colorized Output
- Auto-Installation of Missing Tools
- Internet Connectivity Check
- Organized Result Logging

---

## Requirements
- Python 3.x
- Kali Linux (or compatible Linux)
---
## Author
 **Genos aka (Shubham Singh Rajput)**
- Developer and Creator of Infosage – Website Footprinting Toolkit


---
### Developer's Note

I am a **full-time cybersecurity enthusiast** passionate about building tools for the community. If you are interested in learning, collaborating, or simply want to explore cybersecurity together, please **connect with me on LinkedIn** and follow my work to stay updated with more interesting tools and future releases.

🔗 [Connect on LinkedIn](https://www.linkedin.com/in/r-shubham02/) 

---

###  Pull Requests

Pull requests are generally welcome. However, please keep in mind:
- I am actively working on **new tools** and maintaining several existing ones.
- My response time may vary due to ongoing projects.

If you have an idea for a **significant feature or large code addition**, please contact me first to check if something similar is already in progress. This helps prevent duplicated effort and ensures smooth project alignment.

Thank you for your interest and support! 
