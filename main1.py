from minineedle import needle, smith, core

seq1, seq2 = "ACTG", "ATCTG"
seq3, seq4 = ["A","C","T","G"], ["A","T","C","T","G"]

alignment1: needle.NeedlemanWunsch[str] = needle.NeedlemanWunsch(seq1, seq2)
alignment2: needle.NeedlemanWunsch[str] = needle.NeedlemanWunsch(seq3, seq4)

alignment1.align()
alignment2.align()

score1 = alignment1.get_score()
score2 = alignment2.get_score()

identity1 = alignment1.get_identity()
identity2 = alignment2.get_identity()

print("Alignment of SEQUENCE 1 and SEQUENCE 2:")
print(alignment1)
print("Score:", score1)
print("Identity:", identity1)

print("Alignment of SEQUENCE 3 and SEQUENCE 4:")
print(alignment2)
print("Score:", score2)
print("Identity:", identity2)