import urllib.request

def main():
    print(urllib.request.urlopen("http://localhost:5000/ping").read())


if __name__ == '__main__':
    main()