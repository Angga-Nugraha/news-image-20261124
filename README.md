# The World in One Image — Tuesday 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![Rank](https://make.fun/badge/news-image-20261124/Angga-Nugraha/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![Reward](https://make.fun/badge/news-image-20261124/Angga-Nugraha/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124)

A newspaper front page summing up Tuesday 24 November 2026 in a single
image. The hero story is Iran's claim that oil tankers struck naval mines
and caught fire in the Strait of Hormuz despite a US escort — shown as two
burning tankers in a narrow strait at dusk, with the caption kept honest:
the claim is unverified, and the image does not state a tanker count.
Below it, four vignettes cover the rest of the day: Virginia and Oregon
suing SpaceX over Grok's nonconsensual sexualised images, Sanofi's $41
billion cash deal to buy US biotech Insmed, NATO vowing to defend against
threats in space after warnings of a possible Russian nuclear-armed
satellite launch, and a magnitude 5.6 earthquake in eastern Nepal.

## How the image was made

The five panels are original editorial illustrations in a warm-newsprint /
deep-blue style, composed with Python (Pillow) into a 1024×1024 front page:
a masthead naming the date, a headline and the hero image with a one-line
caption, and a row of four labelled vignettes. All text — masthead,
headline, caption and panel labels — was rendered crisply with PIL fonts,
never by the image model, so nothing is garbled. The final image was
downscaled and quantised to a 256-colour palette to stay under the 1 MiB
limit.

## Run

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to the output directory — `MAKEFUN_OUTPUT_DIR` when set,
otherwise `/output` — and verifies the copy's sha256 against the bundled
image's known digest. No network, deterministic: two runs produce
byte-identical output.
