import random

def roll():
    minVal = 1
    maxVal = 6
    return random.randint(minVal, maxVal)


while True:
    players = input("Enter the number of players (2-4): \n")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("ERROR! Please enter a number between 2 and 4.")

maxScore = 50
playerScores = [0 for _ in range(players)]


while True:
    allPlayersPassed = True  

    for player in range(players):
        print(f"\nPlayer {player + 1}'s turn. Total score: {playerScores[player]}")

        currentScore = 0
        while True:
            shouldRoll = input("Roll? (y/n) \n")
            if shouldRoll.lower() != "y":
                break
            allPlayersPassed = False  

            value = roll()
            if value == 1:
                print("You rolled a 1! You lose your current score for this turn!")
                currentScore = 0
                break
            else:
                currentScore += value
                print(f"You rolled a {value}. Current turn score: {currentScore}")

        playerScores[player] += currentScore
        print(f"Player {player + 1}'s total score: {playerScores[player]}")

        
        if playerScores[player] >= maxScore:
            print(f"Player {player + 1} wins with a score of {playerScores[player]}!")
            exit()

    
    if allPlayersPassed:
        break


maxScore = max(playerScores)
winners = [i + 1 for i, score in enumerate(playerScores) if score == maxScore]

if len(winners) == 1:
    print(f"\nPlayer {winners[0]} wins with a score of {maxScore}!")
else:
    print(f"\nIt's a tie between players: {', '.join(map(str, winners))} with a score of {maxScore}!")
