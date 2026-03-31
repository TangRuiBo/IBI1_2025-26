def process_fasta():
    
    input_file = r"Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
    output_file = "stop_genes.fa"
    
    stop_codons = {'TAA', 'TAG', 'TGA'}
    gene_name = ""
    sequence = ""
    results = []

    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if gene_name and sequence:
                    found_stops = []
                    for i in range(0, len(sequence)-2, 3):
                        codon = sequence[i:i+3]
                        if codon in stop_codons and codon not in found_stops:
                            found_stops.append(codon)
                    if found_stops:
                        new_header = f">{gene_name} {' '.join(found_stops)}"
                        results.append((new_header, sequence))

                gene_name = line.split()[0][1:]
                sequence = ""
            else:
                sequence += line

        if gene_name and sequence:
            found_stops = []
            for i in range(0, len(sequence)-2, 3):
                codon = sequence[i:i+3]
                if codon in stop_codons and codon not in found_stops:
                    found_stops.append(codon)
            if found_stops:
                new_header = f">{gene_name} {' '.join(found_stops)}"
                results.append((new_header, sequence))

    with open(output_file, 'w') as f:
        for header, seq in results:
            f.write(header + '\n')
            f.write(seq + '\n')

process_fasta()
print("We have generated stop_genes.fa file")