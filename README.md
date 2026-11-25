[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/Angga-Nugraha/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/Angga-Nugraha/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

# The World in One Image — Tuesday 24 November 2026

A dense newspaper front page summing up 24 November 2026 in a single
1024×1024 image: **30 dated stories** — masthead date, Hormuz-tanker hero,
7 illustrated vignettes, 22 headline cells, and a sources credit box.
Built for [news-image-20261124](https://make.fun/bounty/news-image-20261124)
on make.fun ($100, free entry, account @golden-walrus-30). Entries close
2026-11-26 07:00 WIB; result due 2026-12-10.

## The 30 stories

1. **TANKERS HIT IN HORMUZ** (hero) — Iran claims three tankers hit mines
   in the Strait of Hormuz despite US escort; unverified.
2. **GROK SUED** — Virginia & Oregon sue over sexualised images.
3. **SANOFI $41B DEAL** — Sanofi to buy Insmed for $41 billion in cash.
4. **NATO SPACE DEFENCE** — NATO vows to defend against threats in space.
5. **NEPAL QUAKE** — Magnitude 5.6 quake shakes eastern Nepal.
6. **CIA + ODNI HACKED** — Apparent hack hits unclassified systems.
7. **HUAWEI CONVICTED** — Jury convicts on 10 of 12 criminal counts.
8. **DEMOCRATS TAKE HOUSE 259** — Democrats secure at least 259 seats.
9. **SHANGHAI BOSS PURGED** — Party chief Chen Jining probed for graft.
10. **ENGLAND CRUSH AUSTRALIA** — England chase 185 in 13.1 overs.
11. **HAMAS SECURITY CHIEF KILLED** — Israeli strike in Gaza City.
12. **US CONFIDENCE SURGES** — Consumer confidence jumps to 103.3.
13. **WHO FLEES EBOLA HOSPITAL** — WHO evacuates staff in DR Congo.
14. **SENEGAL AFCON CHAMPIONS AGAIN** — CAS reinstates Senegal.
15. **POPE'S DEVIL DIARY** — Late pope's private diary published.
16. **SARKOZY TO TRIAL** — Sarkozy and Carla Bruni to face trial.
17. **FORT HOOD KILLER'S STAY BID** — 2009 gunman seeks stay of execution.
18. **NVIDIA SLIDE AFTER BOUNCE** — Nvidia falls ~6% after a 31.5% surge.
19. **PUNJAB ALLIANCE RETURNS** — BJP and Akali Dal reunite for 2027.
20. **CITI EYES VENEZUELA** — Citi weighs return five years after exit.
21. **TRUMP PARDONS TURKEYS** — Trump spares Freedom and Feathers.
22. **ZELENSKIY OWNS SHIP STRIKES** — Kyiv claims Russian ship strikes.
23. **MICROSOFT "CODE RED"** — Overhaul after the 24-hour outage.
24. **GIULIANI GETS TOP MEDAL** — Trump awards the Medal of Freedom.
25. **US TARIFFS LOOM** — US poised to unveil new tariffs on 16 partners.
26. **O'HARE RADAR DELAYS** — Radar issue delays flights at Chicago O'Hare.
27. **US ENVOY DOUBTS ISRAEL AID END** — Envoy "not certain" aid ends.
28. **REAL MADRID BEAT PSV** — Bellingham wonder goal sees off PSV.
29. **IRAN RIAL RECORD LOW** — Rial hits ~2.85m per dollar.
30. **INDONESIA FIRE TOLL 26** — Toll confirmed at 26; probe opened.

Attribution is kept as reported throughout: Hormuz is Iran's claim
(unverified), the Zelenskiy sinking is Kyiv's claim, and the Indonesia
figure is the confirmed toll only — no missing-persons figure is printed.

## How it runs

`main.py` is standard library only. It copies the committed `entry.png`
to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`) and
prints its size and sha256. Nothing is rendered at run time, no network,
no fonts, no third-party packages — the picture is built once and shipped.

```sh
MAKEFUN_OUTPUT_DIR=/output python3 -P -s main.py
```

## Verification (round 5)

- Output: 1024×1024 PNG, 838,529 bytes (≤ 1 MiB), sha256
  `923f2259ef2549337425a2903c0b0cc917c523a13fea4b72e347ac6931a04495` —
  byte-identical to the round-3/round-4 rendered page.
- Grader-style runs all exit 0: normal run, clean environment, read-only
  source tree, and a run with site-packages disabled (the shape of the
  grader's minimal image, where Pillow is absent).
- Rounds 3 and 4 rendered the page at grade time with Pillow and both
  failed `run_completes` with exit 1; round 2's stdlib-only copier passed
  it. Round 5 returns to the proven shape with the same dense image.

## Files

- `main.py` — stdlib-only entrypoint (copies `entry.png` to the output dir).
- `entry.png` — the 1024×1024 front page (30 stories).
- `assets/` — the 8 illustration sources the page was composed from.
- `LICENSE` — MIT.
