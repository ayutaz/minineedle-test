from minineedle import needle, smith, core

def perform_alignment(seq1, seq2):
    alignment = needle.NeedlemanWunsch(seq1, seq2)
    alignment.align()
    score = alignment.get_score()
    identity = alignment.get_identity()
    
    print("Alignment of SEQUENCE 1 and SEQUENCE 2:")
    print(alignment)
    print("Score:", score)
    print("Identity:", identity)
    print()

# Test case 1: Short English sentences
seq1 = "The cat sat on the mat"
seq2 = "The dog sat on the rug"
perform_alignment(seq1, seq2)

# Test case 2: Longer English sentences
seq1 = "I love to eat pizza and pasta for dinner"
seq2 = "I enjoy eating sushi and ramen for lunch"
perform_alignment(seq1, seq2)

# Test case 3: Short Japanese sentences (Hiragana)
seq1 = "わたしはりんごがすきです"
seq2 = "わたしはバナナがすきです"
perform_alignment(seq1, seq2)

# Test case 4: Longer Japanese sentences (Hiragana and Kanji)
seq1 = "今日はいい天気です。散歩に行きましょう"
seq2 = "明日は雨が降るかもしれません。傘を持って行きましょう"
perform_alignment(seq1, seq2)

# Test case 5: Mixed English and Japanese sentences (Hiragana, Katakana, and Kanji)
seq1 = "I love to eat 寿司 and 天ぷら"
seq2 = "私は寿司とテンプラが大好きです"
perform_alignment(seq1, seq2)

# Test case 6: Japanese tongue twister (Hiragana and Katakana)
seq1 = "あめがあめあめあめがふるあめふるふるかあめてふるあめ"
seq2 = "アメガアメアメアメガフルアメフルフルカアメテフルアメ"
perform_alignment(seq1, seq2)

# Test case 7: Japanese proverb (Hiragana and Kanji)
seq1 = "猿も木から落ちる"
seq2 = "さるもきからおちる"
perform_alignment(seq1, seq2)