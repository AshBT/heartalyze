# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pattern.web import extension, find_urls, URL, DOM, abs, re

# <codecell>

url = URL('http://www.snpedia.com/index.php/Heart_disease')

# <codecell>

dom = DOM(url.download())

# <codecell>

dom

# <codecell>

relevant_links = []
for link in dom('a'):
    all_urls = abs(link.attributes.get('href',''), base=url.redirect or url.string)
    urls = all_urls.lower()
    for url in urls:
        link = re.match(
        

# <codecell>


