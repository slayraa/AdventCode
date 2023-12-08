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

    og1 = card1
    og2 = card2

    #Correct card values with Jokers
    if "J" in card1:
        max_type = Counter(card1).most_common(1)[0][0]
        if (max_type == "J") and (card1 != "JJJJJ"):
            max_type = Counter(card1).most_common()[1][0]
        card1 = card1.replace("J", max_type)
    
    if "J" in card2:
        max_type = Counter(card2).most_common(1)[0][0]
        if (max_type == "J") and (card2 != "JJJJJ"):
            max_type = Counter(card2).most_common()[1][0]
        card2 = card2.replace("J", max_type)
        
    ct1 = Counter(card1).values()
    ct2 = Counter(card2).values()

    # Check the values of the cards
    if len(ct1) < len(ct2):
        return True
    elif len(ct1) > len(ct2):
        return False
    elif max(ct1) > max(ct2):
        return True
    elif max(ct1) < max(ct2):
        return False
    
    # If cards have the same value the winner depends on characters
    for i in range(len(card1)):
        ch1 = og1[i]
        ch2 = og2[i]

        if ch1 != ch2:

            if ch1 == "J":
                return False
            elif ch2 == "J":
                return True   
            
            if ch1.isdigit() and ch2.isdigit():
                return (int(ch1) > int(ch2))
            
            elif ch1.isdigit() and ch2.isalpha():
                return False
            
            elif ch1.isalpha() and ch2.isdigit():
                return True
            
            else:
                if ch1 == "A":
                    return True
                elif ch1 != "A" and ch2 == "A":
                    return False
                elif ch1 == "K":
                    return True
                elif ch1 != "K" and ch2 == "K":
                    return False
                elif ch1 == "Q":
                    return True
                elif ch1 != "Q" and ch2 == "Q":
                    return False
                elif ch1 == "T":
                    return True
                elif ch1 != "T" and ch2 == "T":
                    return False


ordered_hands = [hands[0]]
for hand in hands[1:]:
    #print(hand)
    if len(ordered_hands) == 1:
        if is_more_valuable(hand[0], ordered_hands[0][0]):
            ordered_hands.append(hand)
        else:
            ordered_hands.insert(0, hand)
    else:
        if not (is_more_valuable(hand[0], ordered_hands[0][0])):
            ordered_hands.insert(0, hand)
        
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

# calculate winnings
winnings = 0
for i in range(len(ordered_hands)):
    winnings = winnings + (i + 1) * ordered_hands[i][1]

print(f"What are the total winnings? Answer: {winnings}")

# Sample is 5905
# 254494947
