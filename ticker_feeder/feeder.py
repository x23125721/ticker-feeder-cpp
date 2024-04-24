import feedparser

def fetch_animal_feeds(url):
    """
    Fetches and prints entries from an animal-related RSS feed.

    Args:
    url (str): The URL of the RSS feed.

    Returns:
    list of dict: A list containing the title and link of each entry.
    """
    # Parse the RSS feed
    feed = feedparser.parse(url)

    # List to hold the feed entries
    entries = []

    # Loop through the entries in the feed
    for entry in feed.entries:
        # Append the title and link of each entry to the list
        entries.append({
            'title': entry.title,
            'link': entry.link
        })
    
    return entries

# Example usage
if __name__ == "__main__":
    animal_feed_url = 'http://rss.com/animal-rss-feed'
    entries = fetch_animal_feeds(animal_feed_url)
    for entry in entries:
        print(f"Title: {entry['title']}\nLink: {entry['link']}\n")
