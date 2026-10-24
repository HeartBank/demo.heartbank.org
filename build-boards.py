#!/usr/bin/env python3
"""Generate the heartbank.org landing artboards, canvas.json and the board stylesheet.

One source for both languages and both themes, so the artboards cannot drift from each other.
Khmer below is OURS and marked as a placeholder on every board until a native reader approves it.

    python3 build-boards.py && python3 build-index.py && python3 build-wall.py
"""
import io, json, os

HERE = os.path.dirname(os.path.abspath(__file__))

EMBLEM = ("M3.9743 20.0257L3.8824 18.0670C3.5430 11.1232 3.3167 6.5411 5.9896 3.8683C8.1675 "
          "1.6904 11.5899 1.6904 13.7678 3.8683C14.9981 5.0986 15.6062 6.8523 15.4719 8.5281C17.1477 "
          "8.3938 18.9014 9.0019 20.1317 10.2322C22.3096 12.4101 22.3096 15.8325 20.1317 18.0104C17.4589 "
          "20.6833 12.8768 20.4570 5.9260 20.1247L3.9743 20.0257Z")

APP = "thank.heartbank.org"

T = {
    "en": {
        "lang": "en", "tag": "English",
        "h1": "Say thank you with money. Keep the thanks.",
        "sub": "HeartBank Treasury keeps a record of the thank-yous in your family, on top of the accounts you already use.",
        "cta": "Open the app",
        "share": "Share",
        "cta_note": "You will land at " + APP,
        "how_h": "How a thank-you travels",
        "how_poster": "Motion explainer: give, thank, give forward",
        "steps": ["Someone gives", "The thanks is written down", "It can be passed on"],
        "ben_h": "What it does",
        "ben": ["Every thank-you is written down where your family can see it.",
                "Money moves between your own accounts. HeartBank never holds it.",
                "Thanks can be passed on: what you receive, you can give forward."],
        "why_h": "Why start a Family Kitty\u2120",
        "why": [("Everyday help gets noticed", "A thank-you for the cooking, the caring and the tidying-up can come with a small amount of real money."),
                ("One shared place", "The whole family can see thanks going in and coming out."),
                ("Children learn to pass it on", "When a child is thanked, half is theirs to keep and half is set aside to give forward."),
                ("You stay in charge", "A parent or guardian opens it, invites the family and decides who joins.")],
        "things_h": "Three things in the app",
        "things": [("Family Kitty℠", "One shared place for a family's thank-yous and gifts."),
                   ("Personal Account℠", "Your own place to give and to receive."),
                   ("Re-Thank Foundation℠", "Where a child learns to pass thanks on. Yours to give, never yours to keep.")],
        "is_h": "What it is, and what it is not",
        "is_p": "HeartBank keeps the record. Your own bank accounts and the KHQR code move the money. This page takes no payments.",
        "is_link": "Read the essay: The Gift of Gratitude",
        "is_link_note": "thonly.org/research/the-gift-of-gratitude",
        "else_h": "Elsewhere",
        "else": [("Time", "Chronicle, for the hours we give each other", "heartbank.com"),
                 ("Papers", "The institution's published positions", "heartbank.net"),
                 ("Shops", "Local shops that take thanks", "heartbank.ceo")],
        "who": "Founded by Thon Ly. Miss Aquarius℠ is the CEO.",
        "disc": ("HeartBank® is a data bank of gratitude. It is not a chartered bank or financial institution; it does not "
                 "provide banking services, hold deposits, or extend credit. This page takes no payments. In the app, money "
                 "moves by KHQR straight between people's own bank accounts, and HeartBank never holds it. HeartBank's role is "
                 "to keep the record of thanks; financial services are not provided by HeartBank."),
        "ph": "",
        "sb_h": "Explainer storyboard",
        "sb_cap": ["Two people. One gives.", "The thanks is written in a shared record.", "The receiver passes it on to a third person.", "The ring closes. Thanks keep moving."],
        "sb_note": "Static equivalent under reduced motion: frame 4. The people are drawn figures, never real ones. No clock, counter or water appears in any frame.",
    },
    "km": {
        "lang": "km", "tag": "ខ្មែរ",
        "h1": "និយាយអរគុណដោយប្រាក់ ហើយរក្សាទុកការអរគុណ",
        "sub": "HeartBank Treasury រក្សាកំណត់ត្រានៃការអរគុណក្នុងគ្រួសាររបស់អ្នក នៅលើគណនីដែលអ្នកប្រើរួចហើយ។",
        "cta": "បើកកម្មវិធី",
        "cta_note": "អ្នកនឹងទៅដល់ " + APP,
        "how_h": "របៀបដែលការអរគុណធ្វើដំណើរ",
        "how_poster": "វីដេអូរាយាប់អធិប្បាយ៖ ឡើង អរគុណ ឡើងបន្ត",
        "steps": ["ម្នាក់ឡើង", "ការអរគុណត្រូវបានកត់ទុក", "អាចឡើងបន្តបាន"],
        "ben_h": "វាធ្វើអ្វីបានខ្លះ",
        "ben": ["រាល់ការអរគុណត្រូវបានកត់ទុកនៅកន្លែងដែលគ្រួសារអ្នកអាចមើលឃើញ។",
                "ប្រាក់ផ្លាស់ទីរវាងគណនីផ្ទាល់ខ្លួនរបស់អ្នក។ HeartBank មិនកាន់កាប់ប្រាក់ឡើយ។",
                "ការអរគុណអាចឡើងបន្តបាន៖ អ្វីដែលអ្នកទទួលបាន អ្នកអាចឡើងបន្តទៀត។"],
        "things_h": "របស់បានាក្នុងកម្មវិធី",
        "things": [("Family Kitty℠", "កន្លែងរួមមួយស្រាប់ការអរគុណ និងអំណោយរបស់គ្រួសារ។"),
                   ("Personal Account℠", "កន្លែងផ្ទាល់ខ្លួនរបស់អ្នកស្រាប់ផ្តល់ និងទទួល។"),
                   ("Re-Thank Foundation℠", "កន្លែងដែលកុមាររៀនឡើងការអរគុណបន្ត៖ ជារបស់អ្នកស្រាប់ឡើង មិនមែនស្រាប់រក្សាទុកទេ។")],
        "is_h": "វាជាអ្វី និងមិនមែនជាអ្វី",
        "is_p": "HeartBank រក្សាកំណត់ត្រា។ គណនីធនាគាររបស់អ្នក និងកូដ KHQR ជាអ្នកផ្លាស់ប្ដូរប្រាក់។ ទំព័រនេះមិនទទួលការបង់ប្រាក់ទេ។",
        "is_link": "អានឯកសារស្រាវជ្រាវ",
        "is_link_note": "[ តំណភ្ជាប់ឯកសារមួយ មិនមែនបញ្ជីស្រាវជ្រាវ ]",
        "else_h": "ផ្សេងទៀត",
        "else": [("ពេលវេលា", "Chronicle ស្រាប់ម៉ោងដែលយើងផ្តល់ដល់គ្នា", "heartbank.com"),
                 ("ឯកសារ", "មតិដែលស្ថាប័នបានផ្សាយ", "heartbank.net"),
                 ("ហាង", "ហាងទំនិញដែលទទួលការអរគុណ", "heartbank.ceo")],
        "who": "បង្កើតដោយ Thon Ly។ Miss Aquarius℠ ជានាយកប្រតិបត្តិ។",
        "disc": ("HeartBank® ជាឃ្លាំងទិន្នន័យនៃការដឹងគុណ។ "
                 "វាមិនមែនជាធនាគារមានអាជ្ញាប័ណ្ណ ឬស្ថាប័នហិរញ្ញវត្ថុទេ ហើយមិនផ្តល់សេវាធនាគារ "
                 "មិនទទួលរក្សាប្រាក់បញ្ចើ ឬផ្តល់ឥណទានឡើយ។ ទំព័រនេះមិនទទួលការបង់ប្រាក់ទេ។ "
                 "ក្នុងកម្មវិធី ប្រាក់ផ្លាស់ទីតាម KHQR ដោយផ្ទាល់រវាងគណនីធនាគាររបស់មនុស្សម្នាក់ៗ "
                 "ហើយ HeartBank មិនកាន់កាប់ប្រាក់ឡើយ។ តួនាទីរបស់ HeartBank គឺរក្សាកំណត់ត្រានៃការអរគុណ។"),
        "ph": "ខ្មែរនេះជាពាក្យរង់ចាំ មុននឹងមានការអនុម័ត",
        "sb_h": "រូបភាពរៀបរៀងវីដេអូ",
        "sb_cap": ["ផ្ទះពីរ។ មួយឡើង។", "ការអរគុណត្រូវបានសរសេរក្នុងកំណត់ត្រារួម។", "អ្នកទទួលឡើងបន្តទៅផ្ទះទីបាំ។", "វង់បិទ។ ការអរគុណបន្តស្ថិត។"],
        "sb_note": "រូបភាពស្ថិតក្នុងរង់ចាំ គឺក្រឡោបាន។",
    },
}
# The Khmer above was first composed as \u escapes and came out partly garbled (e.g. ឡើង "go up" for "give").
# This block REPLACES it with Khmer written directly. It is still OURS and UNREVIEWED: every Khmer board says so.
T["km"].update({
    "share": "ចែករំលែក",
    "how_poster": "វីដេអូពន្យល់៖ ឲ្យ អរគុណ ឲ្យបន្ត",
    "steps": ["ម្នាក់ឲ្យ", "ការអរគុណត្រូវបានកត់ទុក", "អាចឲ្យបន្តបាន"],
    "ben_h": "វាធ្វើអ្វីខ្លះ",
    "ben": ["រាល់ការអរគុណត្រូវបានកត់ទុកនៅកន្លែងដែលគ្រួសារអ្នកអាចមើលឃើញ។",
            "ប្រាក់ផ្លាស់ទីរវាងគណនីផ្ទាល់ខ្លួនរបស់អ្នក។ HeartBank មិនកាន់កាប់ប្រាក់ឡើយ។",
            "ការអរគុណអាចឲ្យបន្តបាន៖ អ្វីដែលអ្នកទទួលបាន អ្នកអាចឲ្យបន្តទៀត។"],
    "why_h": "ហេតុអ្វីបានជាចាប់ផ្តើម Family Kitty℠",
    "why": [("ជំនួយប្រចាំថ្ងៃត្រូវបានកត់សម្គាល់", "ការអរគុណសម្រាប់ការចម្អិនអាហារ ការថែទាំ និងការរៀបចំសម្អាត អាចភ្ជាប់ជាមួយប្រាក់ពិតបន្តិចបន្តួច។"),
            ("កន្លែងរួមមួយ", "ក្រុមគ្រួសារទាំងមូលអាចមើលឃើញការអរគុណចូល និងចេញ។"),
            ("កុមាររៀនឲ្យបន្ត", "ពេលកុមារម្នាក់ត្រូវបានអរគុណ ពាក់កណ្តាលជារបស់កុមារ ហើយពាក់កណ្តាលទៀតត្រូវទុកសម្រាប់ឲ្យបន្ត។"),
            ("អ្នកជាអ្នកគ្រប់គ្រង", "ឪពុកម្តាយ ឬអាណាព្យាបាលបើកវា អញ្ជើញគ្រួសារ និងសម្រេចថាអ្នកណាចូលរួម។")],
    "things_h": "បីយ៉ាងក្នុងកម្មវិធី",
    "things": [("Family Kitty℠", "កន្លែងរួមមួយសម្រាប់ការអរគុណ និងអំណោយរបស់គ្រួសារ។"),
               ("Personal Account℠", "កន្លែងផ្ទាល់ខ្លួនរបស់អ្នកសម្រាប់ឲ្យ និងទទួល។"),
               ("Re-Thank Foundation℠", "កន្លែងដែលកុមាររៀនឲ្យការអរគុណបន្ត។ ជារបស់អ្នកសម្រាប់ឲ្យ មិនមែនសម្រាប់រក្សាទុកទេ។")],
    "is_p": "HeartBank រក្សាកំណត់ត្រា។ គណនីធនាគាររបស់អ្នក និងកូដ KHQR ជាអ្នកផ្លាស់ទីប្រាក់។ ទំព័រនេះមិនទទួលការបង់ប្រាក់ទេ។",
    "is_link_note": "thonly.org/research/the-gift-of-gratitude",
    "else": [("ពេលវេលា", "Chronicle សម្រាប់ម៉ោងដែលយើងឲ្យគ្នាទៅវិញទៅមក", "heartbank.com"),
             ("ឯកសារ", "ជំហរដែលស្ថាប័នបានផ្សាយ", "heartbank.net"),
             ("ហាង", "ហាងក្នុងតំបន់ដែលទទួលការអរគុណ", "heartbank.ceo")],
    "who": "ស្ថាបនិកគឺ Thon Ly។ Miss Aquarius℠ ជាប្រធានប្រតិបត្តិ។",
    "disc": ("HeartBank® ជាឃ្លាំងទិន្នន័យនៃការដឹងគុណ។ វាមិនមែនជាធនាគារមានអាជ្ញាប័ណ្ណ ឬស្ថាប័នហិរញ្ញវត្ថុទេ ហើយមិនផ្តល់សេវាធនាគារ "
             "មិនទទួលរក្សាប្រាក់បញ្ញើ ឬផ្តល់ឥណទានឡើយ។ ទំព័រនេះមិនទទួលការបង់ប្រាក់ទេ។ ក្នុងកម្មវិធី ប្រាក់ផ្លាស់ទីតាម KHQR "
             "ដោយផ្ទាល់រវាងគណនីធនាគាររបស់មនុស្សម្នាក់ៗ ហើយ HeartBank មិនកាន់កាប់ប្រាក់ឡើយ។ "
             "តួនាទីរបស់ HeartBank គឺរក្សាកំណត់ត្រានៃការអរគុណ។"),
    "ph": "ភាសាខ្មែរនេះជាសេចក្តីព្រាងរបស់យើង រង់ចាំការពិនិត្យពីអ្នកភាសាខ្មែរ",
    "sb_h": "ផ្ទាំងរូបរឿងនៃវីដេអូពន្យល់",
    "sb_cap": ["មនុស្សពីរនាក់។ ម្នាក់ឲ្យ។", "ការអរគុណត្រូវបានសរសេរក្នុងកំណត់ត្រារួម។",
               "អ្នកទទួលឲ្យបន្តទៅមនុស្សទីបី។", "រង្វង់បិទ។ ការអរគុណបន្តធ្វើដំណើរ។"],
    "sb_note": "ប្រសិនបើបិទចលនា បង្ហាញរូបទី ៤។ មនុស្សជារូបគំនូរ មិនមែនមនុស្សពិតទេ។ គ្មាននាឡិកា ឧបករណ៍រាប់ ឬទឹកក្នុងរូបណាមួយឡើយ។",
})

CSS = """
:root{
  --bg:#ffffff; --surface:#faf5e6; --surface-2:#f3ead0; --line:rgba(20,16,30,.12); --line-strong:rgba(20,16,30,.28);
  --ink:#16141c; --ink-dim:#5b5766; --accent:#9a6f0b; --accent-ink:#ffffff; --wash:rgba(154,111,11,.10); --edge:rgba(154,111,11,.28);
  --font-display:"Newsreader",Georgia,serif; --font-text:"IBM Plex Sans",ui-sans-serif,system-ui,sans-serif;
  --font-mono:"IBM Plex Mono",ui-monospace,Menlo,monospace; --font-khmer:"Noto Sans Khmer",sans-serif;
  --r-card:1.25rem; --r-control:1rem; --r-pill:999px;
}
[data-theme="dark"]{
  --bg:#0a0a0f; --surface:#17171d; --surface-2:#22222a; --line:rgba(255,255,255,.14); --line-strong:rgba(255,255,255,.32);
  --ink:#f4f2f8; --ink-dim:#b4b0c0; --accent:#f0b429; --accent-ink:#16141c; --wash:rgba(240,180,41,.10); --edge:rgba(240,180,41,.32);
}
*{box-sizing:border-box}
html,body{margin:0}
body{background:var(--bg);color:var(--ink);font-family:var(--font-text);font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
.km{font-family:var(--font-khmer),var(--font-text);line-height:1.7}
.board{width:var(--w);margin:0 auto;padding:0 var(--pad);background:var(--bg)}
.desk{--w:1440px;--pad:96px} .phone{--w:390px;--pad:20px}
header{display:flex;align-items:center;justify-content:space-between;padding:26px 0;gap:12px}
.wordmark{font-family:var(--font-display);font-weight:600;font-size:1.5rem;white-space:nowrap;letter-spacing:-.01em;
  --emblem-cap:.66em;--emblem-size:calc(var(--emblem-cap)*1.1);--emblem-box:calc(var(--emblem-size)/.7534)}
.wordmark svg{width:var(--emblem-box);height:var(--emblem-box);color:var(--accent);vertical-align:baseline;
  margin-top:calc(var(--emblem-box)*-.09312);margin-bottom:calc(var(--emblem-box)*-.15333);
  margin-left:calc(var(--emblem-box)*-.15343 + 1px);margin-right:calc(var(--emblem-box)*-.09312 - 1px)}
.wordmark sup{font-size:.4em;font-weight:500;vertical-align:.9em;margin-left:.04em}
.tools{display:flex;gap:8px;align-items:center}
.seg{display:inline-flex;border:1px solid var(--line-strong);border-radius:var(--r-pill);padding:3px;font-size:.8rem}
.seg span{padding:5px 12px;border-radius:var(--r-pill);color:var(--ink-dim)}
.seg span.on{background:var(--ink);color:var(--bg)}
h1{font-family:var(--font-display);font-weight:600;letter-spacing:-.022em;line-height:1.05;margin:0}
.desk h1{font-size:4.2rem;max-width:15ch} .phone h1{font-size:2.5rem}
.km h1,h1.km{letter-spacing:0;line-height:1.35} .desk h1.km{font-size:3.3rem;max-width:18ch} .phone h1.km{font-size:2rem}
h2{font-family:var(--font-display);font-weight:600;font-size:1.9rem;letter-spacing:-.01em;margin:0 0 20px}
h2.km{font-size:1.7rem;letter-spacing:0}
.lede{color:var(--ink-dim);font-size:1.2rem;max-width:44ch;margin:22px 0 0}
.phone .lede{font-size:1.05rem}
.btn{display:inline-block;background:var(--accent);color:var(--accent-ink);border-radius:var(--r-control);padding:15px 28px;font-weight:600;font-size:1.05rem}
.note{color:var(--ink-dim);font-family:var(--font-mono);font-size:.8rem;margin:12px 0 0}
section{padding:56px 0;border-top:1px solid var(--line)}
.hero{padding:40px 0 64px;border:0}
.desk .hero{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:center}
.hero .art{border:1px solid var(--edge);background:var(--wash);border-radius:var(--r-card);padding:24px}
.poster{border:1px solid var(--line);background:var(--surface);border-radius:var(--r-card);padding:28px;display:flex;flex-direction:column;gap:20px}
.poster svg{width:100%;height:auto;display:block}
.steps{display:grid;gap:14px}.desk .steps{grid-template-columns:repeat(3,1fr)}
.step{font-size:1.05rem;color:var(--ink-dim);border:1px solid var(--line);border-radius:var(--r-card);background:var(--surface);padding:18px 18px 22px}
.step svg{width:100%;height:auto;display:block;margin-bottom:10px}
.step b{display:block;color:var(--accent);font-family:var(--font-display);font-weight:600;font-size:3rem;line-height:1;margin-bottom:6px}
.foot-row{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin:0 0 22px}
.foot-row p{margin:0}
.cols{display:grid;gap:16px}.desk .cols{grid-template-columns:repeat(3,1fr);gap:24px}.desk .cols4{grid-template-columns:repeat(4,1fr);gap:20px}
.share{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--line-strong);border-radius:var(--r-pill);padding:6px 13px;font-size:.85rem;color:var(--ink)}
.share svg{width:16px;height:16px;flex:none}
.phone .share{padding:7px 9px}.phone .share .lbl{display:none}
.card{border:1px solid var(--line);border-radius:var(--r-card);padding:22px;background:var(--surface)}
.card h3{font-family:var(--font-display);font-size:1.3rem;margin:0 0 6px;font-weight:600}
.card p{margin:0;color:var(--ink-dim)}
.ben{display:grid;gap:14px;margin:0;padding:0;list-style:none}
.ben li{padding:18px 20px;border-left:3px solid var(--accent);background:var(--wash);border-radius:0 var(--r-control) var(--r-control) 0;font-size:1.1rem}
.mono{font-family:var(--font-mono)}
.tag{display:inline-block;font-family:var(--font-mono);font-size:.72rem;letter-spacing:.06em;text-transform:uppercase;border:1px dashed var(--line-strong);border-radius:var(--r-pill);padding:3px 10px;color:var(--ink-dim)}
a.link{color:var(--accent);text-decoration:underline;text-underline-offset:3px}
footer{border-top:1px solid var(--line);padding:36px 0 56px;color:var(--ink-dim);font-size:.9rem}
footer p{max-width:70ch;margin:0 0 14px}
.sb{display:grid;gap:20px}.desk .sb{grid-template-columns:repeat(2,1fr)}
.sb figure{margin:0;border:1px solid var(--line);border-radius:var(--r-card);padding:16px;background:var(--surface)}
.sb figcaption{margin-top:10px;color:var(--ink-dim);font-size:.95rem}
"""


def mark(lang="en"):
    return ('Heart<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="%s"/></svg>ank<sup>®</sup>' % EMBLEM)


def person(cx, cy, top, skin, hair, piece, s=1.0):
    """A DRAWN figure (art, never a real or identifiable person): ground circle, shoulders, head, hair, one piece."""
    g = ['<g transform="translate(%s %s) scale(%s)">' % (cx, cy, s),
         '<circle cx="0" cy="0" r="34" fill="var(--surface-2)" stroke="var(--line)" stroke-width="1.5"/>',
         '<path d="M-23 30 C-23 10 -13 4 0 4 C13 4 23 10 23 30 A34 34 0 0 1 -23 30 Z" fill="%s"/>' % top,
         '<circle cx="0" cy="-8" r="13" fill="%s"/>' % skin]
    if piece == "bun":
        g += ['<path d="M-13 -9 C-13 -24 13 -24 13 -9 C8 -16 -8 -16 -13 -9 Z" fill="%s"/>' % hair, '<circle cx="0" cy="-26" r="6" fill="%s"/>' % hair]
    elif piece == "grey":
        g += ['<path d="M-13 -7 C-14 -24 14 -24 13 -7 C9 -15 -9 -15 -13 -7 Z" fill="%s"/>' % hair]
    else:  # pigtails
        g += ['<path d="M-13 -8 C-13 -23 13 -23 13 -8 C8 -15 -8 -15 -13 -8 Z" fill="%s"/>' % hair,
              '<circle cx="-16" cy="-6" r="5" fill="%s"/>' % hair, '<circle cx="16" cy="-6" r="5" fill="%s"/>' % hair]
    g.append('</g>')
    return "".join(g)


def parent(cx, cy):  return person(cx, cy, "#c0603f", "#d9a47a", "#2a1d17", "bun")
def elder(cx, cy):   return person(cx, cy, "#4f7a62", "#b98a63", "#c9c4c0", "grey")
def child(cx, cy):   return person(cx, cy, "var(--accent)", "#e0b48a", "#2a1d17", "pigtails", .9)


def flow_svg(frame, w=520, h=230):
    """frame 1-4 of the explainer; literal attributes only, never dependent on animation.
    A (90,170) gives to C (430,170); C passes on to B (260,60); B closes the ring back to A."""
    a, b, c = (90, 172), (260, 44), (430, 172)
    arrow = ('<path d="%s" fill="none" stroke="var(--accent)" stroke-width="3" stroke-linecap="round" marker-end="url(#ar%d)"/>')
    parts = ['<svg viewBox="0 0 %d %d" role="img" aria-hidden="true">' % (w, h)]
    parts.append('<defs><marker id="ar%d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="var(--accent)"/></marker></defs>' % frame)
    parts.append(parent(*a)); parts.append(child(*c))
    if frame >= 3:
        parts.append(elder(*b))
    parts.append(arrow % ("M128 158 C190 128 330 128 392 158", frame))
    if frame >= 2:
        parts.append('<g transform="translate(260 204)"><rect x="-46" y="-17" width="92" height="34" rx="8" fill="var(--bg)" stroke="var(--accent)" stroke-width="2"/>'
                     '<line x1="-30" y1="-4" x2="30" y2="-4" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/><line x1="-30" y1="7" x2="12" y2="7" stroke="var(--line-strong)" stroke-width="3" stroke-linecap="round"/></g>')
    if frame >= 3:
        parts.append(arrow % ("M412 142 C384 112 346 84 308 62", frame))
    if frame == 4:
        parts.append(arrow % ("M212 62 C174 84 136 112 108 142", frame))
    parts.append('</svg>')
    return "".join(parts)


def page(lang, theme, size, kind="landing"):
    t = T[lang]
    kmc = " km" if lang == "km" else ""
    cls = "desk" if size == "desk" else "phone"
    seg_l = '<div class="seg"><span%s>EN</span><span%s class="km">ខ្មែរ</span></div>' % (' class="on"' if lang == "en" else "", ' class="on"' if lang == "km" else "")
    tl = ("Auto", "Light", "Dark") if lang == "en" else ("ស្វ័យប្រវត្តិ", "ភ្លឺ", "ងងឹត")
    seg_t = '<div class="seg%s"><span>%s</span><span%s>%s</span><span%s>%s</span></div>' % (kmc, tl[0], ' class="on"' if theme == "light" else "", tl[1], ' class="on"' if theme == "dark" else "", tl[2])
    ph = ('<p class="note km">[ %s ]</p>' % t["ph"]) if t["ph"] else ""
    share = ('<span class="share"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12M12 3l-4 4M12 3l4 4M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-7" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'
             '<span class="lbl%s">%s</span></span>' % (kmc, t["share"]))
    head = ('<header><div class="wordmark">%s</div><div class="tools">%s%s</div></header>' % (mark(), seg_l, share))
    if kind == "storyboard":
        body = ('%s<section class="hero" style="padding-bottom:24px"><h1 class="%s">%s</h1>%s</section><div class="sb">%s</div><p class="note">%s</p>'
                % (head, kmc.strip(), t["sb_h"], ph,
                   "".join('<figure>%s<figcaption><b class="mono">%d</b> · <span class="%s">%s</span></figcaption></figure>' % (flow_svg(i + 1), i + 1, kmc.strip(), t["sb_cap"][i]) for i in range(4)),
                   t["sb_note"]))
    else:
        hero_art = '<div class="art"><div class="poster">%s<p class="note%s" style="margin:0">[ %s ]</p></div></div>' % (flow_svg(4), kmc, t["how_poster"])
        steps = "".join('<div class="step%s">%s<b>%d</b>%s</div>' % (kmc, flow_svg(i + 1), i + 1, s) for i, s in enumerate(t["steps"]))
        ben = "".join('<li class="%s">%s</li>' % (kmc.strip(), b) for b in t["ben"])
        why = "".join('<div class="card"><h3 class="%s">%s</h3><p class="%s">%s</p></div>' % (kmc.strip(), n, kmc.strip(), d) for n, d in t["why"])
        things = "".join('<div class="card"><h3>%s</h3><p class="%s">%s</p></div>' % (n, kmc.strip(), d) for n, d in t["things"])
        elsewhere = "".join('<div class="card"><h3 class="%s">%s</h3><p class="%s">%s</p><p class="note">%s</p></div>' % (kmc.strip(), n, kmc.strip(), d, h) for n, d, h in t["else"])
        body = ('%s<section class="hero"><div><h1 class="%s">%s</h1><p class="lede%s">%s</p><p style="margin:32px 0 0"><span class="btn%s">%s</span></p><p class="note%s">%s</p>%s</div>%s</section>'
                '<section><h2 class="%s">%s</h2><div class="steps">%s</div></section>'
                '<section><h2 class="%s">%s</h2><div class="cols cols4">%s</div></section>'
                '<section><h2 class="%s">%s</h2><ul class="ben">%s</ul></section>'
                '<section><h2 class="%s">%s</h2><div class="cols">%s</div></section>'
                '<section><h2 class="%s">%s</h2><p class="lede%s" style="margin-top:0">%s</p><p style="margin:18px 0 0"><span class="link a">%s</span> <span class="note" style="margin-left:8px">%s</span></p></section>'
                '<section><h2 class="%s">%s</h2><div class="cols">%s</div></section>'
                '<footer><div class="foot-row"><p class="lede%s">%s</p>%s</div><p class="%s">%s</p><p class="note">%s</p></footer>'
                % (head, kmc.strip(), t["h1"], kmc, t["sub"], kmc, t["cta"], kmc, t["cta_note"], ph, hero_art,
                   kmc.strip(), t["how_h"], steps,
                   kmc.strip(), t["why_h"], why,
                   kmc.strip(), t["ben_h"], ben,
                   kmc.strip(), t["things_h"], things,
                   kmc.strip(), t["is_h"], kmc, t["is_p"], t["is_link"], t["is_link_note"],
                   kmc.strip(), t["else_h"], elsewhere,
                   kmc, t["who"], seg_t,
                   kmc.strip(), t["disc"],
                   ("[ Khmer is our own placeholder until a native reader approves it ]" if lang == "km" else "[ Drawing. This page takes no payments. ]")))
    width = 1440 if size == "desk" else 390
    return ('<!doctype html>\n<html lang="%s" data-theme="%s">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=%d">\n'
            '<meta name="googlebot" content="noindex,nofollow"><meta name="bingbot" content="noindex,nofollow">\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&family=Noto+Sans+Khmer:wght@400;500;600&display=swap">\n'
            '<link rel="stylesheet" href="board.css">\n<style>[hidden]{display:none!important}</style>\n<title>%s</title>\n</head>\n<body>\n<div class="board %s">%s</div>\n</body>\n</html>\n'
            % (t["lang"], theme, width, "heartbank.org landing (%s, %s, %s)" % (lang, theme, size), cls, body))


BOARDS = [
    # file, lang, theme, size, kind, title
    ("LandingEnDesktop.html", "en", "light", "desk", "landing", "1 · Landing, English, desktop"),
    ("LandingEnPhone.html", "en", "light", "phone", "landing", "2 · Landing, English, phone"),
    ("LandingKmDesktop.html", "km", "light", "desk", "landing", "3 · Landing, Khmer, desktop"),
    ("LandingKmPhone.html", "km", "light", "phone", "landing", "4 · Landing, Khmer, phone"),
    ("LandingEnDark.html", "en", "dark", "desk", "landing", "5 · Dark pass, English, desktop"),
    ("LandingKmDarkPhone.html", "km", "dark", "phone", "landing", "6 · Dark pass, Khmer, phone"),
    ("ExplainerStoryboard.html", "en", "light", "desk", "storyboard", "7 · Explainer storyboard, English"),
    ("ExplainerStoryboardKm.html", "km", "light", "desk", "storyboard", "8 · Explainer storyboard, Khmer"),
]

HEIGHTS = {}
if os.path.exists(os.path.join(HERE, "heights.json")):
    HEIGHTS = json.load(open(os.path.join(HERE, "heights.json")))


def main():
    io.open(os.path.join(HERE, "board.css"), "w", encoding="utf-8").write(CSS.strip() + "\n")
    artboards, x, y = [], 0, 0
    for f, lang, theme, size, kind, title in BOARDS:
        io.open(os.path.join(HERE, f), "w", encoding="utf-8").write(page(lang, theme, size, kind))
        w = 1440 if size == "desk" else 390
        h = HEIGHTS.get(f, 2600 if size == "desk" else 4200)
        artboards.append({"file": f, "x": x, "y": 0, "w": w, "h": h, "title": title, "page": "page-1"})
        x += w + 120
    canvas = {"artboards": artboards, "annotations": [], "launch": {"view": "canvas", "page": "page-1"},
              "pages": [{"id": "page-1", "name": "heartbank.org"}]}
    io.open(os.path.join(HERE, "canvas.json"), "w", encoding="utf-8").write(json.dumps(canvas, indent=1, ensure_ascii=False) + "\n")
    print("wrote %d artboards" % len(artboards))


if __name__ == "__main__":
    main()
