# Pattern:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def number_repeated_pattern(n):
    for i in range(1, n+1):  # Loop for each row
        print(' '.join(str(i)*i))
        #print(' '.join([str(i)] * i))


number_repeated_pattern(5)
