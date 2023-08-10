#Web validation

import re

web = input('Type Your Website Link: ')

search = re.search(r'(https?): //(www)?\.?(\w+)\.(\w+):?(\d+)?/?(.+)', web)

print(search.group())

print(search.groups())

print(f'The protocol: {search.group(1)}')

print(f'The sub domain: {search.group(2)}')

print(f'The domin name: {search.group(3)}')

print(f'The top level domain: {search.group(4)}')

print(f'The port: {search.group(5)}')

print(f'The query string: {search.group(6)}')

