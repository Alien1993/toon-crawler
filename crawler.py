import wikipedia

def crawl():
    # Here we set the starting page to crawl
    start_page = wikipedia.page("Looney Tunes and Merrie Melodies filmography")

    # Get all links to pages listing filmographies per year
    filmography_links = [l for l in start_page.links if "filmography" in l]

    # These are words that might help me find what I'm searching for
    magic_words = [
            'barn',
            'windmill',
            'mill',
            'fireflies',
            'firefly',
            'ligthbulb',
            'bulb',
            'insect',
            'dawn',
            'sunset',
    ]

    results = set()

    # Loops all the pages found and tries to find at least one of the magic words
    for link in filmography_links:
        page = wikipedia.page(link)

        for word in magic_words:
            if word in page.content:
                results.add(page.url)

    return results

if __name__ == "__main__":
    pages_found = crawl()
    if len(pages_found) > 0:
        print(pages_found)
    else:
        print("Nothing found")
