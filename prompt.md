
---

## ⚙️ `CRAFT_PROMPT.txt`

### 🧩 C.R.A.F.T. Prompt

**C — Context**  
I’m building a simple Flask-based local file manager website that allows me to upload, download, browse, and manage files or folders on my host. It should support both files and folders, show folder structure, file metadata, and be user-friendly like a lightweight Google Drive.

**R — Request**  
Help me create, update, or debug a Flask app (`app.py` + `browse.html` + other templates) that provides:

1. File/folder upload (manual and drag & drop)
2. File/folder browsing with breadcrumbs
3. File download (as file, ZIP, or TAR)
4. Delete functionality
5. File size and last-modified timestamps
6. Live search filtering
7. Pretty, responsive interface (HTML/CSS/JS)
8. Account creation and permission-based login (admin/editor/viewer)
9. Online text editor directly on the site

**A — Action**  
When I ask to “update,” give me a **fully working and ready-to-run** code version (not snippets), combining backend (`app.py`) and frontend (`browse.html`, etc.).  
Ensure:

- URLs always use `/`, not `\`  
- Uploads preserve folder structure  
- Downloads work for both files and folders  
- Browsing dynamically reflects filesystem  
- Only authorized users can modify/delete files

**F — Format**  
- Complete, copy-pasteable code blocks (Python + HTML/JS)  
- Short explanations of changes  
- Optional UI improvements when requested

**T — Tone**  
Developer-friendly, clear, practical.  
Focus on real usability and stability.

---

### ✅ Example Usage

> “Using my CRAFT Flask file browser context, add password protection and dark theme.”  
> “Update it to support TAR and ZIP folder downloads side by side.”  
> “Make drag-and-drop show a progress bar.”  
> “Add syntax highlighting to the file editor.”
