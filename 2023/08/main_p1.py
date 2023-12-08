from collections import Counter

puzzle_input = "2023/inputs/07.txt"
#puzzle_input = "2023/inputs/07_sample.txt"

with open(puzzle_input) as f:
    lines = f.read().splitlines()

hands = []
for line in lines:
    aux = line.split(" ")
    hands.append([aux[0], int(aux[1])])


def is_more_valuable(card1, card2):

    ct1 = Counter(card1).values()
    ct2 = Counter(card2).values()

    # Five of a kind, where all five cards have the same label: AAAAA
    if len(ct1) < len(ct2):
        return True
    elif len(ct1) > len(ct2):
        return False
    elif max(ct1) > max(ct2):
        return True
    elif max(ct1) < max(ct2):
        return False
    
    # Cards have the same value so they need to be decided per character
    letter_order = ["A", "K", "Q", "J", "T"]
    for i in range(len(card1)):
        ch1 = card1[i]
        ch2 = card2[i]
        
        if ch1.isdigit() and ch2.isdigit():
            if int(ch1) > int(ch2):
                return True
            elif int(ch1) < int(ch2):
                return False
        
        elif ch1.isdigit() and ch2.isalpha():
            return False
        elif ch1.isalpha() and ch2.isdigit():
            return True
        
        else:
            if ch1 == "A" and ch2 != "A":
                return True
            elif ch1 != "A" and ch2 == "A":
                return False
            elif ch1 == "K" and ch2 != "K":
                return True
            elif ch1 != "K" and ch2 == "K":
                return False
            elif ch1 == "Q" and ch2 != "Q":
                return True
            elif ch1 != "Q" and ch2 == "Q":
                return False
            elif ch1 == "J" and ch2 != "J":
                return True
            elif ch1 != "J" and ch2 == "J":
                return False


ordered_hands = [hands[0]]
for hand in hands[1:]:
    if len(ordered_hands) == 1:
        if is_more_valuable(hand[0], ordered_hands[0][0]):
            ordered_hands.append(hand)
        else:
            ordered_hands.insert(0, hand)
    else:
        if not (is_more_valuable(hand[0], ordered_hands[0][0])):
            ordered_hands.insert(0, hand)
            break
        
        else:
            for i in range(1, len(ordered_hands)):

                if (i == len(ordered_hands) - 1):
                    if not (is_more_valuable(hand[0], ordered_hands[i][0])):
                        ordered_hands.insert(i, hand)
                        break
                    else:
                        ordered_hands.append(hand)
                        break
                
                elif not (is_more_valuable(hand[0], ordered_hands[i][0])):
                    ordered_hands.insert(i, hand)
                    break


# 32T3K, KTJJT, KK677, T55J5, QQQJA
#is_more_valuable("QQQJA", "KTJJT")

#for i in range(len(ordered_hands)):
#    if is_more_valuable("KK677", ordered_hands[i][0]):             
#        print(f"Hand KK677 is more valuable than {ordered_hands[i][0]}")

# calculate winnings
winnings = 0
for i in range(len(ordered_hands)):
    winnings = winnings + (i + 1) * ordered_hands[i][1]

print(f"What are the total winnings? Answer: {winnings}")

# Sample is 6440
# 106919 is too low