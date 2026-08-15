# flask_05_forms.py
# Section: Form Handling
# Demonstrates: request.form, server-side validation, PRG pattern, file uploads
# Requires: templates/contact.html, templates/thanks.html
# Run: python flask_05_forms.py

import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024   # 2 MB limit

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "pdf"}

# Create uploads folder if it doesn't exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# ------------------------------------------------------------------
# Contact form: GET renders the form, POST processes it (PRG pattern)
# Visit: http://127.0.0.1:5000/contact
# ------------------------------------------------------------------
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name    = request.form.get("name", "").strip()
        email   = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        # Basic server-side validation
        if not name or not email or not message:
            error = "All fields are required."
            return render_template("contact.html", error=error)

        # Process the data (e.g., save to database or send email)
        print(f"Message from {name} <{email}>: {message}")

        # Redirect after successful POST (PRG pattern)
        return redirect(url_for("contact_thanks"))

    return render_template("contact.html")

@app.route("/contact/thanks")
def contact_thanks():
    return render_template("thanks.html")

# ------------------------------------------------------------------
# File upload: accepts images and PDFs up to 2 MB
# Visit: http://127.0.0.1:5000/upload
# ------------------------------------------------------------------
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            return "No file selected.", 400
        if not allowed_file(file.filename):
            return "File type not allowed.", 400

        filename = secure_filename(file.filename)   # sanitise the name
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        return f"File '{filename}' uploaded successfully."

    return '''
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <button type="submit">Upload</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
