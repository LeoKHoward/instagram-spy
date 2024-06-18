import os
from bs4 import BeautifulSoup


def load_html_content(file_path):
    """Load and return the HTML content from a file"""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def extract_usernames_from_html(html_content):
    """Extract usernames from the given HTML content"""
    soup = BeautifulSoup(html_content, 'html.parser')
    user_divs = soup.find_all('div', class_='pam _3-95 _2ph- _a6-g uiBoxWhite noborder')
    usernames = [username_link.text for div in user_divs for username_link in div.find_all('a')]
    return usernames


def find_the_snakes(followers, following):
    """Calculate and return users who you are following but who don't follow you back"""
    followers_set = set(followers)
    following_set = set(following)
    not_followed_back = following_set - followers_set
    return list(not_followed_back)


def add_snakes_to_file(usernames, file_name):
    """Write the list of usernames to a file"""
    with open(file_name, 'w', encoding='utf-8') as file:
        for username in usernames:
            file.write(username + '\n')


def main():
    # Define the file paths for followers and following
    followers_file = 'followers.html'
    following_file = 'following.html'

    # Check if 'snakes.txt' exists and delete it if it does
    if os.path.exists('snakes.txt'):
        os.remove('snakes.txt')

    # Load HTML content and extract usernames
    followers_html = load_html_content(followers_file)
    following_html = load_html_content(following_file)
    follower_usernames = extract_usernames_from_html(followers_html)
    following_usernames = extract_usernames_from_html(following_html)

    # Find snakes not following me back
    snakes = find_the_snakes(follower_usernames, following_usernames)

    # Add each snake to a file
    add_snakes_to_file(snakes, 'snakes.txt')

    # Inform the user to check snakes.txt
    print("Check 'snakes.txt' for the list of snakes not following you back...")


if __name__ == "__main__":
    main()
