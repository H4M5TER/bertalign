# Bertalign

This fork currently

- supports specifying languages manually
- replaces googletrans by lingua for language detection
  - because newer version of googletrans is using coroutine and thus contagious
    - I'm not willing to modify other codes to adapt it
  - because networkless is prefered
- replaces [sentence-splitter](https://github.com/mediacloud/sentence-splitter) by [pySBD](https://github.com/nipunsadvilkar/pySBD) for sentence segmentation
  - `sentence-splitter` doesn't support Chinese and Japanese
  - Upstream worked around a simple punctuation dependent Chinese splitter
  - `pySBD` doesn't support Korean and Vietnamese though
  - Chinese and Japanese support of `pySBD` is also suspectable

This fork is willing to

- support more embedding models
  - harrier-oss: current bitext SOTA
  - LaBSE is still very high ranked on [MMTEB](https://mteb-leaderboard.hf.space/benchmark/MTEB(Multilingual%2C%20v2)?s.summary=tt%3ABitextMining&d.summary=desc) though
- support [wtpsplit](https://github.com/segment-any-text/wtpsplit)
  - good quality
  - punctuation agnostic
  - language agnostic, so the whole project could be as well
  - but kind of slow (compared to heuristic methods, ofc)
