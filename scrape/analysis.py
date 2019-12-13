import json

with open('results.json', 'r') as fp:
    results = json.load(fp)

    marginals = []
    worst = 1
    arg_worst = ()
    left_tot = 0
    right_tot = 0
    left_lost = 0
    right_lost = 0
    left_same = 0
    right_same = 0
    left_marg = 0
    right_marg = 0
    
    for constit in results.values():
        total = 0
        best = 0
        argbest = ''
        left = 0
        right = 0
        title = constit['title']
        for party in constit.keys():
            total += int(vote)
            if int(vote) > best:
                best = int(vote)
                argbest = party

            party = constit[vote][0]
            if party == 'Labour' or party == 'Liberal Democrat' or party == 'Green':
                left += num
            if party == 'Conservative' or party == 'The Brexit Party':
                right += num

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
            if left / total <= .5:
                left_marg += 1
            if partyb == 'Conservative' or partyb == 'The Brexit Party':
                right_lost += 1
            elif partyb == 'Labour' or partyb == 'Liberal Democrat' or partyb == 'Green':
                left_same += 1
            else:
                print('left from {}'.format(partyb))

        if right > left and right >= best:
            right_tot += 1
            if right / total <= .5:
                right_marg += 1
            if partyb == 'Labour' or partyb == 'Liberal Democrat' or partyb == 'Green':
                left_lost += 1
            elif partyb == 'Conservative' or partyb == 'The Brexit Party':
                right_same += 1
            else:
                print('right from {}'.format(partyb))

    print("marginal seats: " + len(marginals))
    print("left: {} right: {}".format(left_tot, right_tot))
    print("left_lost: {} right_lost: {}".format(left_lost, right_lost))
    print("left_same: {} right_same: {}".format(left_same, right_same))

