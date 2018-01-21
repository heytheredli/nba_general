import random

p_team1_home = 0.7
p_team1_away = 0.4

final_prob_option1 = 0
final_prob_option2 = 0
for trial in range(1000000):
    game1 = random.randint(0,99)
    game2 = random.randint(0,99)
    game3 = random.randint(0,99)
    game4 = random.randint(0,99)
    game5 = random.randint(0,99)
    game6 = random.randint(0,99)
    game7 = random.randint(0,99)

    if game1 < 70:
        game1_outcome = 'win'
    else:
        game1_outcome = 'lose'

    if game2 < 70:
        game2_outcome = 'win'
    else:
        game2_outcome = 'lose'

    if game3 < 40:
        game3_outcome = 'win'
    else:
        game3_outcome = 'lose'

    if game4 < 40:
        game4_outcome = 'win'
    else:
        game4_outcome = 'lose'

    if game5 < 40:
        game5_outcome_option1 = 'win'
    else:
        game5_outcome_option1 = 'lose'
    if game5 < 70:
        game5_outcome_option2 = 'win'
    else:
        game5_outcome_option2 = 'lose'

    if game6 < 70:
        game6_outcome_option1 = 'win'
    else:
        game6_outcome_option1 = 'lose'
    if game6 < 40:
        game6_outcome_option2 = 'win'
    else:
        game6_outcome_option2 = 'lose'

    if game7 < 70:
        game7_outcome = 'win'
    else:
        game7_outcome = 'lose'

    option1_outcomes = [game1_outcome
                        , game2_outcome
                        , game3_outcome
                        , game4_outcome
                        , game5_outcome_option1
                        , game6_outcome_option1
                        , game7_outcome]
    option2_outcomes = [game1_outcome
                        , game2_outcome
                        , game3_outcome
                        , game4_outcome
                        , game5_outcome_option2
                        , game6_outcome_option2
                        , game7_outcome]

    # option 1: 2-3-2

    # 4 games
    if sum(1 if x == 'win' else 0 for x in option1_outcomes[:4]) == 4:
        final_prob_option1 += 1

    # 5 games
    elif sum(1 if x == 'win' else 0 for x in option1_outcomes[:5]) == 4:
        final_prob_option1 += 1

    # 6 games
    elif sum(1 if x == 'win' else 0 for x in option1_outcomes[:6]) == 4:
        final_prob_option1 += 1

    # 7 games
    elif sum(1 if x == 'win' else 0 for x in option1_outcomes) == 4:
        final_prob_option1 += 1


    # option 2: 2-2-1-1-1

    # 4 games
    if sum(1 if x == 'win' else 0 for x in option2_outcomes[:4]) == 4:
        final_prob_option2 += 1

    # 5 games
    elif sum(1 if x == 'win' else 0 for x in option2_outcomes[:5]) == 4:
        final_prob_option2 += 1

    # 6 games
    elif sum(1 if x == 'win' else 0 for x in option2_outcomes[:6]) == 4:
        final_prob_option2 += 1

    # 7 games
    elif sum(1 if x == 'win' else 0 for x in option2_outcomes) == 4:
        final_prob_option2 += 1


print final_prob_option1/1000000.0
print final_prob_option2/1000000.0
