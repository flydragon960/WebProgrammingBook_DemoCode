# Chapter 2 copyright audit — book (chapter2.tex) and repo (chap2/)

Checked: all 56 code listings and 24 figure references in `chapter2.tex`, and every file in `chap2/` of
WebProgrammingBook_DemoCode (commit 5ccb665). Not legal advice. The source matches below come from my
knowledge of W3Schools pages, Sebesta's *Programming the World Wide Web* examples and Wikipedia — please
confirm against those sources.

**Risk levels.** High = copied media or long copied text. Medium = recognisable copied example (sample
text, headings, sentences) or near-verbatim explanatory wording. Low = trivial or generic, optional to change.

## A. The book (chapter2.tex)

Most of the chapter is your own: hello world, paragraphs, headings, images (Old Port), links, lists,
tables, the basic form, buttons, div/span/section, and the AI-era section. Items to fix:

| # | Lines | What | Likely source | Risk | Fix |
|---|---|---|---|---|---|
| A1 | 1700–1705 | `<video width="320" height="240">`, `movie.mp4`, `movie.ogg`, "Your browser does not support the video tag." | W3Schools video example (verbatim) | Medium | Replace listing (below) |
| A2 | 1468–1480 | `<h2>The select Element</h2>`, "The select element defines a drop-down list:", `/action_page.php` | W3Schools select example (structure and sentences) | Medium | Replace listing |
| A3 | 1507–1513 | `<h2>Textarea</h2>`, "The textarea element defines a multi-line input field.", `rows="10" cols="30"`, `/action_page.php` | W3Schools textarea example | Medium | Replace listing |
| A4 | 1438–1450 | Checkbox example: W3Schools structure; values `"Car"`, `"Boat"` left over from its bike/car/boat sample; also bugs (id `op2` twice, `for="op3"` with no matching id) | W3Schools checkbox example (adapted) | Medium | Replace listing |
| A5 | 1407–1418 | Radio example with `<h2>Radio Buttons</h2>` and `/action_page.php` | W3Schools radio example (adapted; your own options) | Low | Change `action` to `submit.php` and the heading text |
| A6 | 1924–1929 | Viewport bullet wording ("sets the width of the page to follow the screen-width of the device", "sets the initial zoom level when the page is first loaded") | W3Schools viewport page (near-verbatim prose) | Medium | Reword (below) |
| A7 | 1360–1362 | GET "appends form-data into the URL in name/value pairs", POST "sends form-data as an HTTP post transaction" | W3Schools form `method` page (near-verbatim) | Medium | Reword (below) |
| A8 | 680–690 | `target` values: "Opens … in a new window or tab", "in the parent frame", "in the full body of the window" | W3Schools `target` table (near-verbatim) | Low–Medium | Reword (below) |
| A9 | 1937, 1952 | `content="Free Web tutorials on HTML, CSS, XML, and more."`, `content="John Doe"` | W3Schools meta examples | Low–Medium | Use your own values (below) |
| A10 | 2155–2172 | Attribute table: value `style_definition`, descriptions "Specifies a classname / a unique id / an inline style / extra information about an element", links to old w3schools `att_standard_*.asp` pages | Old W3Schools "Standard Attributes" table | Medium | Rewrite descriptions, link to MDN (below) |
| A11 | 168–177, 400–465 | Comment `<!-- greet.html A trivial document -->`, title "Our first document", "Greetings from your Webmaster!" | Sebesta's `greet.html` style example | Low | Optional. Changing the text also means retaking figures 2-2-1, 2.3.1 and 2.4 |
| A12 | figures | `figure2122.png` (video player) and `figure2121.png` (audio player): whatever frame or poster the player shows must be yours or licensed; `figure281/282.png` (Old Port photo) | Unknown | Check | Confirm you took or licensed the Old Port photo; if the video frame comes from a sample video (e.g. W3Schools' or a TV ad), retake it with your own clip |

Not a problem: the Gettysburg Address and "Mary Had a Little Lamb" are public domain; `<a href="https://www.example.com">`,
`Header 1/Data 1` tables, Coffee/Sugar/Tea and similar one-line snippets are generic.

### Replacement text for the book

**A1 video**
```html
<video width="640" height="360" controls>
  <source src="lecture.mp4" type="video/mp4">
  <source src="lecture.webm" type="video/webm">
  <track kind="captions" src="lecture.vtt" srclang="en" label="English">
  Your browser does not support the video element.
</video>
```

**A2 dropdown**
```html
<h2>Dropdown List</h2>
<form action="submit.php">
  <label for="lang">Choose a programming language:</label>
  <select id="lang" name="lang">
    <option value="js">JavaScript</option>
    <option value="java">Java</option>
    <option value="python">Python</option>
    <option value="csharp">C#</option>
  </select>
  <input type="submit" value="Submit">
</form>
```

**A3 textarea**
```html
<h2>Your Comment</h2>
<form action="submit.php" method="post">
  <label for="message">Tell us what you think of the course:</label><br>
  <textarea id="message" name="message" rows="6" cols="40"
            placeholder="Write your comment here"></textarea>
  <br><br>
  <input type="submit" value="Submit">
</form>
```

**A4 checkboxes** (also fixes the id/label/value bugs)
```html
<h2>Checkboxes</h2>
<p>What do you like to buy?</p>
<form action="submit.php">
  <input type="checkbox" id="op1" name="shopping" value="eggs">
  <label for="op1"> Eggs</label><br>
  <input type="checkbox" id="op2" name="shopping" value="milk">
  <label for="op2"> Milk</label><br>
  <input type="checkbox" id="op3" name="shopping" value="tomatoes">
  <label for="op3"> Tomatoes</label><br><br>
  <input type="submit" value="Submit">
</form>
```

**A6 viewport**
- `width=device-width` makes the page's layout width equal to the width of the device's screen, instead of a wide desktop width.
- `initial-scale=1.0` shows the page at 100% zoom when it first opens.

**A7 method**
- method: the HTTP method used to send the data. With GET, the browser adds the form data to the end of the URL as `name=value` pairs. With POST, it sends the data in the body of the HTTP request, so the data does not appear in the URL.

**A8 target**
- `_self` (default): opens the linked page in the current tab.
- `_blank`: opens it in a new tab or window.
- `_parent` and `_top`: only matter when the page is shown inside a frame (`<iframe>`); they open the link in the enclosing frame or in the whole browser window.

**A9 meta**
```html
<meta name="description" content="Example pages for Chapter 2 of SOEN 287 Web Programming.">
<meta name="author" content="Yuhong Yan">
```

**A10 attribute table** — value column: *class name(s)*, *unique name*, *CSS declarations*, *text*;
descriptions: "Assigns one or more class names, used by CSS selectors and JavaScript", "Gives the element a
name that is unique in the page; used by CSS, JavaScript and #fragment links", "Applies CSS declarations
directly to this element", "Extra information, usually shown as a tooltip". Link each name to
`https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/<name>`.

## B. The repository (chap2/)

| File(s) | Problem | Likely source | Risk | Action |
|---|---|---|---|---|
| NorskTippingKebab.mp4 / .ogv / .webm, testvideo.html | TV commercial video | Norsk Tipping (Norwegian lottery) | **High** | Delete; new `video.html` uses your own `media/lecture.*` |
| nineoneone.mp3 / .ogg / .wav | Audio clip of unknown origin | Probably textbook companion files | **High** | Delete; new `audio.html` uses `media/welcome.*` |
| table-twocolumn.html | Two long paragraphs about Colorado and South Dakota, no attribution | Wikipedia (CC BY-SA requires attribution) | **High** | Replaced with your own text |
| c210new.jpg, images/c210new.jpg | Cessna photo | Sebesta companion files | **High** | Delete |
| headings.html, image.html, image2.html, link.html, linkOnImage.html, C210data.html | Aidan's Airplanes / Cessna 210 examples | Sebesta | Medium | Replaced with book examples (Heading 1–6, Old Port, example.com); `C210data.html` → `old_port.html`; `image2.html` deleted |
| popcorn.html | Popcorn sales form | Sebesta | Medium | Delete (the book's basic form is `form.html`) |
| definition.html, unordered.html, nested_lists.html | Cessna models, aircraft lists | Sebesta | Medium | Replaced (HTML/CSS/JS; First/Second/Third item; course topics) |
| table.html, table_irr.html, cell_span.html | Fruit juice drinks tables; `#96D4D4` colour | Sebesta; W3Schools colour | Medium | Replaced with book tables; `table_irr.html` deleted |
| cell_align.html, space_pad.html | "The align and valign attributes / Column Label…", "Small spacing, large padding" | Sebesta | Medium | Replaced with your own versions |
| checkbox.html, menu.html, radio.html, textarea.html | Grocery checklist, grocery menu, age category, "employment aspirations" | Sebesta | Medium | Replaced with book examples; `menu.html` → `select.html` |
| organized.html | The Podunk Press, "Squeak Martin" | Sebesta | Medium | Replaced with the book's div/span/section examples; new `blog_divsoup.html` and `blog_semantic.html` |
| blockquote.html | Lincoln speech (public domain) inside Sebesta's surrounding sentences | Sebesta | Low–Medium | Replaced with your own framing |
| link_bookmark.html | "Jump to Chapter 4", "This chapter explains ba bla bla" | W3Schools bookmark example | Medium | Replaced (weekly schedule) |
| link_colors.html, my_style.html, nested_lists_2.html | "You can change the default colors of links"; "This is a heading" with powderblue/tomato/verdana/courier; Coffee/Tea/Black tea/Green tea | W3Schools examples (verbatim) | Medium | Replaced; `nested_lists_2.html` deleted |
| font_my.html | "My favorite color is blue red" del/ins sentences | W3Schools | Low–Medium | Replaced |
| audio.html | Uses the nineoneone files | — | — | Replaced |
| concordia.jpg (chap2, unused) and chap1/imgs/concordia.jpg (used by chap1/greet_img.html) | Professional campus photo | Probably Concordia University communications | **Check** | Delete from chap2; in chap1 replace with a photo you took, or get Concordia's permission |
| images/avatar.png (unused) | 3D cartoon avatar, saved as a Mac screenshot | Probably a stock illustration | **Check** | Delete (unused) |
| greet.html, index.html, p1.html, br.html, pre.html | Sebesta-style comments/titles; br.html links non-existent style.css/script.js; index.html duplicated greet.html | Sebesta (trivial) | Low | Replaced with clean versions; `index.html` is now a list of all examples |
| ordered.html, ordered_2.html, ordered_3.html, font_my_style.html, form_validation_Step1.html, test.html, tester.html | Your own | — | None | `ordered_2/3` merged into `ordered_attributes.html` and `ordered_style.html`; others kept (tester.html tidied) |
| .DS_Store (2 files) | macOS system files | — | — | Delete and add to .gitignore |
| (missing) images/old_port.jpg | Used by the book but not in the repo | — | — | Add your own photo |

## C. How to apply

1. Unzip `chap2_clean` somewhere outside the repository.
2. In your local clone (`git pull` first), from the repository root:
   `bash /path/to/chap2_clean/apply_chap2_cleanup.sh /path/to/chap2_clean`
   The script deletes 21 files, overwrites 29 and adds 17 (tested on a copy of commit 5ccb665), then stages everything.
3. Check with `git status` and open `chap2/index.html` in a browser.
4. Add `chap2/images/old_port.jpg` and your own media files, then
   `git commit -m "chap2: replace third-party examples with original ones"` and `git push`.

**Deleted files stay in the Git history** and can still be downloaded from old commits. For the high-risk media
(the commercial video and the audio), consider rewriting history after the commit above:

```bash
pip install git-filter-repo
git filter-repo --invert-paths \
  --path chap2/NorskTippingKebab.mp4 --path chap2/NorskTippingKebab.ogv --path chap2/NorskTippingKebab.webm \
  --path chap2/nineoneone.mp3 --path chap2/nineoneone.ogg --path chap2/nineoneone.wav \
  --path chap2/c210new.jpg --path chap2/images/c210new.jpg --path chap2/table-twocolumn.html
git remote add origin https://github.com/flydragon960/WebProgrammingBook_DemoCode.git   # filter-repo removes the remote
git push --force --all
```

This changes every commit ID: anyone who cloned the repo (e.g. students) must clone it again, and forks keep the old files.
Make a backup copy of the repository first. The same check is worth doing for chap3 (it also contains Sebesta images such as `c210new.jpg` and `c172.gif`).
