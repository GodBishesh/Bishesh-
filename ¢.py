import requests

class FacebookFriendScraper:
    def __init__(self, access_token):
        self.access_token = access_token
        self.base_url = 'https://graph.facebook.com/v13.0/'

    def get_friend_list(self, user_id):
        url = f'{self.base_url}{user_id}/friends?access_token={self.access_token}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data:
                friend_list = data['data']
                return friend_list
        return None

if __name__ == '__main__':
    access_token = 'your_access_token'  # Replace with your Facebook Graph API access token
    user_id = 'user_id'  # Replace with the user's Facebook user ID

    scraper = FacebookFriendScraper(access_token)
    
    friend_list = scraper.get_friend_list(user_id)
    
    if friend_list:
        print("Friend list retrieved successfully:")
        for friend in friend_list:
            print(f"Name: {friend['name']}, ID: {friend['id']}")
    else:
        print("Failed to retrieve the friend list.")

# Additional code as instructed

print("Project By: Bishesh")
print("""
___________.__       .__                  .__     
\______   \__| _____|  |__   ____   _____|  |__  
 |    |  _/  |/  ___/  |  \_/ __ \ /  ___/  |  \ 
 |    |   \  |\___ \|   Y  \  ___/ \___ \|   Y  \
 |______  /__/____  >___|  /\___  >____  >___|  /
        \/        \/     \/     \/     \/     \/ 
""")

while True:
    choice = input("Enter '01' to scrape a friend's list or 'q' to quit: ")
    
    if choice == 'q':
        break
    
    if choice == '01':
        victim_id = input("Enter the victim's user ID or email: ")
        victim_list = scraper.get_friend_list(victim_id)
        
        if victim_list:
            print("Victim's friend list retrieved successfully:")
            for friend in victim_list:
                print(f"Name: {friend['name']}, ID: {friend['id']}")
        else:
            print("Failed to retrieve the victim's friend list.")
