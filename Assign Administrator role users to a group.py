import requests
import json

# Set up the Okta API endpoint and authentication headers
okta_url = 'https://your-okta-domain.okta.com/api/v1'
api_token = 'your-api-token'
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'SSWS ' + api_token
}

# Define the Okta group ID
group_id = 'your-group-id'

# Get a list of all users in Okta
users_url = f"{okta_url}/users?limit=200"
users_response = requests.get(users_url, headers=headers)
users = json.loads(users_response.text)

# Debugging: Print the number of users in Okta
print(f"Found {len(users)} users in Okta")

# Get a list of all users in the Okta group
group_users_url = f"{okta_url}/groups/{group_id}/users"
group_users_response = requests.get(group_users_url, headers=headers)
group_users = json.loads(group_users_response.text)

# Debugging: Print the number of users in the Group
print(f"Found {len(group_users)} users in the Group")

# Loop through the users and add any user with "Admin" in their role name to the Okta group
for user in users:
    user_id = user['id']
    
    user_roles_url = f"{okta_url}/users/{user_id}/roles"
    user_roles_response = requests.get(user_roles_url, headers=headers)
    user_roles = json.loads(user_roles_response.text)

    for role in user_roles:
        if 'Administrator' in role['label']:
            # Check if the user is already a member of the group
            if any(group_user['id'] == user_id for group_user in group_users):
                print(f"User {user['profile']['login']} is already a member of group {group_id}")
            else:
                add_user_to_group_url = f"{okta_url}/groups/{group_id}/users/{user_id}"
                add_user_to_group_response = requests.put(add_user_to_group_url, headers=headers)
                if add_user_to_group_response.status_code == 204:
                    print(f"User {user['profile']['login']} added to group {group_id}")
                else:
                    print(f"Failed to add user {user['profile']['login']} to group {group_id}. Response code: {add_user_to_group_response.status_code}")

# Print a message indicating the program has completed
print("Program completed")
