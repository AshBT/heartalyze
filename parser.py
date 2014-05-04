# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from pattern.web import extension, find_urls, URL, DOM, abs
import re
from bs4 import BeautifulSoup

# <codecell>

url = URL('http://www.snpedia.com/index.php/Heart_disease')
dom = DOM(url.download())

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

# <codecell>

snpedia_data = {}

for page in relevant_links:

    #for relevant_link in test_link:
    data = URL(page)
    site = data.download()
    
    soup = BeautifulSoup(site)
    rsid_upper = soup.find("h1", attrs={'class':"firstHeading"}).getText()
    rsid = str(rsid_upper.lower())
    orientation = soup.find("a", attrs={'title':"Orientation"}).findNext().getText().lower()
    gmaf = soup.find("a", attrs={'title':"GMAF"}).findNext().getText().lower()
    
    table_data = soup.findAll('td')
    for entry in table_data:
        if entry.getText() == "Chromosome":
            chromosome = entry.findNext().getText().lower()   #assign this to snpedia_data
        if entry.getText() == "Gene":
            gene = entry.findNext().getText().lower()
        if entry.getText() == "Position":
            position = entry.findNext().getText().lower()
            
    open_snp_link = "http://opensnp.org/snps/" + rsid_upper
        
    magnitude = soup.find("a", attrs={'title':"Max Magnitude"}).findNext().getText().lower()
    
    if soup.find("table", attrs={'class':"sortable"}) == None:
        pairs = []
    else:
        pairs = []
        geno_data = soup.find("table", attrs={'class':"sortable"}).findAll("td")
        for line in geno_data:
            genotype = line.find_all("a")
            if genotype == []:
                pass
            else: 
                pair = ""
                pre_pair = genotype[0].getText()
                for character in pre_pair:
                    if character not in ["(",";",")"]:
                        pair = pair + character
                pairs.append(pair)
        
    
    snpedia_data[rsid] = {}
    snpedia_data[rsid]['rsid'] = rsid
    print snpedia_data[rsid]['rsid']
    
    if orientation == None:
        snpedia_data[rsid]['orientation'] = ""
    else:
        snpedia_data[rsid]['orientation'] = orientation
    
    if chromosome == None:
        snpedia_data[rsid]['chromosome'] = ""
    else:
        snpedia_data[rsid]['chromosome'] = chromosome
    
    if gmaf == None:
        snpedia_data[rsid]['GMAF'] = ""
    else:
        snpedia_data[rsid]['GMAF'] = gmaf
    
    if position == None:
        snpedia_data[rsid]['position'] = ""
    else:
        snpedia_data[rsid]['position'] = position
    
    if open_snp_link == None:
        snpedia_data[rsid]['open_snp_link'] = ""
    else:
        snpedia_data[rsid]['open_snp_link'] = open_snp_link
    
    if pairs == None:
        snpedia_data[rsid]['pairs'] = ""
    else:
        snpedia_data[rsid]['pairs'] = pairs
    
    
    print snpedia_data[rsid]['orientation']
    print snpedia_data[rsid]['chromosome']
    print snpedia_data[rsid]['GMAF']
    print snpedia_data[rsid]['position']
    print snpedia_data[rsid]['open_snp_link']
    print snpedia_data[rsid]['pairs']
    #{'rsid_string':{'orientation':[], 'chromosome':[], 'GMAF':[], 'position':[], 'open_snp_link':[], 'genos': {'pair':{'msg':[],'summary':[]}}}}
    #print position
    #print gene
    #print rsid
    #print orientation
    #print chromosome
    #print gmaf
    #print open_snp_link
    #print pairs

# <codecell>

### get the valuable users and relevant information

#open_snp_users = {}

valued_users_url = URL('https://opensnp.org/achievements/10')
dom_valued_users = DOM(valued_users_url.download())
users_soup = BeautifulSoup(valued_users_url.download())

valued_users = {}
users_re = re.compile(r'/users/(\d+)')
for link in dom_valued_users('a'):
    attributes = link.attrs['href']
    match = users_re.match(attributes)
    if match:
        user_id = str(match.group(1))
        valued_users[user_id] = {}
        users_url = "/users/" + user_id
        valued_users[user_id]['user_name'] = users_soup.find("a", attrs={'href':users_url}).getText().lower()
        valued_users[user_id]['user_url'] = "https://opensnp.org" + users_url

print valued_users

# <codecell>

data_download_re = re.compile(r'/data/[A-Za-z0-9._%+-?]+')
phenotype_re = re.compile(r'/phenotypes/(\d+)')
for userid in valued_users:
    users_page = URL(valued_users[userid]['user_url'])
    user_phenotype_soup = BeautifulSoup(users_page)
    
    for li in user_phenotype_soup.findAll('li'):
        for a in li.findAll('a'):
            link_match = data_download_re.match(a.attrs['href'])
            if link_match:
                user_data_download_url = link_match.group()
    ### fix multiple URLs issue
      
    
    if user_phenotype_soup.find("table", attrs={'class':'table table-striped'}):
        for tr in user_phenotype_soup.find("table", attrs={'class':'table table-striped'}).findAll('tr'):
            for td in tr.findAll('td'):
                
                if td.find('a'):
                    phenotype = td.find('a').getText()
                    match = phenotype_re.match(td.find('a').attrs['href'])
                    if match:
                        phenotype_id = match.group(1)
    
                    #print phenotype
                variation = td.getText()
                        #print variation
            #print phenotype_id, phenotype, variation
        valued_users[userid]['phenotypes'] = {}
        valued_users[userid]['phenotypes'][phenotype_id] = {}
        valued_users[userid]['phenotypes'][phenotype_id]['phenotype'] = phenotype
        valued_users[userid]['phenotypes'][phenotype_id]['variation'] = variation
    else:
        print valued_users[userid]['user_name'] + " doesn't have any phenotypes!"
    
    valued_users[userid]['data_download_url'] = "https://opensnp.org" + user_data_download_url 
    
    print "scraped user with id " + valued_users[userid]['user_name']
    
print len(valued_users)

# <codecell>

test = snpedia_data.keys()[0]

print test

snp_data_url = URL('https://opensnp.org/snps/' + test)

snp_data_soup = BeautifulSoup(snp_data_url.download())

download_links = snp_data_soup.findAll('a')
print download_links




# <codecell>

e = {"a":1}
print len(e)

# <codecell>


