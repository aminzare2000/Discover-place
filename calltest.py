from OpenAlexTools import OpenAlexTools
from json import *

def get_journal_by_issn(issn):
    oaTools = OpenAlexTools()
    # 0029-3970
    pages_of_venues = oaTools.get_venues('2167-8359') 
    for page in pages_of_venues:
        for work in page['results']:
            return work
            # display_name: "PeerJ",
            # publisher: "PeerJ",
            # works_count: 21100,
            # cited_by_count: 151312,
            # is_oa: true,
            # is_in_doaj: true,
            # homepage_url: "http://www.peerj.com/",        
            # print(work['issn']) # list of issns
            # print(work['display_name'])
            # print(work['publisher'])
            # print(work['works_count'])
            # print(work['cited_by_count'])
            # print(work['is_oa'])
            # print(work['is_in_doaj'])
            # print(work['homepage_url'])
            # print(work['created_date']) # date of creation
            
            counts_by_year_list = work['counts_by_year']
            for item in counts_by_year_list:
                print(item['year'])
                print(item['works_count'])
                print(item['cited_by_count'])

        
        

