from sys import stdin as st


set1 = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
ans = set1 - {x.upper() for x in st.read()[:-8] if x.isalpha()}

print(*sorted(ans)) if ans else print('NONE')
