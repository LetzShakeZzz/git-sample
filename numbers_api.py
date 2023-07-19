import requests
import sys

def check_number(number):
    api_url = f'http://numbersapi.com/{number}/math?json=true'
    r = requests.get(api_url)
    print(('Boring', 'Interesting')[r.json()['found']])

def main():
    for num in sys.stdin:
        num = num.rstrip()
        check_number(num)

if __name__ == '__main__':
    main()