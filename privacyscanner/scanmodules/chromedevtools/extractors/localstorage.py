from privacyscanner.scanmodules.chromedevtools.extractors.base import Extractor
from privacyscanner.scanmodules.chromedevtools.utils import JavaScriptError, javascript_evaluate

STORAGE_JS = """
(function() {
    var dict = new Object();
    for (var i = 0; i < localStorage.length; i++){
        key=localStorage.key(i); 
        dict[key]=localStorage.getItem(key);   
    } 
    window.localstorage = window.localstorage - localStorage.length;
    return dict;
})()
""".lstrip()



class LocalStorageExtractor(Extractor):
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
            localStorage = {}
            localStorage['key'] = key
            localStorage['content'] = value
            result.append(localStorage)
        
        self.result['local_storage'] = result
        