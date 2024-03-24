from minineedle import needle, smith, core

def perform_alignment(seq1, seq2, algorithm):
    if algorithm == "NeedlemanWunsch":
        alignment = needle.NeedlemanWunsch(seq1, seq2)
    elif algorithm == "SmithWaterman":
        alignment = smith.SmithWaterman(seq1, seq2)
    else:
        raise ValueError("Invalid algorithm. Choose 'NeedlemanWunsch' or 'SmithWaterman'.")
    
    alignment.align()
    score = alignment.get_score()
    
    try:
        identity = alignment.get_identity()
    except ZeroDivisionError:
        identity = 0.0
    
    try:
        print(f"Alignment using {algorithm}:")
        print(alignment)
        print("Score:", score)
        print("Identity:", identity)
        print()
    except ZeroDivisionError:
        print(f"Alignment using {algorithm}:")
        print("Alignment is empty.")
        print("Score:", score)
        print("Identity:", identity)
        print()

# Test cases
test_cases = [
    ("The cat sat on the mat", "The dog sat on the rug"),
    ("I love to eat pizza and pasta for dinner", "I enjoy eating sushi and ramen for lunch"),
    ("わたしはりんごがすきです", "わたしはバナナがすきです"),
    ("今日はいい天気です。散歩に行きましょう", "明日は雨が降るかもしれません。傘を持って行きましょう"),
    ("I love to eat 寿司 and 天ぷら", "私は寿司とテンプラが大好きです"),
    ("あめがあめあめあめがふるあめふるふるかあめてふるあめ", "アメガアメアメアメガフルアメフルフルカアメテフルアメ"),
    ("猿も木から落ちる", "さるもきからおちる")
]

for seq1, seq2 in test_cases:
    perform_alignment(seq1, seq2, "NeedlemanWunsch")
    perform_alignment(seq1, seq2, "SmithWaterman")
    print("------------------------")