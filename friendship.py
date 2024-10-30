users = [
    {"id": 0, "name": "Thando"},
    {"id": 1, "name": "Basi"},
    {"id": 2, "name": "Xoli"},
    {"id": 3, "name": "Loyd"},
    {"id": 4, "name": "Sivene"},
    {"id": 5, "name": "Mzi"},
    {"id": 6, "name": "Bash"},
    {"id": 7, "name": "Avela"},
    {"id": 8, "name": "Sine"},
    {"id": 9, "name": "Zuko"}
]


friendship_pairs = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),\
                   (6,8),(7,8),(8,9)]

# Initialize a dict with an emptylist for each user id:

friendships  = {user["id"]:[] for user in users}

#loop through the friendship pairs to populate it:

for i, j in friendship_pairs:
    friendships[i].append(j) #add j as a friend of user i
    friendships[j].append(i) #add i as a friend of user j

# find total number of connections

def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user  in users) #24

num_users = len(users)
avg_connections = total_connections / num_users

# Create a list  (user_id, number_of_friends).

number_of_friends_by_id = [(user["id"], number_of_friends(user))\
                            for user in users]
number_of_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],\
    reverse=True) # sort the list (largest to smallest)

# Establish more connections (uses may know friends of their friends)

def faof_ids_bad(user):
    """foaf = friends pf a friend"""
    return [foaf_id\
            for friend_id in friendships[user["id"]]\
            for foaf_id in friendships[friend_id]]

print(friendships[0])

# A count of  mutual friends excluding people already known  to the user
from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]  # for each of my friend
        for foaf_id in friendships[friend_id]  # find their friend
        if foaf_id != user_id                  # who aren't me
        and foaf_id not in friendships[user_id] # and aren't my friends.
    )

print(friends_of_friends(users[3])) # Loyd has 2 mutual friends with Thando and 1 mutual friend with Mzi.

# users and their interests

interests  = [
    (0, "Dancing"), (0, "Singing"), (0, "Sleeping"), (0, "Swimming"), 
    (0, "Journaling"), (0, "Gym"), (0, "Playing"), 
    (1, "Mathematics"), (1, "Soccer"), (1, "Jumping"), (1, "Probability"), 
    (1, "Playing"), (2, "Jumping"), (2, "Learning"), (2, "Reading"), 
    (2, "Writting"), (2, "Dancing"), (2, "Mathematics"), (3, "Rugby"), (3, "Soccer"), 
    (3, "Playing"), (3, "Singing"), (3, "Gym"), 
    (4, "Learning"), (4, "Gym"), (4, "Sleeping"), 
    (4, "Reading"), (5, "Singing"), (5, "Reading"), (5, "Gym"), (5, "Dancing"), 
    (5, "Bowling"), (5, "Journaling"), (6, "Sleeping"), 
    (6, "Probability"), (6, "Mathematics"), (6, "Jumping"), 
    (7, "Learning"), (7, "Rugby"), (7, "Mathematics"), 
    (7, "Writting"), (8, "Singing"), (8, "Learning"), 
    (8, "Swimming"), (8, "Swimming"), (9, "Jumping"), 
    (9, "Rugby"), (9, "Gym"), (9, "Soccer")
]

def friends_who_like(target_interest):
    """find the ids  of all users who like the target interes."""
    return[user_id
           for user_id, user_interest in interests
           if user_interest == target_interest]

from collections import defaultdict

# Keys are interests, values are lists os user_ids with that interest

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# keys are user_ids, values are lists of interests for that  user_id.

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interest_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]] # Iterate over interests of the user
        for interested_user_id in user_ids_by_interest[interest] # Find users with the same interest
        if interested_user_id != user["id"] # Exclude the original user
    )
user = {"id": 0}
#result = most_common_interest_with(user, interests_by_user_id, user_ids_by_interest)
print(most_common_interest_with)