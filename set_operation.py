if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    
    operation_count = int(input())
    
    for _ in range(operation_count):
        parts = input().split()
        
        if parts[0] == "pop":
            if s:   # prevent empty pop error
                s.remove(min(s))
        elif parts[0] == "remove":
            x = int(parts[1])
            if x in s:
                s.remove(x)
        elif parts[0] == "discard":
            s.discard(int(parts[1]))
    
    print(sum(s))