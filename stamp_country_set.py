if __name__ == '__main__':
    n = int(input())
    country_stamp = set()
    
    for _ in range(n):
        country = input()
        country_stamp.add(country)
    
    print(len(country_stamp))