import requests
RIOT_API_KEY = "RGAPI-c019b7aa-ea6f-43ad-901c-2f3bc382872f"

queue = "RANKED_SOLO_5X5"
response = requests.get("https://na1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=RGAPI-c019b7aa-ea6f-43ad-901c-2f3bc382872f")


response_dict = response.json()

total_wins = 0
total_losses = 0
num_total = 0
for league_item in response_dict['entries']:
    if league_item['summonerName'].lower()[0] == 'a':
        total_wins += league_item['wins']
        total_losses += league_item['losses']
        num_total += 1

print(float(total_wins)/float(total_losses))
print(num_total)