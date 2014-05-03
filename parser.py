# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pattern.web import extension, find_urls, URL, DOM, abs
import re

# <codecell>

url = URL('http://www.snpedia.com/index.php/Heart_disease')

# <codecell>

dom = DOM(url.download())

# <codecell>

dom

# <codecell>

relevant_links = []
urls = []

for link in dom('a'):
    all_urls = abs(link.attributes.get('href',''), base=url.redirect or url.string)
    urls.append(all_urls)
    
for item in urls:
    lower = item.lower() 
    if re.search(r'rs[\d]+', lower):
        relevant_links.append(lower)
        
print relevant_links
    

# <codecell>

for relevant_link in relevant_links:
    data = URL(relevant_link)
    site = data.download()
    

# <codecell>


