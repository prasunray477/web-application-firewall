# Machine Learning Based Web Application Firewall (WAF)

This project implements a **Web Application Firewall (WAF)** powered by **Machine Learning**.  
It works as a **local HTTP proxy server** that analyzes requests in real-time, extracts key features, and predicts whether they are **benign or malicious**.

---

## Features
- Acts as a proxy server on `localhost:8080`
- Extracts features from HTTP requests (special characters, SQL keywords, suspicious patterns, etc.)
- Supports ML model:
  - Random Forest Classifier
- Real-time intrusion detection (`Bad Request` or `Good Request`)
- Can proxy requests to **any website**, not just a single target
- Easy to extend with new features or models


---

## Dataset
- The model is trained on a dataset of **HTTP requests**, with labels:
  - `0` → Benign request
  - `1` → Malicious request
- Features include:
  - Quotes (`'`, `"`)
  - SQL patterns (`--`, `union`, `select`, etc.)
  - Script tags (`<`, `>`, `script`)
  - Special characters (`$`, `|`, `&`)
  - Path and body length
- You can expand the dataset using **open-source WAF datasets** (e.g., Kaggle FWAF dataset, WebEye, ModSec-Learn).

---

## Installation & Usage

### 1. Clone the repo
```bash
git clone https://github.com/your-username/web-application-firewall.git
cd web-application-firewall
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Train the model 
```bash
python waf_training.py
```
### 4. Run the proxy server
```bash
python proxy_server.py

#Server starts at:
http://127.0.0.1:8080
```
### 5. Test with a website.



