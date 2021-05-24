import glob
import json
import csv
 

path = '/home/ronghao/analisis_top-100/analisis_V80/'
path_file = glob.glob(path + "/**/*.json", recursive = True)
csv_file = open('/home/ronghao/analisis_top-100/analisis_V80/analisis_80_2.csv', 'w', encoding='UTF8')
csv_writer = csv.writer(csv_file)
header=['URL', 'Cookies de tercero', 'Trackers', 'Almacenamiento local', 
        'Almacenamiento de sesión', 'fingerprinting','Canvas', 'WebGL', 'WebRTC', 'Facebok pixel', 'Google Analytics']
csv_writer.writerow(header)

info_ob= ["window.navigator.appCodeName", "window.navigator.appName", "window.navigator.appVersion",
 "window.navigator.buildID", "window.navigator.cookieEnabled", "window.navigator.doNotTrack", 
 "window.navigator.geolocation", "window.navigator.language", "window.navigator.languages", 
 "window.navigator.onLine", "window.navigator.oscpu", "window.navigator.platform", 
 "window.navigator.product", "window.navigator.productSub", "window.navigator.userAgent", 
 "window.navigator.vendorSub", "window.navigator.vendor", "window.screen.pixelDepth", 
 "window.screen.colorDepth"]
 
navplug= "window.navigator.plugins"
navmim= "window.navigator.mimeTypes"


for path in path_file:
    result = []
    info_count = 0
    plug_count = 0
    mime_count = 0
    
    with open(path) as json_file:
        data = json.load(json_file)
        if (not data['chrome_error']):
            result.append(data['site_url'])
            result.append(data['cookiestats']['third_party_long'] + data['cookiestats']['third_party_short'])
            result.append(len(data['cookiestats']['trackers']))
            result.append(len(data['local_storage']))
            result.append(len(data['session_storage']))
            #TODO: check 
            for k in data['fingerprinting_window']: 
                if(k in info_ob ):
                    if data['fingerprinting_window'][k] != 0:
                        info_count +=1
                elif(k == navplug):
                    plug_count += data['fingerprinting_window'][k]
                elif(k == navmim):
                    mime_count += data['fingerprinting_window'][k]

            if(info_count > 15 or plug_count > 5 or mime_count > 3): 
                result.append(1)
            else:
                result.append(0)
            
            if (data['fingerprinting']['canvas']['is_fingerprinting']):
                canvas = 1
            else:
                canvas = 0

            result.append(canvas)

            if (len(data['fingerprinting']['webGL']['calls']) == 0):
                webgl = 0
            else: 
                webgl = 1

            result.append(webgl)

            if (len(data['fingerprinting']['webRTC']['calls']) == 0):
                webRTC = 0
            else: 
                webRTC = 1

            result.append(webRTC)

            if (data['facebook_pixel']['facebook_pixel'] is not None):
                fb = 1
            else: 
                fb = 0

            result.append(fb)
            
            if (data['google_analytics']['has_trackers'] is not None):
                google = 1
            else: 
                google = 0
            
            result.append(google)
            csv_writer.writerow(result)

csv_file.close
