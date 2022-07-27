from logging import raiseExceptions
from diophila import *


class OpenAlexTools:

    def __init__(self):
        self.openalex = OpenAlex()
        # https://api.openalex.org/venues?filter=works_count:%3E1000
        self.baseVenue = "https://api.openalex.org/venues"

    #  There are several types, including journals, conferences, preprint repositories, and institutional repositories.
    def get_venues(self, issn=None):
        if issn is None:
            raiseExceptions(Exception("issn is required"))
        else:
            issn = {"issn": issn}
        pages = [1, 2, 3]
        # url = self.baseVenue + issn
        venues_gen = self.openalex.get_list_of_venues(filters=issn, pages=pages)
        venues =[]
        for page_gen in venues_gen:
            # for meta in page['meta']:            
            for work_gen in page_gen['results']:
                venue = work_gen;
                venue['id'] = work_gen['id'].split('/')[-1]
                venues.append(venue)
                # return work;
        return venues


    def __cal_pages(self, per_page ,filters):
        # if no `pages` parameter is supplied, we use cursor paging
        pages = None        
        # if `pages` parameter is supplied, we use basic paging
        pages_of_works_gen = self.openalex.get_list_of_works(filters=filters,pages=pages,per_page=1)
        
        for page_of_work in pages_of_works_gen:        # loop through pages
            count = page_of_work['meta']['count'] 
            break               

        no_pages = 0

        if(count % per_page == 0):
            no_pages = count // per_page         
        else:
            no_pages =  (count // per_page) + 1

        pages = [*range(1, no_pages)]
        return pages

    def __Process_abstract_inverted_index(self, inverted_index):

        max = 0
        temp1 = None
        if(inverted_index is not None):        
            for word in inverted_index:
                for idx in inverted_index[word]:
                    if idx > max:
                        max = idx

            
            abstract = [None for _ in range(max)]
            for word in inverted_index:
                for idx in inverted_index[word]:
                    abstract[idx-1] = word
            temp1 = ' '.join(abstract)
        
        
        
        return temp1

    def get_works(self, url_id, year , page = None):
        page_work =[]
        abstract_work =[]
        # works_api_url = "https://api.openalex.org/works?page=1&per-page=25&" + \
        # "filter=host_venue.id:"+url_id+",publication_year:"+str(year)        
        # pages_of_works_gen = self.openalex.get_works_by_api_url(works_api_url)
        # for page_of_work in pages_of_works_gen:
        #     # for meta in page['meta']:            
        #     for work_gen in page_of_work['results']:
        #         work1 = work_gen;                
        #         page_work.append(work1)

        # if no `pages` parameter is supplied, we use cursor paging
        pages = None
        per_page = 25
        # if `pages` parameter is supplied, we use basic paging        
        filters = {"host_venue.id": url_id,
                "publication_year": str(year) }        
        pages = self.__cal_pages(per_page ,filters)
        if page is None:
            pages_of_works_gen = self.openalex.get_list_of_works(filters=filters,per_page=per_page, pages=[pages[0]])
        else:
            pages_of_works_gen = self.openalex.get_list_of_works(filters=filters,per_page=per_page, pages=[page])

        for page_of_work in pages_of_works_gen:        # loop through pages
            for work_gen in page_of_work['results']:   # loop though list of venues
                # self.__Process_abstract_inverted_index(work_gen['abstract_inverted_index'])
                temp = self.__Process_abstract_inverted_index(work_gen['abstract_inverted_index'])
                work1 = work_gen                
                page_work.append( {'work':work1, 'abstract':temp} )
            
        return page_work , pages
    


        


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
