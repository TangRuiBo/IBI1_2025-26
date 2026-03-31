import matplotlib.pyplot as plt
from collections import Counter

def read_stop_genes(file_path):
    sequences = []
    current_seq = ""
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if current_seq:
                    sequences.append(current_seq)
                    current_seq = ""
            else:
                current_seq += line
        if current_seq:
            sequences.append(current_seq)
    return sequences

def count_codon_frequency(sequences, target_stop):
    codon_count = Counter()
    for seq in sequences:
        max_orf = ""
        for i in range(0, len(seq)-2, 3):
            if seq[i:i+3] == "ATG":
                for j in range(i, len(seq)-2, 3):
                    codon = seq[j:j+3]
                    if codon == target_stop:
                        orf_candidate = seq[i:j+3]
                        if len(orf_candidate) > len(max_orf):
                            max_orf = orf_candidate
                        break
        if max_orf:
            for k in range(0, len(max_orf)-3, 3):
                codon = max_orf[k:k+3]
                codon_count[codon] += 1
    return codon_count

def plot_pie(codon_count, stop_codon):
    total = sum(codon_count.values())
    main_codons = {}
    other_sum = 0
    
    for codon, count in codon_count.items():
        percentage = (count / total) * 100
        if percentage >= 1.0:
            main_codons[codon] = count
        else:
            other_sum += count
    
    if other_sum > 0:
        main_codons['Other'] = other_sum
    
    sorted_items = sorted(main_codons.items(), key=lambda x: x[1], reverse=True)
    labels = [item[0] for item in sorted_items]
    sizes = [item[1] for item in sorted_items]
    
    plt.figure(figsize=(14, 10))
    explode = [0.05] * len(labels)
    wedges, texts, autotexts = plt.pie(
        sizes, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=90,
        explode=explode,
        labeldistance=1.05,
        pctdistance=0.8
    )
    
    plt.setp(texts, fontsize=10)
    plt.setp(autotexts, fontsize=9)
    plt.title(f'Codon Distribution (≥1%) for Sequences ending with {stop_codon}', fontsize=14)
    plt.axis('equal')
    plt.savefig(f'codon_pie_{stop_codon}_optimized.png', dpi=300, bbox_inches='tight')
    print(f"Optimized pie chart saved as codon_pie_{stop_codon}_optimized.png")

if __name__ == "__main__":
    valid_stops = ['TAA', 'TAG', 'TGA']
    user_stop = input("Please enter stop codon (TAA/TAG/TGA)：").strip().upper()

    while user_stop not in valid_stops:
        print("Invalid input! Please enter TAA, TAG or TGA")
        user_stop = input("Re-enter：").strip().upper()

    seqs = read_stop_genes("stop_genes.fa")
    count = count_codon_frequency(seqs, user_stop)
    print("\nCodon count results：")
    for codon, num in count.items():
        print(f"{codon}: {num}")

    plot_pie(count, user_stop)
""" Because codons with less than one percent proportion overlap seriously when placed together, 
    as in the image codon_pie_TAA I generated, I have categorized all codons with less than one percent proportion 
    into the 'other' category."""
