def gap(g, m, n):
    import math
    previous = None
    for num in range(m, n + 1):
        prime = True
        for divisor in range(2, int(math.sqrt(num)+1)):
            if num % divisor == 0:
                prime = False
                break
        if prime == False:
            continue
        if previous == None:
            previous = num
            continue
        if num - previous == g:
            return [previous, num]
        previous = num
