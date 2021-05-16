from privacyscanner.scanmodules.chromedevtools.extractors.base import Extractor
from privacyscanner.scanmodules.chromedevtools.utils import JavaScriptError, javascript_evaluate


GetResult = """
(function() {
    dict = new Object();
    dict['window.navigator.plugins'] =  window.plugins;
    dict['window.navigator.userAgent'] = window.userAgent;
    dict['window.navigator.language'] =  window.language;
    dict['window.navigator.cpuclass'] =  window.cpuclass;
    dict['window.navigator.platform'] =  window.platform;
    dict['window.navigator.doNotTrack'] =  window.doNotTrack;
    dict['window.navigator.appName'] = window.appName;
    dict['window.navigator.indexDB'] = window.indexDB;
    dict['window.AudioContext'] = window.audioContext; 
    dict['window.navigator.appCodeName'] = window.appCodeName; 
    dict['window.screen.pixelDepth'] = window.pixelDepth; 
    dict['window.screen.colorDepth'] = window.colorDepth; 
    dict['window.navigator.mimeTypes'] = window.mimeTypes; 
    dict['window.navigator.appVersion'] = window.appVersion; 
    dict['window.navigator.buildID'] = window.buildID;
    dict['window.navigator.cookieEnable'] = window.cookieEnable; 
    dict['window.navigator.languages'] = window.languages;
    dict['window.navigator.onLine'] = window.onLine;
    dict['window.navigator.oscpu'] = window.oscpu;
    dict['window.navigator.product'] = window.product;
    dict['window.navigator.productSub'] = window.productSub;
    dict['window.navigator.vendorSub'] = window.vendorSub;
    dict['window.navigator.vendor'] = window.vendor;
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