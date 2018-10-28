import argparse
import requests

BASE_URL = 'https://haveibeenpwned.com/api/v2/breachedaccount/{0}'


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main(mailid='test@example.com'):
    try:
        req = requests.get(BASE_URL.format(mailid))
        pwned_no = len(req.json())
        if (pwned_no <= 1):
            print('{0}You have been pwned {1} time'.format(bcolors.FAIL, pwned_no))
        else:
            print('You have been pwned {1} times'.format(bcolors.FAIL, pwned_no))
        for d in req.json():
            for key, val in d.items():
                print(key, val)
    except:
        print(bcolors.HEADER + 'You where never pwned~!')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='haveibeenpwned command line tool')
    parser.add_argument('string', metavar='str', nargs='+', type=str, help='mail id to check')
    args = parser.parse_args()
    main(args.string[0])
