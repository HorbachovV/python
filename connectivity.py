import urllib.request as urlib


def main(url):
    print('Cheking connectivity...')

    response = urlib.urlopen(url)
    print(f'Connected to {url} succesfully')
    print(f'The response code was:  {response.getcode()}')

print('This is site connectivity checker program')
input_url  = input('Input the URL of the site: ')
    
main(input_url)