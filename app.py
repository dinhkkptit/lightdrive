from flask import Flask, render_template, request, send_from_directory, redirect, url_for, abort
import os
import zipfile
import pathlib
import shutil
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def get_path(subpath=""):
    """Get full filesystem path from relative web path"""
    safe_path = os.path.normpath(os.path.join(app.config["UPLOAD_FOLDER"], subpath))
    if not safe_path.startswith(app.config["UPLOAD_FOLDER"]):
        abort(403)  # prevent directory traversal
    return safe_path


@app.route("/", defaults={"subpath": ""})
@app.route("/browse/<path:subpath>")
def browse(subpath):
    """Browse files and folders"""
    folder_path = get_path(subpath)
    if not os.path.exists(folder_path):
        abort(404)

    items = os.listdir(folder_path)
    files = []
    dirs = []

    for item in items:
        full_path = os.path.join(folder_path, item)
        rel_path = os.path.relpath(full_path, app.config["UPLOAD_FOLDER"])
        rel_path = pathlib.PurePath(rel_path).as_posix()
        if os.path.isdir(full_path):
            dirs.append(rel_path)
        else:
            files.append(rel_path)

    parent = os.path.dirname(subpath)
    parent_url = url_for("browse", subpath=parent) if subpath else None

    return render_template(
        "index.html",
        files=sorted(files),
        dirs=sorted(dirs),
        current=subpath,
        parent_url=parent_url,
    )


@app.route("/upload", methods=["POST"])
def upload_file():
    """Upload files and folders into the current directory"""
    subpath = request.form.get("path", "")
    folder_path = get_path(subpath)

    if "file" not in request.files:
        return "No file part", 400

    files = request.files.getlist("file")
    for file in files:
        if not file.filename:
            continue

        # Detect relative folder paths for folder uploads
        # Chrome sends them as file.webkitRelativePath
        relative_path = file.filename
        # Handle both normal and folder uploads
        if hasattr(file, "filename") and hasattr(file, "mimetype") and hasattr(file, "stream"):
            relpath = getattr(file, "webkitRelativePath", None) or file.filename
        else:
            relpath = file.filename

        filename = secure_filename(os.path.basename(relpath))
        dir_part = os.path.dirname(relpath)

        # Construct target folder path inside uploads
        target_dir = os.path.join(folder_path, dir_part)
        os.makedirs(target_dir, exist_ok=True)

        save_path = os.path.join(target_dir, filename)
        file.save(save_path)

    return redirect(url_for("browse", subpath=subpath))


@app.route("/download/<path:filename>")
def download_file(filename):
    """Download file or folder (as zip)"""
    file_path = get_path(filename)
    if not os.path.exists(file_path):
        abort(404)

    if os.path.isdir(file_path):
        zip_path = file_path + ".zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(file_path):
                for f in files:
                    full_path = os.path.join(root, f)
                    rel_path = os.path.relpath(full_path, file_path)
                    zipf.write(full_path, rel_path)
        return send_from_directory(os.path.dirname(zip_path), os.path.basename(zip_path), as_attachment=True)

    return send_from_directory(app.config["UPLOAD_FOLDER"], filename, as_attachment=True)


@app.route("/delete/<path:filename>", methods=["POST"])
def delete_file(filename):
    """Delete a file or folder"""
    file_path = get_path(filename)
    if os.path.exists(file_path):
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)

    parent = os.path.dirname(filename)
    return redirect(url_for("browse", subpath=parent))

@app.template_filter("datetimeformat")
def datetimeformat(value):
    return datetime.fromtimestamp(value).strftime("%Y-%m-%d %H:%M:%S")

@app.context_processor
def inject_helpers():
    return dict(get_path=get_path, os=os)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
