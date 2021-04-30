from privacyscanner.scanmodules.chromedevtools.extractors.base import Extractor
from privacyscanner.scanmodules.chromedevtools.utils import JavaScriptError, javascript_evaluate

STORAGE_JS = """
(function() {
    var dict = new Object();
    for (var i = 0; i < sessionStorage.length; i++){
        key=sessionStorage.key(i); 
        dict[key]=sessionStorage.getItem(key);   
    } 
    window.sessionstorage = window.sessionstorage - sessionStorage.length;
    return dict;
})()
""".lstrip()



class SessionStorageExtractor(Extractor):
    def extract_information(self):
        
        result = []

        info = {}
        # Ejecuta script y conseguir local storage
        if not self.options['disable_javascript']:
            try: 
                info = javascript_evaluate(self.page.tab, STORAGE_JS);
            except JavaScriptError: 
                print("error")
                pass
        
        for key, value in info.items():
            sessionStorage = {}
            sessionStorage['key'] = key
            sessionStorage['content'] = value
            result.append(sessionStorage)
        
        self.result['session_storage'] = result
        