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
        "sub": "HeartBank® Treasury keeps a record of the thank-yous in your family, on top of the accounts you already use.",
        "cta": "Open B-Treasury App",
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
        "who1": "Founded by Thon Ly", "who2": "Miss Aquarius℠ is the CEO",
        "disc": ("HeartBank® is a data bank of gratitude. It is not a chartered bank or financial institution; it does not "
                 "provide banking services, hold deposits, or extend credit. This page takes no payments. In the app, money "
                 "moves by KHQR straight between people's own bank accounts, and HeartBank never holds it. HeartBank's role is "
                 "to keep the record of thanks; financial services are not provided by HeartBank."),
        "ph": "",
        "sb_h": "Explainer storyboard",
        "sb_cap": ["A parent thanks a child for tidying up, with a small coin and a thank-you.", "The thanks is written in a shared record.", "The child keeps half and passes half on to a grandparent.", "The thanks moves on to someone new. Thanks keep moving."],
        "sb_legend": "Heart: the thank-you. Coin: the money. Card: the shared record. The coin goes straight between people. Nothing in the middle holds it.",
        "sb_note": "Static equivalent under reduced motion: frame 4. No clock, counter or water appears in any frame.",
    },
    "km": {
        "lang": "km", "tag": "ខ្មែរ",
        "h1": "និយាយអរគុណដោយប្រាក់ ហើយរក្សាទុកការអរគុណ",
        "sub": "HeartBank® Treasury រក្សាកំណត់ត្រានៃការអរគុណក្នុងគ្រួសាររបស់អ្នក នៅលើគណនីដែលអ្នកប្រើរួចហើយ។",
        "cta": "បើកកម្មវិធី B-Treasury",
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
        "who1": "ស្ថាបនិកគឺ Thon Ly", "who2": "Miss Aquarius℠ ជាប្រធានប្រតិបត្តិ",
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
    "who1": "ស្ថាបនិកគឺ Thon Ly", "who2": "Miss Aquarius℠ ជាប្រធានប្រតិបត្តិ",
    "disc": ("HeartBank® ជាឃ្លាំងទិន្នន័យនៃការដឹងគុណ។ វាមិនមែនជាធនាគារមានអាជ្ញាប័ណ្ណ ឬស្ថាប័នហិរញ្ញវត្ថុទេ ហើយមិនផ្តល់សេវាធនាគារ "
             "មិនទទួលរក្សាប្រាក់បញ្ញើ ឬផ្តល់ឥណទានឡើយ។ ទំព័រនេះមិនទទួលការបង់ប្រាក់ទេ។ ក្នុងកម្មវិធី ប្រាក់ផ្លាស់ទីតាម KHQR "
             "ដោយផ្ទាល់រវាងគណនីធនាគាររបស់មនុស្សម្នាក់ៗ ហើយ HeartBank មិនកាន់កាប់ប្រាក់ឡើយ។ "
             "តួនាទីរបស់ HeartBank គឺរក្សាកំណត់ត្រានៃការអរគុណ។"),
    "ph": "ភាសាខ្មែរនេះជាសេចក្តីព្រាងរបស់យើង រង់ចាំការពិនិត្យពីអ្នកភាសាខ្មែរ",
    "sb_h": "ផ្ទាំងរូបរឿងនៃវីដេអូពន្យល់",
    "sb_legend": "បេះដូង៖ ពាក្យអរគុណ។ កាក់៖ ប្រាក់។ ប័ណ្ណ៖ កំណត់ត្រារួម។ កាក់ទៅដោយផ្ទាល់រវាងមនុស្ស គ្មានអ្វីនៅចន្លោះកាន់វាឡើយ។ មនុស្សជារូបគំនូរ មិនមែនមនុស្សពិតទេ។",
    "sb_cap": ["ឪពុកម្តាយអរគុណកូនដែលរៀបចំសម្អាត ដោយកាក់តូចមួយ និងពាក្យអរគុណ។", "ការអរគុណត្រូវបានសរសេរក្នុងកំណត់ត្រារួម។",
               "កុមារទុកពាក់កណ្តាល ហើយឲ្យពាក់កណ្តាលទៀតបន្តទៅជីដូនជីតា។", "ការអរគុណបន្តទៅមនុស្សថ្មី។ ការអរគុណបន្តធ្វើដំណើរ។"],
    "sb_note": "ប្រសិនបើបិទចលនា បង្ហាញរូបទី ៤។ មនុស្សជារូបគំនូរ មិនមែនមនុស្សពិតទេ។ គ្មាននាឡិកា ឧបករណ៍រាប់ ឬទឹកក្នុងរូបណាមួយឡើយ។",
})


T["en"].update({
    "states_h": "Other states",
    "st_login": "/login (still listed by Google)",
    "login_h": "Looking for the app?", "login_p": "Sign in at thank.heartbank.org.", "login_btn": "Open B-Treasury App",
    "st_nf": "Page not found",
    "nf_h": "That page is not here.", "nf_p": "Try the front page, or open the app.", "nf_home": "Go to the front page",
    "st_copied": "After Share, then Copy link",
    "copied": "Link copied",
})
T["km"].update({
    "states_h": "ស្ថានភាពផ្សេងទៀត",
    "st_login": "/login (Google នៅតែបង្ហាញ)",
    "login_h": "កំពុងរកកម្មវិធីមែនទេ?", "login_p": "ចូលនៅ thank.heartbank.org។", "login_btn": "បើកកម្មវិធី B-Treasury",
    "st_nf": "រកមិនឃើញទំព័រ",
    "nf_h": "មិនមានទំព័រនេះទេ។", "nf_p": "សូមសាកល្បងទំព័រដើម ឬបើកកម្មវិធី។", "nf_home": "ទៅទំព័រដើម",
    "st_copied": "បន្ទាប់ពីចែករំលែក រួចចម្លងតំណ",
    "copied": "បានចម្លងតំណ",
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
.wordmark sup{font-size:.72em;font-weight:500;vertical-align:-.27em;margin-left:.05em;line-height:0}
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
.intro{padding:40px 0 64px;border:0}
.desk .intro{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:center}
.intro .art{border:1px solid var(--edge);background:var(--wash);border-radius:var(--r-card);padding:24px}
.poster{border:1px solid var(--line);background:var(--surface);border-radius:var(--r-card);padding:28px;display:flex;flex-direction:column;gap:20px}
.poster svg{width:100%;height:auto;display:block}
.steps{display:grid;gap:14px}.desk .steps{grid-template-columns:repeat(3,1fr)}
.step{position:relative;font-size:1.05rem;color:var(--ink-dim);border:1px solid var(--line);border-radius:var(--r-card);background:var(--surface);padding:18px 18px 22px}
.step svg{width:100%;height:auto;display:block;margin-bottom:10px}
.step b{position:absolute;top:12px;left:18px;color:var(--accent);font-family:var(--font-display);font-weight:600;font-size:3rem;line-height:1}
.foot-row{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin:0 0 22px}
.foot-row p{margin:0}
.who{font-size:1rem}
.cols{display:grid;gap:16px}.desk .cols{grid-template-columns:repeat(3,1fr);gap:24px}.desk .cols4{grid-template-columns:repeat(4,1fr);gap:20px}
.nw{white-space:nowrap}
.sm{font-size:.45em;font-weight:500;vertical-align:.75em;margin-left:.05em;line-height:0}
.spot{width:100%;height:84px;display:block;margin:0 0 14px;background:var(--wash);border-radius:var(--r-control)}
.stl{font-family:var(--font-mono);font-size:.75rem;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-dim);margin:0 0 14px}
.btn2{display:inline-block;border:1px solid var(--line-strong);border-radius:var(--r-control);padding:14px 24px;font-weight:600}
.toast{display:inline-block;background:var(--ink);color:var(--bg);border-radius:var(--r-pill);padding:10px 20px;font-weight:500}
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
footer p{margin:0 0 14px}
.sb{display:grid;gap:20px}.desk .sb{grid-template-columns:repeat(2,1fr)}
.sb figure{margin:0;border:1px solid var(--line);border-radius:var(--r-card);padding:16px;background:var(--surface)}
.sb figcaption{margin-top:10px;color:var(--ink-dim);font-size:.95rem}
"""


def mark(lang="en", beating=False):
    return ('Heart<svg%s viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="%s"/></svg>ank<sup>®</sup>' % (' class="beating"' if beating else "", EMBLEM))


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
def friend(cx, cy):  return person(cx, cy, "#6b5b95", "#c99a6e", "#2a1d17", "bun", .95)
def elder(cx, cy):   return person(cx, cy, "#4f7a62", "#b98a63", "#c9c4c0", "grey")
def child(cx, cy):   return person(cx, cy, "var(--accent)", "#e0b48a", "#2a1d17", "pigtails", .9)


def _trav(x, y, half=False):
    """What travels on an arrow: a heart (the thank-you) and a coin (the money), or half a coin."""
    bg = '<circle cx="%s" cy="%s" r="15" fill="var(--surface)"/>'
    out = [bg % (x - 15, y), bg % (x + 15, y - 3)]
    if half:
        out.append('<path d="M%s %s A10 10 0 0 0 %s %s Z" fill="var(--accent)"/>' % (x - 15, y - 10, x - 15, y + 10))
    else:
        out.append(_coin(x - 15, y, 10))
    out.append(_heart(x + 15, y - 3, 1.5))
    return "".join(out)


def flow_svg(frame, w=520, h=230):
    """Frames 1-4 of the explainer; literal attributes only, never dependent on animation.
    A parent (90,172) gives to a child C (430,172); C keeps half and passes half on to an elder B (260,44);
    B passes it on to a new person D, so it never returns to A. Heart = the thank-you, coin = the money, card = the shared record.
    The coin travels STRAIGHT between people: nothing in the middle holds it."""
    a, b, c = (90, 172), (260, 44), (430, 172)
    def arrow(d, strong=True):
        return ('<path d="%s" fill="none" stroke="var(--accent)" stroke-width="3" stroke-linecap="round" opacity="%s" marker-end="url(#ar%d)"/>'
                % (d, "1" if strong else ".3", frame))
    parts = ['<svg viewBox="0 0 %d %d" role="img" aria-hidden="true">' % (w, h)]
    parts.append('<defs><marker id="ar%d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="var(--accent)"/></marker></defs>' % frame)
    parts.append(parent(*a)); parts.append(child(*c))
    if frame >= 3:
        parts.append(elder(*b))
    if frame == 4:
        parts.append(friend(480, 44))
    first = "M128 158 C190 128 330 128 392 158"
    second = "M412 142 C384 112 346 84 308 62"
    third = "M312 44 C346 30 380 30 408 44"
    parts.append(arrow(first, frame <= 2))
    if frame <= 2:
        parts.append(_trav(260, 136))
    if frame >= 2:
        parts.append('<g transform="translate(260 204)"><rect x="-46" y="-17" width="92" height="34" rx="8" fill="var(--bg)" stroke="var(--accent)" stroke-width="2"/>'
                     '<line x1="-32" y1="-4" x2="6" y2="-4" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>'
                     '<line x1="-32" y1="7" x2="-8" y2="7" stroke="var(--line-strong)" stroke-width="3" stroke-linecap="round"/>' + _heart(26, 1, .85) + '</g>')
    if frame >= 3:
        parts.append(arrow(second, frame == 3))
        if frame == 3:
            parts.append(_trav(364, 99, half=True))
            parts.append('<path d="M492 158 A11 11 0 0 1 492 180 Z" fill="var(--accent)"/>')  # the half the child keeps
    if frame == 4:
        parts.append(arrow(third))
        parts.append(_trav(408, 44, half=True))
    parts.append('</svg>')
    return "".join(parts)


def _heart(cx, cy, k=1.0, fill="var(--accent)"):
    return ('<path transform="translate(%s %s) scale(%s)" d="M0 8 C-9 1 -8 -7 -3 -7 C-1 -7 0 -5.5 0 -4.5 C0 -5.5 1 -7 3 -7 C8 -7 9 1 0 8Z" fill="%s"/>' % (cx, cy, k, fill))


def _coin(cx, cy, r=8):
    return ('<circle cx="%s" cy="%s" r="%s" fill="var(--accent)"/><circle cx="%s" cy="%s" r="%s" fill="none" stroke="var(--accent-ink)" stroke-width="1.4" opacity=".7"/>' % (cx, cy, r, cx, cy, r * .62))


def _jar(cx, cy):
    return ('<rect x="%s" y="%s" width="30" height="32" rx="8" fill="var(--surface-2)" stroke="var(--accent)" stroke-width="2.5"/>'
            '<rect x="%s" y="%s" width="36" height="9" rx="3" fill="var(--accent)"/>' % (cx - 15, cy - 14, cx - 18, cy - 20)) + _heart(cx, cy + 3, 1.6)


def spot(kind):
    """A small drawn picture for an info card: viewBox 120x72, literal attributes only, no real people."""
    P = person
    parts = []
    if kind == "help":
        parts += [P(38, 38, "#c0603f", "#d9a47a", "#2a1d17", "bun", .8), _heart(92, 22, 1.5), _coin(92, 52)]
    elif kind == "shared":
        parts += [_jar(60, 40), P(22, 42, "#4f7a62", "#b98a63", "#c9c4c0", "grey", .42), P(98, 42, "var(--accent)", "#e0b48a", "#2a1d17", "pigtails", .42)]
    elif kind == "child":
        parts += [P(28, 38, "var(--accent)", "#e0b48a", "#2a1d17", "pigtails", .8),
                  '<path d="M82 24 A14 14 0 0 0 82 52 Z" fill="var(--accent)"/>',
                  '<path d="M86 24 A14 14 0 0 1 86 52 Z" fill="none" stroke="var(--accent)" stroke-width="2.5"/>',
                  '<path d="M104 38 H116 M110 32 L116 38 L110 44" fill="none" stroke="var(--accent)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>']
    elif kind == "charge":
        parts += [P(34, 38, "#c0603f", "#d9a47a", "#2a1d17", "bun", .8), P(80, 44, "#4f7a62", "#b98a63", "#c9c4c0", "grey", .42), P(102, 44, "var(--accent)", "#e0b48a", "#2a1d17", "pigtails", .42)]
    elif kind == "jar":
        parts += [_jar(60, 40), _heart(28, 22, 1.0), _heart(94, 18, .9), _heart(90, 54, .8)]
    elif kind == "account":
        parts += [P(36, 38, "#c0603f", "#d9a47a", "#2a1d17", "bun", .8),
                  '<rect x="68" y="22" width="40" height="28" rx="6" fill="var(--bg)" stroke="var(--accent)" stroke-width="2.5"/>'
                  '<line x1="74" y1="32" x2="100" y2="32" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>'
                  '<line x1="74" y1="41" x2="92" y2="41" stroke="var(--line-strong)" stroke-width="3" stroke-linecap="round"/>']
    elif kind == "sprout":
        parts += [P(34, 40, "var(--accent)", "#e0b48a", "#2a1d17", "pigtails", .8),
                  '<path d="M72 60 H100" stroke="var(--line-strong)" stroke-width="3" stroke-linecap="round"/>'
                  '<path d="M86 60 V38" stroke="var(--accent)" stroke-width="3" stroke-linecap="round" fill="none"/>'
                  '<path d="M86 46 C75 46 71 38 73 31 C82 31 86 38 86 46Z" fill="var(--accent)"/>'
                  '<path d="M86 41 C97 41 101 33 99 26 C90 26 86 33 86 41Z" fill="#4f7a62"/>']
    elif kind == "pair":
        parts += [P(34, 38, "#c0603f", "#d9a47a", "#2a1d17", "bun", .6), P(86, 38, "#4f7a62", "#b98a63", "#c9c4c0", "grey", .6), _heart(60, 36, 1.7)]
    elif kind == "book":
        parts += ['<path d="M60 20 C48 13 32 13 18 19 V56 C32 50 48 50 60 57 Z" fill="var(--surface-2)" stroke="var(--accent)" stroke-width="2.5" stroke-linejoin="round"/>'
                  '<path d="M60 20 C72 13 88 13 102 19 V56 C88 50 72 50 60 57 Z" fill="var(--bg)" stroke="var(--accent)" stroke-width="2.5" stroke-linejoin="round"/>'
                  '<path d="M28 28 C34 26 42 26 50 29 M28 37 C34 35 42 35 50 38 M70 29 C78 26 86 26 92 28 M70 38 C78 35 86 35 92 37" fill="none" stroke="var(--line-strong)" stroke-width="2.5" stroke-linecap="round"/>']
    elif kind == "shop":
        parts += ['<rect x="26" y="30" width="68" height="28" rx="3" fill="var(--surface-2)" stroke="var(--accent)" stroke-width="2.5"/>'
                  '<path d="M20 30 L28 12 H92 L100 30 Z" fill="var(--accent)"/>'
                  '<path d="M20 30 H100" stroke="var(--accent-ink)" stroke-width="1.5" opacity=".5"/>'
                  '<rect x="52" y="38" width="16" height="20" rx="2" fill="var(--accent)"/>']
    return '<svg class="spot" viewBox="0 0 120 72" role="img" aria-hidden="true">%s</svg>' % "".join(parts)


def who_parts(t, anchor=None):
    """The two founder-line items, with the two names linked (a styled span on the drawing, a real link on the site)."""
    a = anchor or (lambda href, text: '<span class="link a">%s</span>' % text)
    return (t["who1"].replace("Thon Ly", a("https://thonly.org/", "Thon Ly")),
            t["who2"].replace("Miss Aquarius", a("https://missaquarius.org/", "Miss Aquarius")))


def disc_html(t):
    """The footer disclaimer, its first sentence held on one line (white-space: nowrap)."""
    d = t["disc"]
    for sep in (". ", "។ "):
        i = d.find(sep)
        if i > 0:
            return '<span class="nw">%s</span> %s' % (d[:i + len(sep.strip())], d[i + len(sep):])
    return d


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
    if kind == "states":
        k = kmc.strip()
        body = ('%s%s<section><p class="stl">%s</p><h1 class="%s">%s</h1><p class="lede%s">%s</p><p style="margin:26px 0 0"><span class="btn%s">%s</span></p></section>'
                '<section><p class="stl">%s</p><h1 class="%s">%s</h1><p class="lede%s">%s</p><p style="margin:26px 0 0;display:flex;gap:12px;flex-wrap:wrap"><span class="btn2%s">%s</span><span class="btn%s">%s</span></p></section>'
                '<section><p class="stl">%s</p><div style="border:1px solid var(--line);border-radius:var(--r-card);padding:18px;background:var(--surface)"><div style="display:flex;justify-content:flex-end;margin-bottom:16px">%s</div><p style="margin:0;text-align:center"><span class="toast%s">%s</span></p></div></section>'
                '<footer><p class="note">%s</p></footer>'
                % (head, ph, t["st_login"], k, t["login_h"], kmc, t["login_p"], kmc, t["login_btn"],
                   t["st_nf"], k, t["nf_h"], kmc, t["nf_p"], kmc, t["nf_home"], kmc, t["login_btn"],
                   t["st_copied"], share, kmc, t["copied"],
                   ("[ Khmer is our own placeholder until a native reader approves it ]" if lang == "km" else "[ Drawing. This page takes no payments. ]")))
    elif kind == "motion":
        body = ('%s<section class="intro" style="padding:24px 0 8px;display:block"><h1 class="%s" style="font-size:2rem">%s</h1><div class="art" style="max-width:560px;margin-top:20px">%s</div></section>'
                % (head, kmc.strip(), t["how_h"], explainer_fragment(lang)))
    elif kind == "storyboard":
        body = ('%s<section class="intro" style="padding-bottom:24px"><h1 class="%s">%s</h1>%s</section><div class="sb">%s</div><p class="%s" style="margin:24px 0 0;color:var(--ink-dim)">%s</p><p class="note">%s</p>'
                % (head, kmc.strip(), t["sb_h"], ph,
                   "".join('<figure>%s<figcaption><b class="mono">%d</b> · <span class="%s">%s</span></figcaption></figure>' % (flow_svg(i + 1), i + 1, kmc.strip(), t["sb_cap"][i]) for i in range(4)),
                   kmc.strip(), t["sb_legend"], t["sb_note"]))
    else:
        intro_art = '<div class="art"><div class="poster">%s<p class="note%s" style="margin:0">[ %s ]</p></div></div>' % (flow_svg(4), kmc, t["how_poster"])
        steps = "".join('<div class="step%s">%s<b>%d</b>%s</div>' % (kmc, flow_svg(i + 1), i + 1, s) for i, s in enumerate(t["steps"]))
        ben = "".join('<li class="%s">%s</li>' % (kmc.strip(), b) for b in t["ben"])
        why = "".join('<div class="card">%s<h3 class="%s">%s</h3><p class="%s">%s</p></div>' % (spot(k), kmc.strip(), n, kmc.strip(), d) for k, (n, d) in zip(("help", "shared", "child", "charge"), t["why"]))
        things = "".join('<div class="card">%s<h3>%s</h3><p class="%s">%s</p></div>' % (spot(k), n, kmc.strip(), d) for k, (n, d) in zip(("jar", "account", "sprout"), t["things"]))
        elsewhere = "".join('<div class="card">%s<h3 class="%s">%s</h3><p class="%s">%s</p><p class="note">%s</p></div>' % (spot(k), kmc.strip(), n, kmc.strip(), d, h) for k, (n, d, h) in zip(("pair", "book", "shop"), t["else"]))
        body = ('%s<section class="intro"><div><h1 class="%s">%s</h1><p class="lede%s">%s</p><p style="margin:32px 0 0"><span class="btn%s">%s</span></p><p class="note%s">%s</p>%s</div>%s</section>'
                '<section><h2 class="%s">%s</h2><div class="steps">%s</div></section>'
                '<section><h2 class="%s">%s</h2><div class="cols cols4">%s</div></section>'
                '<section><h2 class="%s">%s</h2><ul class="ben">%s</ul></section>'
                '<section><h2 class="%s">%s</h2><div class="cols">%s</div></section>'
                '<section><h2 class="%s">%s</h2><p class="lede%s" style="margin-top:0">%s</p><p style="margin:18px 0 0"><span class="link a">%s</span> <span class="note" style="margin-left:8px">%s</span></p></section>'
                '<section><h2 class="%s">%s</h2><div class="cols">%s</div></section>'
                '<footer><div class="foot-row"><p class="who%s">%s</p><p class="who%s">%s</p>%s</div><p class="%s">%s</p><p class="note">%s</p></footer>'
                % (head, kmc.strip(), t["h1"], kmc, t["sub"], kmc, t["cta"], kmc, t["cta_note"], ph, intro_art,
                   kmc.strip(), t["how_h"], steps,
                   kmc.strip(), t["why_h"], why,
                   kmc.strip(), t["ben_h"], ben,
                   kmc.strip(), t["things_h"], things,
                   kmc.strip(), t["is_h"], kmc, t["is_p"], t["is_link"], t["is_link_note"],
                   kmc.strip(), t["else_h"], elsewhere,
                   kmc, who_parts(t)[0], kmc, who_parts(t)[1], seg_t,
                   kmc.strip(), disc_html(t),
                   ("[ Khmer is our own placeholder until a native reader approves it ]" if lang == "km" else "[ Drawing. This page takes no payments. ]")))
    body = body.replace("\u2120", '<span class="sm">\u2120</span>')
    width = 1440 if size == "desk" else 390
    return ('<!doctype html>\n<html lang="%s" data-theme="%s">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=%d">\n'
            '<meta name="googlebot" content="noindex,nofollow"><meta name="bingbot" content="noindex,nofollow">\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,500;6..72,600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&family=Noto+Sans+Khmer:wght@400;500;600&display=swap">\n'
            '<link rel="stylesheet" href="board.css?v=%s">\n<style>[hidden]{display:none!important}</style>\n<title>%s</title>\n</head>\n<body>\n<div class="board %s">%s</div>\n</body>\n</html>\n'
            % (t["lang"], theme, width, CSSV, "heartbank.org landing (%s, %s, %s)" % (lang, theme, size), cls, body))


# ── the motion explainer (the scene file is the source of truth: explainer/scene.json) ───────────────────────────
SCENE = json.load(io.open(os.path.join(HERE, "explainer", "scene.json"), encoding="utf-8"))

EXPLAINER_CSS = """
.exp{margin:0}
.exp-stage svg{width:100%;height:auto;display:block}
.exp-caps{display:none;position:relative;min-height:5.4em;margin-top:6px}
.exp.is-live .exp-caps{display:block}
.exp-caps span{position:absolute;left:0;right:0;top:0;opacity:0;font-size:1.05rem;color:var(--ink)}
.exp-bar{display:flex;justify-content:space-between;align-items:center;gap:12px;margin:0 0 10px;min-height:2.1em}
.exp-ctl{display:none;margin:0 0 0 auto;text-align:right}
.exp.is-live .exp-ctl{display:block}
.exp-legend{margin:14px 2px 0}
.exp-end{display:inline-block;color:var(--accent);font-weight:600;text-decoration:underline;text-underline-offset:3px}
.exp-btn{font:inherit;font-size:.85rem;color:var(--ink);background:none;border:1px solid var(--line-strong);border-radius:var(--r-pill);padding:6px 16px;cursor:pointer}
.exp .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
@media (prefers-reduced-motion:reduce){.exp-caps,.exp-ctl{display:none!important}}
"""

# One pure function of t. A frame is render(t); the player only advances t, so ?t=<seconds> reproduces any frame
# (the MP4 export in /motion §7 relies on it). Nothing here counts down, fills, or leaves anyone empty-handed.
EXPLAINER_JS = r"""
(function(){var root=document.querySelector('[data-explainer]');if(!root)return;
var stage=root.querySelector('.exp-stage'),tpl=root.querySelector('template'),caps=[].slice.call(root.querySelectorAll('[data-cap]')),btn=root.querySelector('[data-toggle]'),en=root.querySelector('[data-end]');
var q=new URLSearchParams(location.search),fixed=q.has('t')?parseFloat(q.get('t')):null,END=@END@,
reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
if(reduce&&fixed===null)return; /* the static frame already in the markup IS the reduced-motion frame */
stage.innerHTML=tpl.innerHTML;root.classList.add('is-live');var svg=stage.firstElementChild;
var $=function(i){return svg.querySelector('[data-id="'+i+'"]')},pA=$('pA'),pB=$('pB'),pC=$('pC'),LA=pA.getTotalLength(),LB=pB.getTotalLength(),LC=pC.getTotalLength();
var cl=function(x){return x<0?0:x>1?1:x},ez=function(u){return u<.5?2*u*u:1-Math.pow(-2*u+2,2)/2},P=function(t,a,b){return ez(cl((t-a)/(b-a)))};
var pt=function(p,L,u){var s=p.getPointAtLength(L*u);return[s.x,s.y]},mv=function(e,x,y,s){e.setAttribute('transform','translate('+x+' '+y+')'+(s?' scale('+s+')':''))},op=function(e,v){e.setAttribute('opacity',v)};
var drawn=function(e,L,u,o){e.style.strokeDasharray=L;e.style.strokeDashoffset=L*(1-u);if(e.hasAttribute('marker-end'))e.setAttribute('marker-end',u>.97?'url(#arA)':'none');op(e,u>0?(o==null?1:o):0)};
var O1=pt(pA,LA,1),B0=pt(pB,LB,0),KEEP=[492,169];
var T=@SCENES@;
function render(t){
 op($('elder'),P(t,11,12));op($('friend'),P(t,18,19));
 drawn(pA,LA,P(t,1,4),t<11?1:1-.7*P(t,11,12));
 drawn(pB,LB,P(t,12.5,16),t<18?1:1-.7*P(t,18,19));
 drawn(pC,LC,P(t,19,22.5));
 var tr1=$('trav1');if(t>=1&&t<12){var a=pt(pA,LA,P(t,1,4));mv(tr1,a[0],a[1]);op(tr1,1)}else op(tr1,0);
 var tr2=$('trav2'),hr=$('halfR');
 if(t>=12){var x,y;
  if(t<12.5){var u=P(t,12,12.5);x=O1[0]+(B0[0]-O1[0])*u;y=O1[1]+(B0[1]-O1[1])*u}
  else if(t<16){var b=pt(pB,LB,P(t,12.5,16));x=b[0];y=b[1]}
  else if(t<19){var e=pt(pB,LB,1);x=e[0];y=e[1]}
  else{var c=pt(pC,LC,P(t,19,22.5));x=c[0];y=c[1]}
  mv(tr2,x,y);op(tr2,1);
  var k=P(t,12.5,14),sx=O1[0]-15,sy=O1[1];mv(hr,sx+(KEEP[0]-sx)*k,sy+(KEEP[1]-sy)*k,1+.1*k);op(hr,1)}
 else{op(tr2,0);op(hr,0)}
 if(en){var v=P(t,22.5,23.5);en.style.opacity=v;en.style.visibility=v>0?'visible':'hidden'}
 op($('card'),P(t,6,7));drawn($('ln1'),38,P(t,7,8.3));drawn($('ln2'),24,P(t,8.3,9.3));
 var h=P(t,9.5,10.3),ch=$('cardHeart');ch.setAttribute('transform','translate(26 1) scale('+(.85*h)+')');op(ch,h);
 caps.forEach(function(c,i){var s=T[i],o=Math.min(P(t,s[0],s[0]+.5),i===T.length-1?1:1-P(t,s[1]-.5,s[1]));c.style.opacity=t>=s[0]&&t<=s[1]?o:0});
}
var lbl=function(k){return btn.getAttribute('data-l-'+k)};
if(fixed!==null){render(fixed);if(btn)btn.hidden=true;return}
var t0=0,raf=0,last=0,playing=false;
function tick(now){if(!playing)return;var t=(now-last)/1000+t0;if(t>=END){t=END;playing=false;btn.textContent=lbl('replay')}render(t);if(playing)raf=requestAnimationFrame(tick);else t0=t}
function start(from){t0=from;last=performance.now();playing=true;btn.textContent=lbl('pause');raf=requestAnimationFrame(tick)}
btn.addEventListener('click',function(){if(playing){playing=false;cancelAnimationFrame(raf);t0=Math.min(END,(performance.now()-last)/1000+t0);btn.textContent=lbl('play')}else start(t0>=END?0:t0)});
render(0);btn.textContent=lbl('play');
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){if(es[0].isIntersecting&&!playing&&t0===0){start(0);io.disconnect()}},{threshold:.55});io.observe(root)}else start(0);
})();
"""


def explainer_svg_animated():
    a, b, c = (90, 172), (260, 44), (430, 172)
    bg = '<circle cx="%s" cy="%s" r="15" fill="var(--surface)"/>'
    stroke = 'fill="none" stroke="var(--accent)" stroke-width="3" stroke-linecap="round" marker-end="url(#arA)"'
    return ('<svg viewBox="0 0 520 230" role="img" aria-label="%s">'
            '<defs><marker id="arA" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10Z" fill="var(--accent)"/></marker></defs>'
            '%s%s<g data-id="elder" opacity="0">%s</g><g data-id="friend" opacity="0">%s</g>'
            '<path data-id="pA" d="M128 158 C190 128 330 128 392 158" %s opacity="0"/>'
            '<path data-id="pB" d="M412 142 C384 112 346 84 308 62" %s opacity="0"/>'
            '<path data-id="pC" d="M312 44 C346 30 380 30 408 44" %s opacity="0"/>'
            '<g data-id="card" opacity="0" transform="translate(260 204)"><rect x="-46" y="-17" width="92" height="34" rx="8" fill="var(--bg)" stroke="var(--accent)" stroke-width="2"/>'
            '<line data-id="ln1" x1="-32" y1="-4" x2="6" y2="-4" stroke="var(--accent)" stroke-width="3" stroke-linecap="round" opacity="0"/>'
            '<line data-id="ln2" x1="-32" y1="7" x2="-8" y2="7" stroke="var(--line-strong)" stroke-width="3" stroke-linecap="round" opacity="0"/>'
            '<g data-id="cardHeart" opacity="0" transform="translate(26 1) scale(0)">%s</g></g>'
            '<g data-id="trav1" opacity="0">%s%s%s%s</g>'
            '<g data-id="trav2" opacity="0">%s%s<path d="M-15 -10 A10 10 0 0 0 -15 10 Z" fill="var(--accent)"/>%s</g>'
            '<path data-id="halfR" opacity="0" d="M0 -10 A10 10 0 0 1 0 10 Z" fill="var(--accent)"/>'
            '</svg>') % (
        "{ALT}", parent(*a), child(*c), elder(*b), friend(480, 44), stroke, stroke, stroke, _heart(0, 0, 1.0),
        bg % (-15, 0), bg % (15, -3), _coin(-15, 0, 10), _heart(15, -3, 1.5),
        bg % (-15, 0), bg % (15, -3), _heart(15, -3, 1.5))


def explainer_fragment(lang):
    """The explainer as one self-contained fragment: the STATIC frame in the markup (no script, reduced motion, crawlers),
    the animated SVG in a <template> the player swaps in, four captions, one button, and a screen-reader list."""
    st = SCENE["strings"]
    km = " km" if lang == "km" else ""
    caps = "".join('<span data-cap class="%s">%s</span>' % (km.strip(), st[s["caption"]][lang]) for s in SCENE["scenes"])
    sr = "".join("<li>%s</li>" % st[s["caption"]][lang] for s in SCENE["scenes"])
    alt = st["alt"][lang].replace('"', "&quot;")
    scenes = json.dumps([s["t"] for s in SCENE["scenes"]])
    js = EXPLAINER_JS.replace("@END@", str(SCENE["brief"]["length_s"])).replace("@SCENES@", scenes)
    static = flow_svg(4).replace('role="img" aria-hidden="true"', 'role="img" aria-label="%s"' % alt)
    legend = T[lang]["sb_legend"]
    return ('<figure class="exp" data-explainer data-lang="%s">'
            '<div class="exp-bar"><a class="exp-end%s" data-end href="https://thank.heartbank.org/">%s &rarr;</a>'
            '<div class="exp-ctl"><button type="button" class="exp-btn%s" data-toggle data-l-play="%s" data-l-pause="%s" data-l-replay="%s">%s</button></div></div>'
            '<div class="poster"><div class="exp-stage">%s</div><template>%s</template><div class="exp-caps%s" aria-hidden="true">%s</div></div>'
            '<p class="note exp-legend%s">%s</p>'
            '<ol class="sr">%s</ol><style>%s</style><script>%s</script></figure>'
            % (lang, km, T[lang]["cta"], km, st["play"][lang], st["pause"][lang], st["replay"][lang], st["play"][lang],
               static, explainer_svg_animated().replace("{ALT}", alt), km, caps, km, legend, sr, EXPLAINER_CSS, js))


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
    ("StatesEn.html", "en", "light", "phone", "states", "9 · Login signpost, not found, link copied, English, phone"),
    ("StatesKm.html", "km", "light", "phone", "states", "10 · Login signpost, not found, link copied, Khmer, phone"),
    ("Explainer.html", "en", "light", "desk", "motion", "11 · Motion explainer, English (plays once; ?t=SECONDS shows any frame)"),
    ("ExplainerKm.html", "km", "light", "desk", "motion", "12 · Motion explainer, Khmer (plays once; ?t=SECONDS shows any frame)"),
]

HEIGHTS = {}
if os.path.exists(os.path.join(HERE, "heights.json")):
    HEIGHTS = json.load(open(os.path.join(HERE, "heights.json")))


CSSV = __import__("hashlib").sha256((CSS.strip() + "\n").encode("utf-8")).hexdigest()[:8]


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
