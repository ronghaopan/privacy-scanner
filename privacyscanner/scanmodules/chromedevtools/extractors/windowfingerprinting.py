from privacyscanner.scanmodules.chromedevtools.extractors.base import Extractor
from privacyscanner.scanmodules.chromedevtools.utils import JavaScriptError, javascript_evaluate


GetResult = """
(function() {
    dict['window.navigator.plugins'] = window.plugins;
    return dict;
})()
""".lstrip()

class WindowFingerprintingExtractor(Extractor): 
    def extract_information(self):
        info = {}
        if not self.options['disable_javascript']:
            try:
                info = javascript_evaluate(self.page.tab, GetResult)
            except JavaScriptError:
                pass
        
        for k in info.keys():
            if(info[k] is None or isinstance(info[k], list)): 
                info[k] = 0
        
        self.result['fingerprinting_window'] = info