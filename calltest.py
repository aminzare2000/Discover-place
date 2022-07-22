from OpenAlexTools import OpenAlexTools

oaTools = OpenAlexTools()
# 2167-8359
pages_of_venues = oaTools.get_venues('0029-3970') 
for page in pages_of_venues:
    for work in page['results']:
        print(work['display_name'])
