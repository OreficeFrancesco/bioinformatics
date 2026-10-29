def kmer_analyzer(genome:str, pattern:str) -> tuple[list[int], int]:
    indexes = []
    for i in range(len(genome)-len(pattern)+1):
        kmer = genome[i:i+len(pattern)]
        if kmer == pattern:
            indexes.append(i)
    count = len(indexes)
    return indexes, count

genome = #input
pattern = #input
indexes, count = find_kmer(genome, pattern)
print (f"the kmer {pattern} appears {count} times and its indexes are:{indexes}")
