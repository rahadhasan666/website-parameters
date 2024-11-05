# Save this as dx.py

import urllib.parse

def main():
    print("Dark World")
    print("Creator: Rahad Hasan")
    print("Please paste the website URL:")

    # Get URL from user input
    url = input("> ").strip()

    # Parse the URL and extract parameters
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)

    if query_params:
        print("\nExtracted Parameters:")
        for param, values in query_params.items():
            print(f"{param}: {', '.join(values)}")
    else:
        print("\nNo parameters found in the URL.")

if __name__ == "__main__":
    main()
