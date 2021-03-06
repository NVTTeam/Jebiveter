import urllib,urllib2,urlparse,re,xbmc,xbmcaddon,HTMLParser,time,datetime,os,xbmcvfs
import json
import random
import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])


__addon__ = xbmcaddon.Addon()
cwd = xbmc.translatePath(__addon__.getAddonInfo('path')).decode("utf-8")
BASE_RESOURCE_PATH = os.path.join(cwd, 'resources', 'lib')
DATA_PATH  = xbmc.translatePath(__addon__.getAddonInfo('profile'))
sys.path.append(BASE_RESOURCE_PATH)

if not os.path.exists(DATA_PATH):
    os.mkdir(DATA_PATH)

from router import Router

if __name__ == '__main__':
    router = Router(sys.argv[0])
    router.route(sys.argv[2])
