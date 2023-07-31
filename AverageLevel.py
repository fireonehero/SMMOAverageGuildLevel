import requests
import time
import json

api_key = 'api_key'
guild_id = 'guild_id'
api_endpoint = f'https://api.simple-mmo.com/v1/guilds/members/{guild_id}?api_key={api_key}'

# Initialize a variable for total level
total_level = 0

# Initialize a variable to count the number of players
player_count = 0

# Initialize a variable to track the number of requests
request_count = 0

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

# Get total number of players
response = requests.post(api_endpoint, data=json.dumps({'guildId': guild_id, 'apiKey': api_key}), headers=headers)
total_players = len(response.json()) # Change is here

while True:
    # If we have made 40 requests, sleep for a minute
    if request_count >= 40:
        time.sleep(60)
        request_count = 0

    response = requests.post(api_endpoint, data=json.dumps({'guildId': guild_id, 'apiKey': api_key}), headers=headers)
    data = response.json()

    # Iterate over each player
    for player in data: # And here
        # Convert the level to int (as it's string in the JSON) and add it to the total
        total_level += int(player['level'])
        player_count += 1

    # Increment the request count
    request_count += 1

    # Print progress and ETA
    progress = (player_count / total_players) * 100
    remaining_players = total_players - player_count
    eta = (remaining_players / 40) * 60  # as we can process 40 requests per minute
    print(f'Progress: {progress:.2f}% - ETA: {eta:.2f} seconds')

    # If all players have been processed, break the loop
    if player_count >= total_players:
        break

# Calculate the average level
average_level = total_level / player_count

print(f'The average level of the players is: {average_level}')
