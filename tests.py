from pygooglenews import GoogleNews

gn = GoogleNews()

search_result = gn.search('Eric Ciotti', from_='2020-01-01', to_='2020-12-31')
entries = search_result['entries']
print(entries)
