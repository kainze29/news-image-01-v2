# The World Today, 13 November 2026

A single-image entry for the make.fun news-image-01 bounty: a magazine-cover
style picture that sums up the world news of Friday 13 November 2026 in six
labelled panels, under a header reading `13 NOV 2026 / THE WORLD TODAY`.

## How it works

`main.py` is a small Python 3 program using only the standard library. It
copies the bundled cover image, `news.png`, byte-for-byte into the output
directory as `entry.png`. It renders nothing and fetches nothing.

Run it with:

```sh
python3 main.py
```

The output directory comes from the `MAKEFUN_OUTPUT_DIR` environment
variable and defaults to `/output`.

## The six panels

1. **NVIDIA CEO RESIGNS** - Nvidia chief Jensen Huang steps down and the
   shares fall about sixteen percent, after the US Senate Banking Committee
   had summoned Huang and Commerce Secretary Lutnick.
2. **UKRAINE TALKS EU JOINS** - Zelensky meets US envoys, Europe is promised
   a seat at the next round of Ukraine-Russia talks, and a large prisoner
   exchange is agreed.
3. **DRONE HITS RUSSIAN WARSHIP** - A Ukrainian drone strikes the Russian
   corvette Naro-Fominsk in the Gulf of Finland, and Finland confirms
   detecting the strike.
4. **IRAN CLAIMS BAHRAIN STRIKE** - Iran says it struck a US radar site in
   Bahrain as Gulf tensions rise.
5. **FBI N KOREA $400M HACK** - The FBI says North Korean hackers used fake
   video calls and deepfakes to steal about four hundred million dollars in
   crypto.
6. **STRIKE HITS GAZA HOSPITAL** - An Israeli strike on Nasser Hospital in
   Khan Younis kills six people, including a surgeon.

## Files

- `main.py` - the entry program.
- `news.png` - the bundled 1024x1024 cover image.
- `LICENSE` - licence for the entry.
