def seq_join0(seqs):
    return tuple(((0,) + seq + (0,))[i] for seq in seqs for i in range(len((((0,) + seq + (0,))))))

print(seq_join0(((3, 1, 4), (1, 5), (9, 2, 6))))