"""
General assisting functions
"""


def create_query_fasta(file_path:str, dna_sequence: str):
    with open(file_path, 'w') as out_fasta:
        out_fasta.write('>Query\n')
        for i in range(0, len(dna_sequence), 80):
            out_fasta.write(f'{dna_sequence[i: i+80]}\n')