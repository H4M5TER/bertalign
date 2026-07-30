# Bertalign

This fork make sentence splitting language agnostic by introducing [wtpsplit](https://github.com/segment-any-text/wtpsplit) and 500M (for onnx) runtime download size.
[googletrans](https://github.com/ssut/py-googletrans) and [sentence-splitter](https://github.com/mediacloud/sentence-splitter) is removed.
This project has full language agnostic now since LaBSE is already language agnostic.

This fork is willing to support more embedding models, such as harrier-oss, which is current [bitext SOTA on MMTEB](https://mteb-leaderboard.hf.space/benchmark/MTEB(Multilingual%2C%20v2)?s.summary=tt%3ABitextMining&d.summary=desc). However LaBSE is still very high ranked on MMTEB though.
