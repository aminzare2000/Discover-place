from logging import raiseExceptions
from diophila import *

class OpenAlexTools:

    def __init__(self):
        self.openalex = OpenAlex()
        # https://api.openalex.org/venues?filter=works_count:%3E1000
        self.baseVenue = "https://api.openalex.org/venues" 
    
    def get_venues(self, issn=None):
        if issn is None:
            raiseExceptions(Exception("issn is required"))
        else:
            issn = {"issn" : issn}
        pages = [1, 2, 3]
        # url = self.baseVenue + issn
        return self.openalex.get_list_of_venues(filters=issn, pages=pages)


# works_api_url = "https://api.openalex.org/works?filter=author.id:A1969205032"
# pages_of_works = openalex.get_works_by_api_url(works_api_url)

# for page in pages_of_works:
#     for work in page['results']:
#         print(work['display_name'])



# # if no `pages` parameter is supplied, we use cursor paging
# pages = None
# # if `pages` parameter is supplied, we use basic paging
# pages = [1, 2, 3]

# filters = {"is_oa": "true",
#            "works_count": ">15000"}
# pages_of_venues = openalex.get_list_of_venues(filters=filters, pages=pages)

# for page in pages_of_venues:        # loop through pages
#     for venue in page['results']:   # loop though list of venues
#         venue['id']