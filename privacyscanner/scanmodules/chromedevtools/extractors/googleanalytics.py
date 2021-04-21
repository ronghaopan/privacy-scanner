import re
from privacyscanner.scanmodules.chromedevtools.extractors.base import Extractor


class GoogleAnalyticsExtractor(Extractor):
    def extract_information(self):
        googleAnalytics = {
            'has_trackers': None,
            'trackers_id': []
        }

        google_domain = ('google-analytics', 'stats.g.doubleclick')
        pattern = re.compile(r'^tid=UA-\w+')    
        #find domain in requests 
        for request in self.page.request_log:
            for domain in google_domain:
                if domain in request['parsed_url'].netloc:  
                    fb_query = request['parsed_url'].query.split('&')
                    for query in fb_query: 
                        if pattern.match(query):
                            googleAnalytics['has_trackers'] = True
                            ids = query.split('=')[1]
                            if ids not in googleAnalytics['trackers_id']:
                                googleAnalytics['trackers_id'].append(ids)
                            break
        
        self.result['google_analytics'] = googleAnalytics