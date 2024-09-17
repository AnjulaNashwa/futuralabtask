var = "anjulaarunnashwa"
start = 0
max_length = 0
used_chars = {}
for i in range(len(var)):
    if var[i] in used_chars and start <= used_chars[var[i]]:
        start = used_chars[var[i]] + 1
    else:
        max_length = max(max_length, i - start + 1)

    used_chars[var[i]] = i

print(max_length)
