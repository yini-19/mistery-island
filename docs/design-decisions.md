map: Beach → Jungle → Cave → Old Bridge → Lighthouse.
lantern and rope are found in cave

**Player state**
player = {'name': 'Ada', 'location': 'Beach', 'energy': 5, 'inventory': [], 'game_over': False, 'won': False}

**Suggested modules**
main.py — starts game and handles CLI input. 
game.py — functions such as new_game(), available_actions(), apply_action(player, action), is_win(player). 
tests/test_game.py — tests for pure game functions. Keep game logic testable without requiring interactive typing.
