import os
import json
import time
import requests
import logging
from datetime import datetime

# Configuration
CONFIG_PATH = '/config/addons/onlyfans_watcher/config.json'
DOWNLOAD_PATH = '/config/www/onlyfans'
LOG_PATH = '/config/addons/onlyfans_watcher/logs.txt'

logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def send_notification(message):
    url = "http://homeassistant.local:8123/api/services/persistent_notification/create"
    headers = {
        "Authorization": f"Bearer {os.getenv('HA_TOKEN')}",
        "Content-Type": "application/json"
    }
    payload = {"message": message, "title": "OnlyFans Watcher"}
    requests.post(url, headers=headers, json=payload)

def download_new_posts():
    config = load_config()
    onlyfans_url = config['onlyfans_profile_url']
    
    # Simuler récupération de nouveaux posts (remplace avec un vrai scraping)
    new_posts = [{"id": "12345", "content": "https://example.com/image.jpg", "timestamp": str(datetime.now())}]
    
    for post in new_posts:
        post_folder = os.path.join(DOWNLOAD_PATH, str(post['id']))
        os.makedirs(post_folder, exist_ok=True)
        
        image_path = os.path.join(post_folder, 'image.jpg')
        with open(image_path, 'wb') as img:
            img.write(requests.get(post['content']).content)
        
        logging.info(f"Downloaded post {post['id']}")
        send_notification(f"New post downloaded: {post['id']}")
    
    time.sleep(300)  # Attendre 5 min avant de vérifier à nouveau

if __name__ == "__main__":
    while True:
        download_new_posts()
