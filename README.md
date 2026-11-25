[![make.fun](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Angga-Nugraha/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Angga-Nugraha/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

# news-image-20261124 — The World in One Image

A newspaper front page summing up Tuesday 24 November 2026 in one image:
30 stories — the Hormuz tanker attacks, Grok sued, the $41B Sanofi deal,
NATO's space-defence vow, the Nepal quake, the CIA hack, Huawei convicted,
and Democrats taking the House at 259 seats — plus 22 more headlines from
the day, across every region and beat.

Entry for the [make.fun bounty](https://make.fun/bounty/news-image-20261124):
"Sum up 24 November's world news in one image" ($100, free to enter).

## How it is built

`main.py` (Python 3, stdlib + Pillow only, no network) composes the
1024×1024 front page from the illustration assets in `assets/` and
PIL-rendered text — the masthead, hero caption, vignette labels and all
30 headlines are drawn by the program, never baked into the pictures —
and writes it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).
The build is deterministic: every run produces byte-identical output,
verified in-program against a pinned SHA-256.

Verified on this build: 1024×1024 RGB PNG, 838,529 bytes (under the
1 MiB gate), three runs byte-identical (sha256
`923f2259ef2549337425a2903c0b0cc917c523a13fea4b72e347ac6931a04495`).

## The 30 stories

Hero: tankers hit in Hormuz (Iran's claim, unverified). Vignettes: Grok
sued, Sanofi's $41B deal, NATO space defence, Nepal quake, CIA + ODNI
hacked, Huawei convicted, Democrats take the House at 259. Headline
cells: Shanghai purge, England v Australia, Hamas security chief killed,
US confidence, WHO Ebola evacuation, Senegal AFCON, Pope's diary,
Sarkozy trial, Fort Hood stay bid, Nvidia slide, Punjab alliance, Citi
eyes Venezuela, Trump pardons turkeys, Zelenskiy ship strikes,
Microsoft "Code Red", Giuliani medal, US tariffs, Indonesia fire toll
26, Iran rial record low, O'Hare radar delays, US envoy doubts Israel
aid end, Real Madrid beat PSV. All events of — or first reported on —
Tuesday 24 November 2026; nothing dated 25 November appears.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the composer (entrypoint)
- `entry.png` — the composed 1024×1024 front page (≤1 MiB)
- `assets/` — 8 illustration assets (no text, no recognisable faces, no logos)
- `LICENSE` — MIT
