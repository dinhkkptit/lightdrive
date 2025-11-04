### 🧩 **C.R.A.F.T. Prompt Summary**

**C — Context**  
I’m building a simple Flask-based local file manager website that allows me to upload, download, browse, and manage files or folders on my host. It should support both files and folders, show folder structure, file metadata, and be user-friendly like a lightweight Google Drive.

**R — Request**  
Help me create, update, or debug a Flask app (`app.py` + `browse.html`) that provides:

1. File/folder upload (manual selection and drag & drop)
    
2. File/folder browsing with breadcrumb navigation
    
3. File download (as file, ZIP, or TAR)
    
4. Delete functionality
    
5. File size and last-modified timestamps
    
6. Live search filtering
    
7. (Optional) Pretty, responsive interface using HTML/CSS/JS
    

**A — Action**  
When I ask to “update,” give me a **fully working and ready-to-run** code version (not just snippets), combining backend (`app.py`) and frontend (`browse.html`) logic.  
Ensure:

- URLs always use `/` not `\`
    
- Uploads preserve folder structure
    
- Downloads work for both single files and whole folders (ZIP or TAR options)
    
- Browsing dynamically updates based on the server’s filesystem
    

**F — Format**  
Provide answers as:

- Complete, copy-pasteable code blocks (Python + HTML/JS)
    
- Brief explanations of what changed and why
    
- Optional UI improvements (if asked)
    

**T — Tone**  
Clear, practical, developer-friendly.  
No unnecessary jargon.  
Focus on real functionality, usability, and stability.

---

### ✅ Example Usage

> “Using my CRAFT Flask file browser context, add password protection and dark theme.”  
> “Update it to support TAR and ZIP folder downloads side by side.”  
> “Make drag-and-drop show a progress bar.”

---
