config.load_autoconfig()
config.bind('<Ctrl-v>', 'spawn mpv {url}')
c.url.start_pages = "duckduckgo.com"
c.url.searchengines = {'DEFAULT': 'https://search.brave.com/search?q={}'}
