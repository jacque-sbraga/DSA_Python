s = set("Hacker")
print(s.union("Rank"))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

print(s.union(set(['R', 'a', 'n', 'k'])))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

print(s.union(['R', 'a', 'n', 'k']))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

print(s.union(enumerate(['R', 'a', 'n', 'k'])))
set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

print(s.union({"Rank":2}))
set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

s | set("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])