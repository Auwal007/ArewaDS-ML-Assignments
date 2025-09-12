"""
Simple Pride & Prejudice absolute polarity checker (beginner-friendly)
Save this file next to `pride_and_prejudice.txt` or let it download the book automatically.

Requirements:
- Python 3
- textblob and pattern (install with pip)

Run in PowerShell:
> pip install textblob pattern
> python -m textblob.download_corpora
> python run_pp.py
"""
import os
import urllib.request
from textblob import TextBlob

GUTENBERG_URL = 'https://www.gutenberg.org/files/1342/1342-0.txt'
LOCAL_FILE = 'pride_and_prejudice.txt'


def download_book(url, dest):
    print('Downloading book...')
    urllib.request.urlretrieve(url, dest)
    print('Saved to', dest)


def load_book(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    if not os.path.exists(LOCAL_FILE):
        try:
            download_book(GUTENBERG_URL, LOCAL_FILE)
        except Exception as e:
            print('Could not download book automatically:', e)
            print('Please download it manually from Project Gutenberg and save as', LOCAL_FILE)
            raise SystemExit(1)

    raw = load_book(LOCAL_FILE)

    # Try to remove Gutenberg header/footer simply
    start_marker = '*** START OF THE PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE ***'
    end_marker = '*** END OF THE PROJECT GUTENBERG EBOOK PRIDE AND PREJUDICE ***'
    start = raw.find(start_marker)
    end = raw.find(end_marker)
    if start != -1 and end != -1:
        book_text = raw[start+len(start_marker):end].strip()
    else:
        # fallback: find first "Chapter 1" (simple)
        lines = raw.splitlines()
        idx = 0
        for i, line in enumerate(lines):
            if line.strip().lower().startswith('chapter 1') or line.strip().lower().startswith('chapter i'):
                idx = i
                break
        book_text = '\n'.join(lines[idx:])

    blob = TextBlob(book_text)
    pos = []
    neg = []
    for sent in blob.sentences:
        p = sent.sentiment.polarity
        if p == 1.0:
            pos.append(str(sent))
        elif p == -1.0:
            neg.append(str(sent))

    print('\nAbsolute positive sentences (polarity == 1):', len(pos))
    print('Absolute negative sentences (polarity == -1):', len(neg))

    if pos:
        print('\nExamples (positive):')
        for s in pos[:5]:
            print('-', s)

    if neg:
        print('\nExamples (negative):')
        for s in neg[:5]:
            print('-', s)
