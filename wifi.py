import time
from pywifi import PyWiFi, const, Profile
   
def connect_to_wifi(ssid, password):
  wifi = PyWiFi()
  # initialise interface using the first one
  interface = wifi.interfaces()[0]
  # disconnect all other connections
  interface.disconnect()
  # waiting for all disconnection to complete
  while interface.status() == 4:
      # break from the loop once all disconnection complete
      pass
  # initialise profile
  profile = Profile()
  # wifi name
  profile.ssid = ssid
  # need verification
  profile.auth = const.AUTH_ALG_OPEN
  # wifi default encryption algorithm
  profile.akm.append(const.AKM_TYPE_WPA2PSK)
  profile.cipher = const.CIPHER_TYPE_CCMP
  # wifi password
  profile.key = password
  # remove all wifi connection profiles
  interface.remove_all_network_profiles()
  # set new wifi connection profile
  tmp_profile = interface.add_network_profile(profile)
  # attempting new connection
  interface.connect(tmp_profile)
  time.sleep(5)
  if interface.status() == 4:        
        print(f'\rConnection Succeeded')
        return 1
  else:
        print(f'\rTrying but not works!!!!', end='')
        return 0
    
 


# Configuración de la red Wi-Fi
SSID = "Soporte_CELLSHOP_2.4Ghz"
SSID2 = "Soporte_CELLSHOP_5G"
PASSWORD = "41162910"

# Intentar conectar a la red
# connect_to_wifi(SSID, PASSWORD)


def wifi():
    print(f"trying to connect with : {SSID2}")
    result = connect_to_wifi(SSID2, PASSWORD)
    if(result == 0):
       print(f"\nnot work !! trying with another one : {SSID}")
       connect_to_wifi(SSID, PASSWORD)
    
wifi()