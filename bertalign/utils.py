import re
from functools import lru_cache

from wtpsplit import SaT


@lru_cache(maxsize=1)
def _get_sat_model() -> SaT:
    return SaT(
        "sat-12l-sm",
        ort_providers=[
            "CPUExecutionProvider",
            "CUDAExecutionProvider",
        ],
    )

def clean_text(text):
    clean_text = []
    text = text.strip()
    lines = text.splitlines()
    for line in lines:
        line = line.strip()
        if line:
            line = re.sub('\s+', ' ', line)
            clean_text.append(line)
    return "\n".join(clean_text)

def split_sents(text):
    sat = _get_sat_model()
    sents = sat.split(
        text,
        # do_paragraph_segmentation=True,
        # split_on_input_newlines=False,

        block_size=1024, # default 512
        stride=256, # default 64
        weighting="hat", # allow larger stride, there is no EWMA though
    )

    return [sent.strip() for sent in sents if sent.strip()]
        
def yield_overlaps(lines, num_overlaps):
    lines = [_preprocess_line(line) for line in lines]
    for overlap in range(1, num_overlaps + 1):
        for out_line in _layer(lines, overlap):
            # check must be here so all outputs are unique
            out_line2 = out_line[:10000]  # limit line so dont encode arbitrarily long sentences
            yield out_line2

def _layer(lines, num_overlaps, comb=' '):
    if num_overlaps < 1:
        raise Exception('num_overlaps must be >= 1')
    out = ['PAD', ] * min(num_overlaps - 1, len(lines))
    for ii in range(len(lines) - num_overlaps + 1):
        out.append(comb.join(lines[ii:ii + num_overlaps]))
    return out
    
def _preprocess_line(line):
    line = line.strip()
    if len(line) == 0:
        line = 'BLANK_LINE'
    return line
