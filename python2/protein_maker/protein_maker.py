# import libraries
import matcher

# introduce program to user
print("Hello, and welcome to Protein Maker!")
print("This program will take your DNA strand, and code it into an amino acid sequence!")
print("In DNA, A connects to T, and C connects to G.")
print("RNA works the same as DNA, except that A connects to U instead of T.")
print("So, let\'s do this!")
print("")

# get first DNA strand
print("PART 1: DNA Input")
print("When entering DNA, make sure to only use the letters A, T, C, and G.")
print("Also, only enter the letters in pairs of 3 (codons).")
dna_bases = ["A", "T", "C", "G"]
dna = ""
valid = False
while not valid:
    dna = input("Enter your DNA strand: ").replace(" ", "")
    if len(dna) % 3 == 0:
        for base in dna:
            if base in dna_bases:
                valid = True
            else:
                valid = False
                print("Error: invalid nitrogenous bases. Try again.")
                break
    else:
        print("Error: must have codons of 3. Try again.")

# split user input into codons
dna_codons = []
codon_builder = ""
codon_counter = 1
for base in dna:
    codon_builder += base
    if codon_counter == 3:
        dna_codons.append(codon_builder)
        codon_builder = ""
        codon_counter = 0
    codon_counter += 1
print("Your DNA strand: " + " ".join(dna_codons))
print()

# create and print out mRNA strand
print("PART 2: Transcription")
print("In the Nucleus, your DNA strand is used to make a pairing mRNA strand.")
print("This mRNA strand has the instructions for making the protein.")
mrna_codons = []
codon_builder = ""
for codon in dna_codons:
    for base in codon:
        codon_builder += matcher.get_mRNA(base)
    mrna_codons.append(codon_builder)
    codon_builder = ""
print("Newly-made mRNA Strand: " + " ".join(mrna_codons))
print()

# find and print out amino acids
print("PART 3: Translation")
print("After the mRNA is produced, it is sent to a ribosome to be translated.")
print("At a ribosome, the codons of the mRNA match with the anti-codons of tRNA.")
print("When they pair, they will cause amino acids to be bonded with peptide bonds.")
print("After that, the polymer of amino acids is folded, and then BAM! You have a protein!!!")
acids = ""
for i in range(len(mrna_codons)):
    codon = mrna_codons[i]
    acids += matcher.getAminoAcid(codon)
    if i != len(mrna_codons) - 1:
        acids += ", "
    if i == len(mrna_codons) - 2:
        acids += "and "
print("THE FINAL PRODUCT: " + acids)