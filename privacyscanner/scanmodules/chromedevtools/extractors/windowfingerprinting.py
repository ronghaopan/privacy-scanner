from privacyscanner.scanmodules.chromedevtools.extractors.base import Extractor
from privacyscanner.scanmodules.chromedevtools.utils import JavaScriptError, javascript_evaluate


GetResult = """
(function() {
   var dict = new Object();
    dict['window.plugins'] = window.plugins;
    dict['window.useragent'] = window.useragent;
    dict['window.language'] = window.language;
    dict['window.cpuclass'] = window.cpuclass;
    dict['window.platform'] = window.platform;
    dict['window.doNotTrack'] = window.doNotTrack;
    dict['window.appName'] = window.appName;
    dict['window.localstorage'] = window.localstorage;
    dict['window.sessionstorage'] = window.sessionstorage;
    dict['window.indexDB'] = window.indexDB;
    dict['window.AudioContext'] = window.aud; 
    dict['window.appCodeName'] = window.appCodeName; 
    dict['window.screen.pixelDepth'] = window.pixelDepth; 
    dict['window.screen.colorDepth'] = window.colorDepth; 
    dict['window.mimeTypes'] = window.mimeTypes; 

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
        self.result['fingerprinting_window'] = info