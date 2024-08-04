import urllib.request
import json
import re

# Function to perform a search using Wikipedia API
def wikipedia_search(query):
    api_url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'list': 'search',
        'srsearch': query,
        'format': 'json'
    }
    url = api_url + '?' + urllib.parse.urlencode(params)

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            res = response.read().decode('utf-8')
            result = json.loads(res)
            return result.get('query', {}).get('search', [])
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
    except Exception as e:
        print(f"Error: {str(e)}")
    return []

# Function to strip HTML tags from a string
def strip_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Define the chatbot function
def chatbot():
    print("Hello! I'm your Wikipedia chatbot. Ask me anything, and I'll try to find the answer.")
    while True:
        user_input = input("\nYou: ")

        # Exit the chatbot
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break

        # Perform a search using Wikipedia
        print("Searching Wikipedia...")
        results = wikipedia_search(user_input)

        # Print the results
        if results:
            print("Here are some results:")
            for result in results:
                title = result['title']
                snippet = strip_html_tags(result['snippet'])
                print(f"- {title}: {snippet}")
        else:
            print("No results found.")

        print("\nAsk another question or type 'exit', 'quit', or 'bye' to end the chat.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
