PROTEIN_CODONS = {"AUG":"Methionine",
                    "UUU": "Phenylalanine",
                    "UUC": "Phenylalanine",
                    "UUA": "Leucine",
                    "UUG": "Leucine",
                    "UCU": "Serine",
                    "UCC": "Serine",
                    "UCA": "Serine",
                    "UCG": "Serine",
                    "UAU": "Tyrosine",
                    "UAC": "Tyrosine",
                    "UGU": "Cysteine",
                    "UGC": "Cysteine",
                    "UGG": "Tryptophan",
                    "UAA": "STOP",
                    "UAG": "STOP",
                    "UGA": "STOP"
                    }

def proteins(strand):
    resulting_proteins = []
    for i in range(0, len(strand),3):
        protein = PROTEIN_CODONS[strand[i:i+3]]
        if protein == "STOP":
            break
        resulting_proteins.append(protein)
    return resulting_proteins
