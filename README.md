Heartalyze
----------
 - Heartalyze solves a problem of gathering genuine dataset of various type of diseases that can be of help to doctors, researchers etc. Users can gather the data & use it for machine learning, data analysis etc.
 - Pair programmed: Ankita Kulkarni & Ashley Beattie

<b>Problem we are trying to solve:</b>
----------------------------------
- Gather and accumulate large datasets related to Heart Disease to enable citizen science
- No API for grabing data related to any type of disease

<b>Solution:</b>
-----------------
- By parsing SNPedia and OpenSNP we programatically find relevant 23andMe genome datasets for researchers and citizen scientists
- Built an API to be used for grabbing any disease

<b>Data Gathering:</b>
------------------------
- Check out this video on youtube: <a href="https://www.youtube.com/watch?v=PdIP0BoD5vw">link</a>

<b>How does data look like:</b>
-------------------------------

<b>SNPs identified: 29</b><br>
Information from SNPedia.com         
{'pairs': [u'CC', u'CT', u'TT'], <br> 
'orientation': u'plus', <br> 
'valuable_users': [['39'], ['1'], ['6']], <br> 
'open_snp_link': u'http://opensnp.org/snps/Rs17672135', <br> 
'rsid': 'rs17672135', <br> 
'position': u'240445596', <br> 
'GMAF': u'0.1084', <br> 
'chromosome': u'1'}<br> 

<b>'n' Individual Profiles Identified</b><br>
Information from OpenSNP.org:<br>
{'data_download_url': 'https://opensnp.org/data/216.23andme.109?1328210149', <br> 
'user_name': u'bryan e', <br> 
'phenotypes': {'113': {'phenotype': u'Phobia', <br> 
                      'variation': u'no'}}, <br> 
'user_url': 'https://opensnp.org/users/216'} <br> 


<br>
This API is under development.



