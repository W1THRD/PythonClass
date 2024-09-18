# function for pairing bases in mRNA
def get_mRNA(char):
    if(char == "A"):
        return("U")
    elif(char == "T"):
        return("A")
    elif(char == "C"):
        return("G")
    elif(char == "G"):
        return("C")
    else:
        print("Something weird happened")

# list of all amino acids (index = code line - 15)
amino_acids = ["Phenyl-alanine", # 0
               "Leucine",        # 1
               "Isoleucine",     # 2
               "Methionine",     # 3
               "Valine",         # 4
               "Serine",         # 5
               "Proline",        # 6
               "Threonine",      # 7
               "Alanine",        # 8
               "Tyrosine",       # 9
               "STOP",           # 10
               "Histidine",      # 11
               "Glutamine",      # 12
               "Asparagine",     # 13
               "Lysine",         # 14
               "Aspartic Acid",  # 15
               "Glutamic Acid",  # 16
               "Cysteine",       # 17
               "Tryptophan",     # 18
               "Arginine",       # 19
               "Glycine"]        # 20

# dictionaries of indexes for converting codons to amino acids (3 levels deep)
acid_dict = {}
acid_dict["A"] = {
    "A": {
        "A": 14,
        "G": 14,
        "U": 13,
        "C": 13
    },
    "G": {
        "A": 19,
        "G": 19,
        "U": 5,
        "C": 5
    },
    "U": {
        "A": 2,
        "G": 3,
        "U": 2,
        "C": 2
    },
    "C": {
        "A": 7,
        "G": 7,
        "U": 7,
        "C": 7
    }
}
acid_dict["G"] = {
    "A": {
        "A": 16,
        "G": 16,
        "U": 15,
        "C": 15
    },
    "G": {
        "A": 20,
        "G": 20,
        "U": 20,
        "C": 20
    },
    "U": {
        "A": 4,
        "G": 4,
        "U": 4,
        "C": 4
    },
    "C": {
        "A": 8,
        "G": 8,
        "U": 8,
        "C": 8
    }
}

acid_dict["U"] = {
    "A": {
        "A": 10,
        "G": 10,
        "U": 9,
        "C": 9
    },
    "G": {
        "A": 10,
        "G": 18,
        "U": 17,
        "C": 17
    },
    "U": {
        "A": 1,
        "G": 1,
        "U": 0,
        "C": 0
    },
    "C": {
        "A": 5,
        "G": 5,
        "U": 5,
        "C": 5
    }
}
acid_dict["C"] = {
    "A": {
        "A": 12,
        "G": 12,
        "U": 11,
        "C": 11
    },
    "G": {
        "A": 19,
        "G": 19,
        "U": 19,
        "C": 19
    },
    "U": {
        "A": 1,
        "G": 1,
        "U": 1,
        "C": 1
    },
    "C": {
        "A": 6,
        "G": 6,
        "U": 6,
        "C": 6
    }
}

# function for finding amino acids from mRNA codons
def getAminoAcid(codon):
    return( amino_acids[acid_dict[codon[0]][codon[1]][codon[2]]] )