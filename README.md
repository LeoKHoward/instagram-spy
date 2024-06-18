# Instagram Spy

This project is designed to identify users who you are following on Instagram but who are not following you back.

It utilises web scraping techniques to extract usernames from HTML content and processes this data to find users who fit
this criteria.

### Getting Started

To get started with this project, follow these steps:

### Prerequisites

Python 3.9 installed on your machine

BeautifulSoup library for Python

```
pip install beautifulsoup4
```

### Setup

Before running the script, ensure you have the required HTML files ([followers.html](followers.html)
and [following.html](following.html)) in the project directory.

These files should contain the HTML content from which usernames will be extracted.

You can get these files by downloading the relevant data from your Instagram account to your local machine.

### Running the Script

Run the code manually or by using Python:

```
python RUN_ME.py
```

After execution, the script will generate a snakes.txt file listing the usernames of users who are being followed but
have not followed back.

The script will automatically delete any existing snakes.txt file before generating a new one to avoid data duplication.

## Usage

Once the script has completed its execution, you can find the list of usernames in the snakes.txt file.