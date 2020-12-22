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
    print(deck[::-1])
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
            if len(deck2) == 0:
                break
        else:
            deck2.insert(0, c2)
            deck2.insert(0, c1)
            if len(deck1) == 0:
                break
        # assert c2 != c1 # There are no same cards

    if len(deck2) == 0:
        game_declare_winner(player1, deck1, rounds)
    else:
        game_declare_winner(player2, deck2, rounds)


def in_previous(history, deck1, deck2):
    signature = ','.join(
        str(x) for x in deck1) + '_' + ','.join(
        str(x) for x in deck2)
    if signature in history:
        return True
    else:
        history.add(signature)
    return False


def play_space_cards_recursive(data):
    game = make_game(data)
    players = list(game.keys())
    player1 = players[0]
    player2 = players[1]
    deck1 = game[player1]
    deck2 = game[player2]
    winner, deck, rounds = play_game((player1, deck1), (player2, deck2))
    game_declare_winner(winner, deck, rounds)


def play_game(p1, p2):
    rounds = 0
    player1 = p1[0]
    player2 = p2[0]
    deck1 = [x for x in p1[1]]
    deck2 = [x for x in p2[1]]
    history = set()
    while True:
        rounds += 1
        if in_previous(history, deck1, deck2):
            return player1, deck1, round
        c1 = deck1.pop()
        c2 = deck2.pop()
        l1 = len(deck1)
        l2 = len(deck2)
        if l1 >= c1 and l2 >= c2:
            sub_winner, _, _ = play_game(
                (player1, deck1[-c1:]), (player2, deck2[-c2:]))
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
            else:
                deck2.insert(0, c2)
                deck2.insert(0, c1)
        # assert c2 != c1 # There are no same cards
        if len(deck1) == 0 or len(deck2) == 0:
            break

    if len(deck2) == 0:
        return player1, deck1, rounds
    else:
        assert len(deck1) == 0
        return player2, deck2, rounds




