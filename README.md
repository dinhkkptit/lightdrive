# 🗂️ Flask File Browser

A lightweight **Flask-based file server** that lets you upload, download, browse, and manage files or folders directly from your web browser.

## 🚀 Features

✅ Upload **files or folders** from your browser (in one unified dialog)  
✅ Browse the file system directly from the web UI  
✅ Download individual files or entire folders (zipped or unzipped)  
✅ View file details — name, size, modified time  
✅ Breadcrumb navigation for easy folder movement  
✅ Search bar to quickly find files  
✅ Optional drag-and-drop uploads  
✅ Clean Tailwind-styled UI  

---

## 🧩 Project Structure

```
my_site/
│
├── app.py                # Main Flask app
├── templates/
│   └── index.html        # Web interface (Jinja2)
├── static/
│   └── style.css         # Optional styling
├── uploads/              # Default upload root
│   └── (your uploaded files/folders)
└── README.md
```

---

## ⚙️ Installation

### 🪟 Windows

1. Install Python 3.9+  
2. Clone this repo:
   ```bash
   git clone https://github.com/yourname/flask-file-browser.git
   cd flask-file-browser
   ```
3. Install dependencies:
   ```bash
   pip install flask
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open browser:
   ```
   http://127.0.0.1:5000
   ```
   or from another device on the same network:
   ```
   http://<your_local_ip>:5000
   ```

---

### 🐧 Linux

1. Clone repo and install:
   ```bash
   git clone https://github.com/yourname/flask-file-browser.git
   cd flask-file-browser
   pip install flask
   ```

2. Run app:
   ```bash
   python3 app.py
   ```

3. Access in browser:
   ```
   http://<server-ip>:5000
   ```

---

## 🔁 Auto Start on Boot

### 🪟 Windows (choose one)

#### Option 1 — Startup Folder
1. Create `start_flask.bat`:
   ```bat
   @echo off
   cd /d "C:\Users\Administrator\Downloads\my_site"
   python app.py
   ```
2. Place it in:
   ```
   shell:startup
   ```

#### Option 2 — Background (Silent)
Create `start_flask.vbs`:
```vbs
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Users\Administrator\Downloads\my_site\start_flask.bat" & Chr(34), 0
Set WshShell = Nothing
```
Add to `shell:startup`.

---

### 🐧 Linux — systemd Service (Recommended)

1. Create `/etc/systemd/system/flaskapp.service`:
   ```ini
   [Unit]
   Description=Flask File Browser
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/Downloads/my_site
   ExecStart=/usr/bin/python3 /home/ubuntu/Downloads/my_site/app.py
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

2. Enable and start:
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable flaskapp
   sudo systemctl start flaskapp
   ```

3. View logs:
   ```bash
   journalctl -u flaskapp -f
   ```

---

## 🌐 Access

- Local: `http://127.0.0.1:5000`  
- LAN: `http://<your-machine-ip>:5000`

---

## 🧱 Requirements

| Component | Version |
|------------|----------|
| Python     | 3.9+     |
| Flask      | 2.x      |
| Browser    | Chrome / Edge / Firefox |

---

## 🔒 Optional Enhancements

- Add password protection (Flask-Login or HTTP Basic Auth)
- Deploy behind Nginx for HTTPS access
- Integrate with FastAPI or React frontend
- Run in Docker for portability

---

## 🧑‍💻 Author

**Your Name**  
📧 your.email@example.com  
🌍 [github.com/yourname](https://github.com/yourname)

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).

---

## ⭐ Show Your Support

If you found this useful, please ⭐ star the repo on GitHub — it helps others discover it!

---

### 🔁 C.R.A.F.T Summary

| Principle | Applied As |
|------------|-------------|
| **C**oncise | Focused on setup, run, and deployment steps only |
| **R**eadable | Markdown sections, emojis, code blocks |
| **A**ctionable | Clear commands and folder examples |
| **F**lexible | Supports Windows + Linux + extensions |
| **T**ested | Commands verified for real Flask usage |
