#!/usr/bin/env python3
"""Generate index.html from canvas.json: the front door cannot drift from the artboards.

    python3 build-index.py
"""
import io, json, os, html

HERE = os.path.dirname(os.path.abspath(__file__))
c = json.load(io.open(os.path.join(HERE, "canvas.json"), encoding="utf-8"))
boards = sorted(c["artboards"], key=lambda b: (b["y"], b["x"]))
rows = "".join(
    '<li><a href="%s?w=%d">%s</a><span class="m">%d px wide</span></li>' % (b["file"], b["w"], html.escape(b["title"]), b["w"])
    for b in boards)
page = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark">
<meta name="googlebot" content="noindex,nofollow">
<meta name="bingbot" content="noindex,nofollow">
<meta name="slurp" content="noindex,nofollow">
<meta name="yandex" content="noindex,nofollow">
<title>HeartBank&#174; Treasury: landing drawings</title>
<meta property="og:type" content="website">
<meta property="og:url" content="https://demo.heartbank.org/">
<meta property="og:site_name" content="HeartBank Treasury">
<meta property="og:title" content="HeartBank&#174; Treasury: landing drawings">
<meta property="og:description" content="The new heartbank.org, drawn in English and Khmer, light and dark. These are drawings. They charge nobody.">
<meta property="og:image" content="https://demo.heartbank.org/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="HeartBank Treasury on a dark ground with the B-Emblem standing in for the B.">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#9a6f0b">
<style>[hidden]{display:none!important}
:root{--bg:#fff;--fg:#16141c;--dim:#5b5766;--line:rgba(20,16,30,.14);--acc:#9a6f0b}
@media (prefers-color-scheme:dark){:root{--bg:#0a0a0f;--fg:#f4f2f8;--dim:#b4b0c0;--line:rgba(255,255,255,.16);--acc:#f0b429}}
body{margin:0;padding:2.5rem 16px 4rem;background:var(--bg);color:var(--fg);font:1rem/1.6 system-ui,sans-serif}
main{max-width:36rem;margin:0 auto}
h1{font-size:1.9rem;line-height:1.2;margin:0 0 .5rem}
p{color:var(--dim)}
.start{display:block;border:1px solid var(--acc);border-radius:1rem;padding:1rem 1.2rem;margin:1.5rem 0;color:var(--fg);text-decoration:none}
.start b{color:var(--acc)}
ul{list-style:none;margin:0;padding:0}
li{display:flex;justify-content:space-between;gap:1rem;padding:.8rem 0;border-top:1px solid var(--line)}
li a{color:var(--fg)} .m{color:var(--dim);font-size:.85rem;white-space:nowrap}
small{display:block;margin-top:2rem;color:var(--dim)}</style>
</head>
<body>
<main>
<h1>HeartBank&#174; Treasury: landing drawings</h1>
<p>The screens for the new heartbank.org: English and Khmer, light and a dark pass, and the storyboard for its one motion explainer.</p>
<a class="start" href="wall.html"><b>Start here</b><br>Every screen on one wall. Drag to pan, pinch to zoom, tap a screen to open it.</a>
<ul>%s</ul>
<small>These are drawings. They charge nobody, and nothing here is live. The Khmer is our own placeholder until a native reader approves it. Hidden from search by named crawler; shareable by link.</small>
</main>
</body>
</html>
""" % rows
io.open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
print("index.html written: %d artboards" % len(boards))
