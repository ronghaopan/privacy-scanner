from privacyscanner.scanmodules.chromedevtools.extractors.base import Extractor
from privacyscanner.scanmodules.chromedevtools.utils import JavaScriptError, javascript_evaluate


GetResult = """
(function() {
   var dict = new Object();
    dict['window.plugins'] = window.plugins;
    dict['window.useragent'] = window.useragent;
    dict['window.language'] = window.language;
    dict['window.languages'] = window.languages;
    dict['window.cpuclass'] = window.cpuclass;
    dict['window.platform'] = window.platform;
    dict['window.doNotTrack'] = window.doNotTrack;
    dict['window.appName'] = window.appName;
    dict['window.colorDepth'] = window.colorDepth;
    dict['window.height'] = window.height;
    dict['window.width'] = window.width;
    dict['window.localstorage'] = window.localstorage;
    dict['window.sessionstorage'] = window.sessionstorage;
    dict['window.indexDB'] = window.indexDB;
    dict['window.connection'] = window.connection;
    dict['window.rtc'] = window.rtc;
    dict['window.aud'] = window.aud;
    dict['window.memory'] = window.memory;
    dict['window.concurrency'] = window.concurrency;
    dict['window.geolocation'] = window.geolocation; 
    return dict;
})()
"""

class WindowFingerprintingExtractor(Extractor): 
    def extract_information(self):
        info = {}
        if not self.options['disable_javascript']:
            try:
                info = javascript_evaluate(self.page.tab, GetResult)
            except JavaScriptError:
                pass
        self.result['fingerprinting_window'] = info