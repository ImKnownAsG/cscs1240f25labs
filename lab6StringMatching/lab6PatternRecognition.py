def compute_lps_array(pattern):
    print(f"Building LPS array for pattern: '{pattern}'")
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix
    i = 1

    while i < len(pattern):
        print(f"  i={i}, length={length}, comparing pattern[{i}]='{pattern[i]}' with pattern[{length}]='{pattern[length]}'")
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            print(f"    Match! lps[{i}] = {length}")
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
                print(f"    Mismatch. Backtrack length to {length}")
            else:
                lps[i] = 0
                print(f"    Mismatch. Set lps[{i}] = 0")
                i += 1

    print(f"LPS array complete: {lps}\n")
    return lps

def kmp_search(text, pattern):
    print(f"Searching for pattern '{pattern}' in text '{text}'\n")
    lps = compute_lps_array(pattern)

    i = 0  # index for text
    j = 0  # index for pattern

    match_positions = []

    while i < len(text):
        print(f"Text[{i}] = '{text[i]}', Pattern[{j}] = '{pattern[j]}'")

        if pattern[j] == text[i]:
            i += 1
            j += 1
            print(f"  Characters match! Move both pointers: i={i}, j={j}")
        else:
            if j != 0:
                j = lps[j - 1]
                print(f"  Mismatch. Reset j using lps: j={j}")
            else:
                i += 1
                print(f"  Mismatch and j=0. Move i to {i}")

        if j == len(pattern):
            print(f"  >> Match found at index {i - j} <<\n")
            match_positions.append(i - j)
            j = lps[j - 1]  # prepare for next match

    if not match_positions:
        print("No matches found.")
    return match_positions


text = "ABABDABACDABABCABAB"
#text = "BABCABABABABDABACD"
pattern = "ABABCABAB"


positions = kmp_search(text, pattern)
print("Pattern found at indices:", positions)
