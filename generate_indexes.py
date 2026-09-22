#!/usr/bin/env python3
"""
generate_indexes.py — build an index.html + README.md in every demo folder.

Run it from the ROOT of your demo repo:

    python3 generate_indexes.py

What it does, for each folder (recursively, skipping .git, node_modules, assets, etc.):
  • writes an index.html — a clean landing page that links to every .html demo
    in that folder and to any sub-folders (so GitHub Pages opens a real page,
    not a file listing);
  • writes a README.md IF one does not already exist (never overwrites yours).
It also writes a root index.html that links to each chapter folder.

Re-run any time you add or rename demos. Links are relative, so they work both
locally and on GitHub Pages (https://<user>.github.io/<repo>/...).
"""
import os, re, html, sys

# ---------- settings (edit if you like) ----------
COURSE   = "SOEN 287 · Web Programming"
BOOK     = "Web Programming: With Modern Full-Stack Technology"
SKIP_DIRS = {".git", ".github", "node_modules", "__pycache__", "venv", ".venv",
             "env", "dist", "build", "assets", "images", "img", "css", "js",
             "lib", "vendor", "static"}
NAVY, GOLD, INK, MUTED, BG, CARD = "#16243b", "#d6a23a", "#1b2430", "#5b6572", "#ffffff", "#f5f3ef"
# -------------------------------------------------

ACRONYMS = {"css","html","html5","css3","js","dom","json","api","jwt","http","https",
            "ui","ux","php","sql","ajax","url","npm","xml","svg","rest"}

def pretty(name: str) -> str:
    base = os.path.splitext(name)[0]
    base = re.sub(r"[_\-]+", " ", base)
    base = re.sub(r"(?<=[A-Za-z])(?=\d)|(?<=\d)(?=[A-Za-z])", " ", base)  # split letter<->digit
    base = re.sub(r"\s+", " ", base).strip()
    words = []
    for w in base.split(" "):
        if not w: continue
        words.append(w.upper() if w.lower() in ACRONYMS else w[:1].upper() + w[1:])
    return " ".join(words) or name

def esc(s): return html.escape(s, quote=True)

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Demos</title>
<style>
  :root {{ --navy:{navy}; --gold:{gold}; --ink:{ink}; --muted:{muted}; --bg:{bg}; --card:{card}; }}
  * {{ box-sizing: border-box; }}
  body {{ margin:0; font-family: -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif;
          color: var(--ink); background: var(--bg); line-height:1.5; }}
  header {{ background: var(--navy); color:#fff; padding: 28px 24px; }}
  .wrap {{ max-width: 960px; margin: 0 auto; padding: 0 24px; }}
  header .wrap {{ padding: 0; }}
  .kicker {{ color: var(--gold); font-size:.72rem; letter-spacing:.16em; font-weight:700; text-transform:uppercase; margin:0 0 6px; }}
  h1 {{ font-family: Georgia, "Times New Roman", serif; font-size: 1.9rem; margin:.1rem 0 .2rem; }}
  header p {{ margin:.2rem 0 0; color:#c9d2df; font-size:.95rem; }}
  main {{ padding: 26px 0 40px; }}
  h2 {{ font-size:.8rem; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); margin:22px 0 10px; }}
  .grid {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(230px,1fr)); gap:14px; }}
  a.card {{ display:block; text-decoration:none; color:var(--ink); background:var(--card);
            border:1px solid #e7e2d8; border-left:4px solid var(--gold); border-radius:10px;
            padding:14px 16px; transition:transform .06s ease, box-shadow .12s ease; }}
  a.card:hover {{ transform: translateY(-2px); box-shadow:0 6px 16px rgba(22,36,59,.10); }}
  a.card.dir {{ border-left-color: var(--navy); }}
  .name {{ font-weight:700; font-size:1.02rem; }}
  .file {{ color:var(--muted); font-size:.82rem; font-family: ui-monospace, Menlo, Consolas, monospace; margin-top:3px; }}
  .note {{ background:#fbf3d9; border:1px solid #efe2b8; border-radius:10px; padding:12px 16px; color:#5a4b1e; font-size:.92rem; }}
  footer {{ border-top:1px solid #e7e2d8; color:var(--muted); font-size:.85rem; padding:18px 0 40px; }}
  footer a {{ color: var(--navy); }}
</style>
</head>
<body>
<header><div class="wrap">
  <p class="kicker">{course} · Demo code</p>
  <h1>{title}</h1>
  <p>{subtitle}</p>
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">
  {up}Companion code for <em>{book}</em>.
</div></footer>
</body>
</html>
"""

def build_index(folder, is_root=False):
    entries = sorted(os.listdir(folder))
    html_files = [f for f in entries if f.lower().endswith((".html", ".htm")) and f.lower() != "index.html"]
    subdirs = [f for f in entries if os.path.isdir(os.path.join(folder, f)) and f not in SKIP_DIRS and not f.startswith(".")]
    other = [f for f in entries if f.lower().endswith((".js", ".mjs", ".cjs", ".py", ".json")) and not f.startswith(".")]

    title = "Demo Code" if is_root else pretty(os.path.basename(os.path.abspath(folder)))
    subtitle = ("Browse the runnable demos by chapter." if is_root
                else "Front-end demos open in the browser. Server demos (Node.js / Flask) run locally.")
    parts = []

    if subdirs:
        parts.append('<h2>' + ("Chapters" if is_root else "Folders") + '</h2>\n<div class="grid">')
        for dnm in subdirs:
            parts.append(f'  <a class="card dir" href="{esc(dnm)}/"><span class="name">{esc(pretty(dnm))}</span>'
                         f'<div class="file">{esc(dnm)}/</div></a>')
        parts.append('</div>')

    if html_files:
        parts.append('<h2>Demos</h2>\n<div class="grid">')
        for f in html_files:
            parts.append(f'  <a class="card" href="{esc(f)}"><span class="name">{esc(pretty(f))}</span>'
                         f'<div class="file">{esc(f)}</div></a>')
        parts.append('</div>')

    if not html_files and other and not is_root:
        parts.append('<div class="note"><strong>Server-side demo.</strong> These files run on a server '
                     '(e.g. <code>node server.js</code> or <code>flask run</code>), not in the browser — '
                     'see the README, and run them locally.</div>')
        parts.append('<h2>Source files</h2>\n<div class="grid">')
        for f in other:
            parts.append(f'  <a class="card" href="{esc(f)}"><span class="name">{esc(f)}</span></a>')
        parts.append('</div>')

    if not (subdirs or html_files or other):
        parts.append('<div class="note">No demos in this folder yet.</div>')

    up = '' if is_root else '<a href="../index.html">← All chapters</a> &nbsp;·&nbsp; '
    out = PAGE.format(title=esc(title), subtitle=esc(subtitle), course=esc(COURSE), book=esc(BOOK),
                      body="\n".join(parts), up=up,
                      navy=NAVY, gold=GOLD, ink=INK, muted=MUTED, bg=BG, card=CARD)
    with open(os.path.join(folder, "index.html"), "w", encoding="utf-8") as fh:
        fh.write(out)
    return html_files, subdirs, other

def build_readme(folder, html_files, other, is_root=False):
    path = os.path.join(folder, "README.md")
    if os.path.exists(path):
        return False  # never overwrite an existing README
    title = "Demo Code" if is_root else pretty(os.path.basename(os.path.abspath(folder)))
    lines = [f"# {title}", ""]
    if is_root:
        lines += [f"Companion demo code for *{BOOK}* ({COURSE}).", "",
                  "Open **index.html** (or the GitHub Pages link) to browse the demos by chapter."]
    else:
        lines += [f"Demo code for **{title}** — from *{BOOK}* ({COURSE}).", "",
                  "Open **index.html** (or the GitHub Pages link) to browse the demos."]
        if html_files:
            lines += ["", "## Demos", ""] + [f"- `{f}` — _describe this demo_" for f in html_files]
        if other and not html_files:
            lines += ["", "> Server-side demo — run it locally (e.g. `node server.js` or `flask run`).", "",
                      "## Files", ""] + [f"- `{f}`" for f in other]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    return True

def main():
    root = os.getcwd()
    made_idx = made_rd = 0
    for cur, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        is_root = (os.path.abspath(cur) == os.path.abspath(root))
        hf, sd, ot = build_index(cur, is_root=is_root); made_idx += 1
        if build_readme(cur, hf, ot, is_root=is_root): made_rd += 1
    print(f"Done. Wrote {made_idx} index.html file(s); created {made_rd} new README.md file(s).")
    print("Existing README.md files were left untouched. Re-run any time you add demos.")

if __name__ == "__main__":
    main()
