import json

with open('results.json', 'r') as fp:
    results = json.load(fp)

    marginals = []
    worst = 1
    arg_worst = ()
    left_tot = 0
    right_tot = 0
    
    for constit in results.values():
        total = 0
        best = 0
        argbest = ''
        left = 0
        right = 0
        title = constit['title']
        for vote in constit.keys():
            if not vote.isdigit():
                continue

            party = constit[vote][0]
            total += int(vote)
            if int(vote) > best:
                best = int(vote)
                argbest = party

            if party == 'Labour' or party == 'Liberal Democrat' or party == 'Green':
                left += int(vote)
            if party == 'Conservative' or party == 'The Brexit Party':
                right += int(vote)

        percentb = best / total
        partyb = constit[str(best)][0]
        nameb = constit[str(best)][1]
        if percentb <= .5:

            marginal = (partyb, percentb, title, nameb)
            marginals.append(marginal)

            if percentb < worst:
                worst = percentb
                arg_worst = marginal

        if left > right and left >= best:
            left_tot += 1
        if right > left and right >= best:
            right_tot += 1

    print("marginal seats: {}".format(len(marginals)))
    print("left: {} right: {}".format(left_tot, right_tot))
