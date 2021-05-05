
from privacyscanner.scanmodules.chromedevtools.extractors.base import Extractor


FB_STANDARD_EVENTS = {
    "AddPaymentInfo", "AddToCart", "AddToWishlist", "CompleteRegistration",
    "Contact", "CustomizeProduct", "Donate", "FindLocation", "InitiateCheckout",
    "Lead", "PageView", "Purchase", "Schedule", "Search", "StartTrial", 
    "SubmitApplication", "Subscribe", "ViewContent"
}


class FacebookPixelExtractor(Extractor): 
    def extract_information(self):  
        fb = {
            'facebook_pixel' : None,
            'event': []
        }

        fb_domain = 'www.facebook.com'
        #find the facebook request 
        for request in self.page.request_log:
            if fb_domain == request['parsed_url'].netloc:
                fb_query = request['parsed_url'].query.split('&')
                for ele in fb_query: 
                    res_stantard = [ev for ev in FB_STANDARD_EVENTS if(ev in ele)]
                    if res_stantard: 
                        fb['facebook_pixel'] = True
                        fb['event'].append(ele)

        self.result['facebook_pixel'] = fb
                        
