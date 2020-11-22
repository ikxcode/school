import random


class DiceRoller:
    @staticmethod
    def roll_single():
        return random.randint(1, 6)

    @staticmethod
    def roll():
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        bonus_throw = random.randint(1, 6)
        return DiceRoller.score(dice_1, dice_2, bonus_throw)

    @staticmethod
    def score(dice_1, dice_2, bonus_throw=0):
        score = dice_1 + dice_2
        print(score)
        odd_or_even = score % 2

        if odd_or_even == 1:
            print("You rolled an odd number! You lose 5 points!")
            score -= 5
            print(score)
        else:
            print("You rolled an even number! You win 10 points!")
            score += 10
            print(score)
            if dice_1 == dice_2:
                print("You rolled a double!")
                print("You get " + str(bonus_throw) + " extra points!")
                score += bonus_throw
                print(score)

        if score < 0:
            score = 0
        return score
