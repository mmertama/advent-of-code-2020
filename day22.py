example = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''

example0 = '''Player 1:
43
19

Player 2:
2
29
14'''

def make_game(data):
    game = {}
    current_player = None
    current_deck = []
    for line in data:
        if len(line) == 0:
            current_deck.reverse()
            game[current_player] = current_deck
            current_player = None
            current_deck = []
        elif current_player is None:
            current_player = line
        else:
            current_deck.append(int(line.strip()))
    current_deck.reverse()
    game[current_player] = current_deck
    return game


def game_declare_winner(player, deck, rounds):
    score = 0
    for i in range(0, len(deck)):
        score += (i + 1) * deck[i]
    print("Round 1:", player, "has won, on round:", rounds, ", score:", score)


def play_space_cards(data):
    game = make_game(data)
    rounds = 0
    players = list(game.keys())
    player1 = players[0]
    player2 = players[1]
    deck1 = game[player1]
    deck2 = game[player2]
    while True:
        rounds += 1
        c1 = deck1.pop()
        c2 = deck2.pop()
        if c1 > c2:
            deck1.insert(0, c1)
            deck1.insert(0, c2)
        elif c2 > c1:
            deck2.insert(0, c2)
            deck2.insert(0, c1)
        else:
            deck2.insert(0, c2)
            deck1.insert(0, c1)
        if len(deck1) == 0:
            break
        if len(deck2) == 0:
            break

    if len(deck2) == 0:
        game_declare_winner(player1, deck1, rounds)
    else:
        game_declare_winner(player2, deck2, rounds)


def has_previous(current_deck, history, player):
    size = len(current_deck)
    signature = ''.join(str(x) for x in current_deck)
    if size in history[player]:
        if signature in history[player][size]:
            return True
        history[player][size].add(signature)
    else:
        history[player][size] = {signature}
    return False


def play_space_cards_recursive(data):
    game = make_game(data)
    players = list(game.keys())
    player1 = players[0]
    player2 = players[1]
    deck1 = game[player1]
    deck2 = game[player2]
    results = {}
    winner, deck, rounds = play_game((player1, deck1), (player2, deck2), 1, results)
    game_declare_winner(winner, deck, rounds)


def make_sig(deck1, deck2):
    return str(len(deck1)) + '_' + str(len(deck2)) + '_' + ''.join(str(x) for x in deck1) + ''.join(
        str(x) for x in deck1)


def join(results, games, winner):
    for g in games:
        #assert g not in results
        results[g] = winner


def play_game(p1, p2, sub_game, results):
    rounds = 0
    player1 = p1[0]
    player2 = p2[0]
    deck1 = [x for x in p1[1]]
    deck2 = [x for x in p2[1]]
    history = {player1: {}, player2: {}}
    games = set()
    while True:
        rounds += 1
        signature = make_sig(deck1, deck2)
        if signature in results:
            #print("on loop", len(results), sub_game)
            join(results, games, results[signature])
            return results[signature], deck1, rounds
        games.add(signature)
        if has_previous(deck1, history, player1):
            join(results, games, player1)
            return player1, deck1, rounds
        if has_previous(deck2, history, player2):
            join(results, games, player2)
            return player1, deck1, rounds
        c1 = deck1.pop()
        c2 = deck2.pop()
        if c1 <= len(deck1) and c2 <= len(deck2):
            signature = make_sig(deck1, deck2)
            if signature in results:
                #print("on sub", len(results), sub_game)
                sub_winner = results[signature]
            else:
                sub_winner, _, _ = play_game((player1, deck1), (player2, deck2), sub_game + 1, results)
                results[signature] = sub_winner
            if sub_winner == player1:
                deck1.insert(0, c1)
                deck1.insert(0, c2)
            else:
                deck2.insert(0, c2)
                deck2.insert(0, c1)
        else:
            if c1 > c2:
                deck1.insert(0, c1)
                deck1.insert(0, c2)
            elif c2 > c1:
                deck2.insert(0, c2)
                deck2.insert(0, c1)
            else:
                deck2.insert(0, c2)
                deck1.insert(0, c1)
        if len(deck1) == 0:
            break
        if len(deck2) == 0:
            break

    signature = make_sig(deck1, deck2)
    if len(deck2) == 0:
        results[signature] = player1
        join(results, games, player1)
        return player1, deck1, rounds
    else:
        results[signature] = player2
        join(results, games, player2)
        return player2, deck2, rounds







