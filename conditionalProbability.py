def conditional():
    pass_stats=0.15
    pass_codingWStats=0.60
    pass_codingW0Stats=0.40

    prob_both= pass_stats * pass_codingWStats

    print("The probability that appilcant passes both is",round(prob_both,3))

    prob_coding=(prob_both)+((1-pass_stats)*pass_codingW0Stats)

    print("Probability that he/ she passes only coding is",round(prob_coding,3))

    stats_given_coding=prob_both/prob_coding

    print("Conditional probability is", round(stats_given_coding,3))

print("Hey New")
conditional()