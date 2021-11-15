from typing import List

import Levenshtein


def phoneme_error_rate(p_seq1: List[str], p_seq2: List[str]):
    p_vocab = set(p_seq1 + p_seq2)
    p2c = dict(zip(p_vocab, range(len(p_vocab))))
    c_seq1 = [chr(p2c[p]) for p in p_seq1]
    c_seq2 = [chr(p2c[p]) for p in p_seq2]
    return Levenshtein.distance(''.join(c_seq1),
                                ''.join(c_seq2)) / len(c_seq2)
