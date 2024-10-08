from utils.search import search_podcasts

def main():
    print("Welcome to Podcast Finder!")
    person_name = input("Enter the person's name to search for podcasts: ")
    
    # Fetch results from Spotify and YouTube
    results = search_podcasts(person_name)
    
    # Display Spotify results
    print("\nSpotify Results:")
    for item in results['spotify']['episodes']['items']:
        print(f"{item['name']} - {item['release_date']}")
        print(f"Link: {item['external_urls']['spotify']}\n")

    # Display YouTube results
    print("YouTube Results:")
    for item in results['youtube']['items']:
        # Check if 'id' and 'videoId' exist in the response
        if 'id' in item and 'videoId' in item['id']:
            print(f"Podcast: {item['snippet']['title']} - {item['snippet']['publishedAt']}")
            print(f"Link: https://youtube.com/watch?v={item['id']['videoId']}\n")
        else:
            print(f"Podcast: {item['snippet']['title']} - {item['snippet']['publishedAt']}")
            print("No video link available for this item.\n")

if __name__ == "__main__":
    main()
