# Your RNAseq
seq = 'AAGAUACAUGCAAGUGGUGUGUGUUCUCUGAGAGGGCCUAAAAG'

def validate_rna_sequence(RNA_seq):
    """Check ewhether the RNA sequence contains only A/U/G/C. 
       If there are error characters, throw an error and indicate 
       the position and the incorrect character.
    """
    valid_bases = {'A', 'U', 'G', 'C'}
    
    for index, base in enumerate(RNA_seq):
        if base not in valid_bases:
            raise ValueError(
                f" Error：in the place{index+1} there is a '{base}'\n"
                f"The right bases are：A、U、G、C"
            )
    
    print(" RNAseq verification passed: contains only A/U/G/C")

def find_largest_orf(RNA_seq):
    """Find ORF"""
    start_codon = 'AUG'
    stop_codons = {'UAA', 'UAG', 'UGA'}
    max_orf = ''
    n = len(RNA_seq)

    
    for i in range(n - 2):
        if RNA_seq[i:i+3] == start_codon:
            # Starting from the start codon, step through every 3 bases to find the stop codon
            for j in range(i, n-2, 3):
                codon = RNA_seq[j:j+3]
                if codon in stop_codons:
                    current_orf = RNA_seq[i:j+3]
                    if len(current_orf) > len(max_orf):
                        max_orf = current_orf
                    break
    return max_orf

if __name__ == "__main__":
    try:
        validate_rna_sequence(seq)
        
        largest_orf = find_largest_orf(seq)
        orf_length = len(largest_orf)

        print("\nThe ORF is：", largest_orf)
        print("ORF length：", orf_length)

    except ValueError as e:
        print("\n" + str(e))
