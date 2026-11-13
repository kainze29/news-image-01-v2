# news-image-01: The World on 13 November 2026

One image that sums up the world's news of Friday 13 November 2026:
a newsroom-style cover with six labelled panels.

| Panel | Story |
| --- | --- |
| NVIDIA CEO RESIGNS | Nvidia chief Jensen Huang resigns; shares fall about 16%; the US Senate Banking Committee had summoned Huang and Commerce Secretary Lutnick |
| UKRAINE TALKS: EU JOINS | Zelensky meets US envoys; Europe is promised a seat at the next round of Ukraine-Russia talks; a large prisoner exchange is agreed |
| DRONE HITS RUSSIAN WARSHIP | A Ukrainian drone strikes the Russian corvette Naro-Fominsk in the Gulf of Finland; Finland confirms detecting the strike |
| IRAN CLAIMS BAHRAIN STRIKE | Iran says it struck a US radar site in Bahrain as Gulf tensions rise |
| FBI: N. KOREA $400M HACK | The FBI says North Korean hackers used fake video calls and deepfakes to steal about $400m in crypto |
| STRIKE HITS GAZA HOSPITAL | An Israeli strike on Nasser Hospital in Khan Younis kills six people, including a surgeon |

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled
`news.png` byte-for-byte to `/output/entry.png`. No network, no
rendering, so both runs write identical bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program
- `news.png` — the cover image (1024x1024 PNG, under 1 MiB)
- `LICENSE` — MIT
