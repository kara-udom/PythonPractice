import requests
from bs4 import BeautifulSoup

def print_secret_message(doc_url):
    #get page content via url
    response = requests.get(doc_url)
    response.raise_for_status()

    #parse HTML
    soup = BeautifulSoup(response.text, "html.parser")
    #all table rows (each row has x, char, y)
    rows = soup.find_all("tr")

    points = []

    #loop through rows and extract data
    for row in rows:
        cols = row.find_all(["td", "th"])
        if len(cols) < 3:
            continue #skip if does not match the format

        values = [col.get_text(strip=True) for col in cols]

        try:
            #convert x y to integer
            x = int(values[0])
            char = values[1]
            y = int(values[2])
            #store
            points.append((x, y, char))
        except ValueError:
            #help ignore header row
            continue

    if not points:
        #if nothing was parsed, print empty
        print("")
        return

    max_x = max(x for x, _, _ in points)
    max_y = max(y for _, y, _ in points)
    
    # create grid filled with spaces
    grid = []
    for _ in range(max_y + 1):
        grid.append([" "] * (max_x + 1))

    # place each character into the grid
    for x, y, char in points:
        grid[y][x] = char
        
    # print the final result line by line
    for row in grid:
        print("".join(row))


print_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")