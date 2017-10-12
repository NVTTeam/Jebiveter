import os

try:
  import xbmc, xbmcaddon
  KODI = True
  __addon__ = xbmcaddon.Addon()
  __data_dir__ = xbmc.translatePath(__addon__.getAddonInfo('profile'))
except:
  KODI = False
  __addon__ = None
  __data_dir__ = ''

__addonname__ = 'Digitally Iported Premium'
DATA_FILE = 'https://pastebin.com/raw/zLnJ5V5k'
CACHE_FILE = os.path.join(__data_dir__, 'data.json')
CACHE_TIME = (12*60*60) #12hours
