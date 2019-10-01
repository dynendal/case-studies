import difflib

#possibilities is a shortened list of a network-reachable file with a list of all possible aliases.
possibilities = ['ab2-flux', 'ab2-texture', 'ab2-fx']
wanted = 'Team Flux'

wanted = tuple(wanted.lower().split(' '))

matcher = lambda x: difflib.get_close_matches(x, possibilities)

print([matcher(match) for match in wanted if matcher(match)])
