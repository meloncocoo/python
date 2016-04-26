import sys


def main(url):
    print('start main function with %(url)s' % {'url': url})

if __name__ == '__main__':
    baseurl = ''
    if sys.argv[1:]:
        baseurl = sys.argv[1]
        if baseurl.startswith("http://"):
            main(baseurl)
        else:
            print("Parameter Error!")
    else:
        print("Parameter request.")
