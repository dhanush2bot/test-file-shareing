import random
import string
import requests
import os
from datetime import datetime, timedelta

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

# URL shortener API
SHORTENER_API = os.getenv("SHORTENER_API", "https://instantearn.in/")
API_KEY = os.getenv("API_KEY", "cb4c61dbfb6bc7b23011c6bb84fbc79e5a3fb105")
WEBSITE_NAME = os.getenv("WEBSITE_NAME", "InstantEarn")

# Generate a random token
def generate_token(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Verify the token
def verify_token(user_token, expected_token):
    return user_token == expected_token

# Task completion status for users
user_tasks = {}

# Premium users
premium_users = {}

# Function to handle user task completion
def complete_task(user_id, is_premium=False):
    # Generate a token for the user
    token = generate_token()
    # Store the token for verification later
    user_tasks[user_id] = {
        "token": token,
        "expiry_time": datetime.now() + timedelta(hours=12)
    }
    if is_premium:
        # Add premium user
        premium_users[user_id] = {
            "expiry_time": datetime.now() + timedelta(days=30)  # Example: Premium for 30 days
        }
    # Shorten the URL with the token
    short_url = shorten_url(token)
    # Return the shortened URL to the user
    return short_url

# Function to shorten URL with the token
def shorten_url(token):
    url = f"{SHORTENER_API}/api?url={SHORTENER_API}&apikey={API_KEY}"
    response = requests.post(url)
    if response.status_code == 200:
        return response.json()["shorturl"]
    else:
        return None

# Function to check if a user has completed the task
def has_completed_task(user_id):
    if user_id in user_tasks:
        return datetime.now() < user_tasks[user_id]["expiry_time"]
    else:
        return False

# Function to verify the user's token
def verify_user_token(user_id, user_token):
    if user_id in user_tasks:
        expected_token = user_tasks[user_id]["token"]
        if verify_token(user_token, expected_token):
            # User has completed the task successfully
            return True
    return False

# Function to check if a user is a premium user
def is_premium_user(user_id):
    if user_id in premium_users:
        return datetime.now() < premium_users[user_id]["expiry_time"]
    else:
        return False
