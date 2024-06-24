from apify_client import ApifyClient

SECRET_API_KEY ="To retrieve via SubRosa"

def add_new_ig_username_to_actor(new_username):
    # Initialize the ApifyClient with your API token
    client = ApifyClient(SECRET_API_KEY)

    # Prepare the Actor input
    ig_username_link = f"https://www.instagram.com/{new_username}/"
    run_input = {
        "directUrls": [ig_username_link],
        "resultsType": "posts",
        "resultsLimit": 200,
        "searchType": "hashtag",
        "searchLimit": 1,
        "addParentData": False,
    }

    # Run the Actor and wait for it to finish
    # run = client.actor("RB9HEZitC8hIUXAha").call(run_input=run_input)
    print(f"Adding username: {new_username} to actor via: {run_input}")