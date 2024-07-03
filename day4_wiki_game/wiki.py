import requests
from bs4 import BeautifulSoup
import time

def get_first_link(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the main content of the article
    content_div = soup.find(id='mw-content-text')
    
    # Ignore IPA, pronunciations, and citation links
    for span in content_div.find_all(['span', 'sup']):
        span.decompose()
    
    # Ignore links within parentheses
    for parenthesis in content_div.find_all(string=lambda text: '(' in text and ')' in text):
        if parenthesis.find_parent('a'):
            parenthesis.find_parent('a').decompose()
    
    # Get the first valid link
    for link in content_div.find_all('a', href=True):
        href = link['href']
        if (href.startswith('/wiki/') and 
            not href.startswith('/wiki/Help:') and 
            not href.startswith('/wiki/Wikipedia:') and 
            not href.startswith('/wiki/Template:')):
            return 'https://en.wikipedia.org' + href
    return None

def follow_links(start_url, max_jumps=100):
    visited = set()
    current_url = start_url
    steps = 0
    
    while current_url and steps < max_jumps:
        if current_url in visited:
            print(f"Loop detected at {current_url}.")
            break
        visited.add(current_url)
        print(f"Step {steps + 1}: {current_url}")
        
        next_url = get_first_link(current_url)
        if not next_url:
            print(f"Dead end reached at {current_url}.")
            break
        
        current_url = next_url
        steps += 1
        time.sleep(1)  # To prevent overwhelming the server
    
    if steps >= max_jumps:
        print("Maximum number of jumps reached.")

# Start with a random Wikipedia page
start_url = 'https://en.wikipedia.org/wiki/cricket'
follow_links(start_url)
