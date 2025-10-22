def seq_join(seqs):
    res = []
    for seq in seqs:
        res += list(seq)
    return res

print(seq_join(((1,), (2,), (3,))))