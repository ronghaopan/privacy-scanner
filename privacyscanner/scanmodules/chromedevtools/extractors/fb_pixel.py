
from privacyscanner.scanmodules.chromedevtools.extractors.base import Extractor


FB_STANDARD_EVENTS = {
    "AddPaymentInfo", "AddToCart", "AddToWishlist", "CompleteRegistration",
    "Contact", "CustomizeProduct", "Donate", "FindLocation", "InitiateCheckout",
    "Lead", "PageView", "Purchase", "Schedule", "Search", "StartTrial", 
    "SubmitApplication", "Subscribe", "ViewContent"
}

FB_ADVANCED_MATCHING_PARAMETERS = {
  "ud[em]": "Email",
  "ud[fn]": "First Name",
  "ud[ln]": "Last Name",
  "ud[ph]": "Phone",
  "ud[ge]": "Gender",
  "ud[db]": "Birthdate",
  "ud[city]": "City",
  "ud[ct]": "City",
  "ud[state]": "State or Province",
  "ud[st]": "State or Province",
  "ud[zp]": "Zip Code",
  "ud[cn]": "Country",
  "ud[country]": "Country",
  "ud[external_id]": "An ID from another database.",
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
                    res_advanced = [ev for ev in FB_ADVANCED_MATCHING_PARAMETERS.keys() if(ev in ele)]
                    if res_stantard or res_advanced: 
                        fb['facebook_pixel'] = True
                        fb['event'].append(ele)

        self.result['facebook_pixel'] = fb
                        
