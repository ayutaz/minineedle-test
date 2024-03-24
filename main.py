from minineedle import needle, smith, core

# Use miniseq objects
# Load sequences as miniseq FASTA object
import miniseq
# fasta = miniseq.FASTA(filename="myfasta.fa")
# seq1, seq2 = fasta[0], fasta[1]

# Or use strings, lists, etc
seq1, seq2 = "ACTG", "ATCTG"
seq3, seq4 = ["A","C","T","G"], ["A","T","C","T","G"]

# Create the instance
alignment: needle.NeedlemanWunsch[str] = needle.NeedlemanWunsch(seq1, seq2)
alignment1: needle.NeedlemanWunsch[str] = needle.NeedlemanWunsch(seq3, seq4)
# or
# alignment smith.SmithWaterman[str] = smith.SmithWaterman(seq1, seq2)

# Make the alignment
alignment.align()

# Get the score
score1 = alignment.get_score()
score2 = alignment1.get_score()
print(score1,",",score2)

# Get the sequences aligned as lists
al1, al2 = alignment.get_aligned_sequences(core.AlignmentFormat.list) # or "list"

# Get the sequences as strings
al1, al2 = alignment.get_aligned_sequences(core.AlignmentFormat.str) # or "str

# Change the matrix and run again
alignment.change_matrix(core.ScoreMatrix(match=4, miss=-4, gap=-2))
alignment.align()

# Print the sequences aligned
print(alignment)

# Change gap character
alignment.gap_character = "-gap-"
print(alignment)

# Sort a list of alignments by score
first_al  = needle.NeedlemanWunsch(seq1, seq2)
second_al = needle.NeedlemanWunsch(seq3, seq4)

for align in sorted([first_al, second_al], reverse=True):
    print(align)
