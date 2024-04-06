# run_main.py
import json
import time
import re
import sys
import pandas as pd
from test8 import get_response

usernames = ['user1', 'user2', 'user3', 'chiragsharma']

# Load balances from CSV
df = pd.read_csv('balances.csv')
username1 = ""
username2 = ""
amount = 0
authorization_code = ""
auth_flag = False

while True:
    user_message = input("Enter your message: ")
    while True:
        try:        
            response = get_response(usernames, user_message)
            response_dict = json.loads(response)
            intent = response_dict['Intent'].lower()  # Convert the intent to lowercase
            username = response_dict['Creds']['username']
            if intent == 'greetings':
                if username in usernames:
                    print(f'Hi {username}, how may I help you?')
                    username1 = username
                else:
                    print('Hi! please tell your username')
            elif username1 != "":
                auth = input("Please enter your authorization code: ")
                if df.loc[df['username'] == username1, 'username'].values[0] == auth:
                    if intent == 'check balance':
                        if username1 in usernames:
                            balance = df.loc[df['username'] == username1, 'amount'].values[0]
                            print(f'Your current balance is {balance}.')
                        else:
                            print('Username not found.')
                    elif intent == 'transfer money' and username in usernames:
                        print(username)
                        username2 = username
                        # Extract the integer from the user message
                        numbers = re.findall(r'\d+', user_message)
                        if numbers:
                            print(numbers[0])  # Print the first number found in the user message
                            amount = numbers[0]
                else:
                    print('Invalid Authorization Code! Please restart the server.')
            break
        except Exception as e:
            print(f"An error occurred while running main.py: {e}. Retrying...")
            time.sleep(5)  # Optional: wait for 5 seconds before retrying
