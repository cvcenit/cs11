def seq_join(seqs):
    return tuple(seq[i] for seq in seqs for i in range(len(seq)))

print(seq_join(((3, 1, 4), (1, 5), (9, 2, 6)))
)