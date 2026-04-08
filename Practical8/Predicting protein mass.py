def protein_molecular_weight(sequence):
    #param sequence: Amino acid sequence string (A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V)

    aa_mass = {
        'A': 71.03711, 'R': 156.10111, 'N': 114.04293, 'D': 115.02694,
        'C': 103.00919, 'Q': 128.05858, 'E': 129.04259, 'G': 57.02146,
        'H': 137.05891, 'I': 113.08406, 'L': 113.08406, 'K': 128.09496,
        'M': 131.04049, 'F': 147.06841, 'P': 97.05276, 'S': 87.03203,
        'T': 101.04768, 'W': 186.07931, 'Y': 163.06333, 'V': 99.06841
    }

    total_mass = 0.0
    for aa in sequence.upper():  # Unify into amino acid sequence string
        if aa not in aa_mass:
            raise ValueError(f"Error：{aa}，Please enter the standard amino acid sequence")
        else:
            total_mass += aa_mass[aa]

    return total_mass


test_seq = "AGPC"
mw = protein_molecular_weight(test_seq)
print(f"氨基酸序列：{test_seq}")
print(f"蛋白质分子量：{mw:.2f} amu")