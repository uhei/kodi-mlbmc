# pylint: disable = line-too-long, invalid-name, bare-except, eval-used, wildcard-import, unused-wildcard-import, too-many-branches, too-many-locals
# pylint: disable = too-many-statements, old-style-class, no-init, too-few-public-methods, missing-docstring, too-many-arguments, global-statement
# pylint: disable = relative-import

# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License.
# *  If not, write to the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *
# *  2011/05/30
# *
# *  Thanks and credit to:
# *
# *  mlbviewer  http://sourceforge.net/projects/mlbviewer/  Most of the mlb.tv code was from this project.
# *
# *  Everyone from the fourm - http://fourm.xbmc.org
# *    giftie - for the colored text code :) thanks.
# *    theophile and the others from - http://forum.xbmc.org/showthread.php?t = 97251
# *    bunglebungle for game highlights patch - http://forum.xbmc.org/showthread.php?tid = 104391&pid = 1109006#pid1109006


import xbmcplugin
import sys
import urllib
import time
from datetime import datetime
from resources import mlb, mlb_common, mlbtv
import xbmcaddon

addon = xbmcaddon.Addon(id='plugin.video.mlbmc')
remote_debugging = addon.getSetting('debug_remote') == "true"

# append pydev remote debugger
if remote_debugging:
    try:
        import pysrc.pydevd as pydevd 
        # stdoutToServer and stderrToServer redirect stdout and stderr to eclipse console
        pydevd.settrace('localhost', stdoutToServer=True, stderrToServer=True)
    except ImportError:
        sys.stderr.write("Error: " +
            "You must add org.python.pydev.debug.pysrc to your PYTHONPATH.")
        sys.exit(1)

url = None
name = None
mode = None
live = None
event = None
content = None
session = None
cookieIp = None
cookieFp = None
scenario = None
game_type = None
podcasts = False

params = mlb_common.get_params()

try:
    url = urllib.unquote_plus(params["url"])
except:
    pass
try:
    name = urllib.unquote_plus(params["name"])
except:
    pass
try:
    mode = int(params["mode"])
except:
    pass
try:
    live = eval(params["live"])
except:
    pass
try:
    podcasts = eval(params["podcasts"])
except:
    pass
try:
    event = urllib.unquote_plus(params["event"])
except:
    pass
try:
    content = urllib.unquote_plus(params["content"])
except:
    pass
try:
    session = urllib.unquote_plus(params["session"])
except:
    pass
try:
    cookieIp = urllib.unquote_plus(params["cookieIp"])
except:
    pass
try:
    cookieFp = urllib.unquote_plus(params["cookieFp"])
except:
    pass
try:
    scenario = urllib.unquote_plus(params["scenario"])
except:
    pass
try:
    game_type = urllib.unquote_plus(params["game_type"])
except:
    pass

mlb_common.addon_log("Mode: "+str(mode))
mlb_common.addon_log("URL: "+str(url))
mlb_common.addon_log("Name: "+str(name))

if mode is None:
    mlb.get_categories()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 1:
    mlb.get_videos(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 2:
    if podcasts:
        mlb.set_video_url(url, True)
    else:
        mlb.set_video_url(url)

if mode == 3:
    mlb.get_game_calendar('mlbtv')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 4:
    mlb.get_teams(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 5:
    mlb.get_team_video(url)

if mode == 6:
    mlb.get_games(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 7:
    mlbtv.get_mlb_game(event)

if mode == 8:
    mlb.get_realtime_video(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 9:
    mlbtv.get_game_url(name, event, content, session, cookieIp, cookieFp, scenario, live)

if mode == 10:
    mlb.get_podcasts(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 11:
    url = mlb.get_date(game_type)
    if game_type == 'mlbtv':
        mlb.get_games(url)
    else:
        mlb.get_condensed_games(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 12:
    mlb.play_latest()

if mode == 13:
    mlb.get_game_calendar('condensed')
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 14:
    mlb.get_condensed_games(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 15:
    try:
        start_date = datetime.strptime(url, "%B %d, %Y - %A")
    except TypeError:
        start_date = datetime.fromtimestamp(time.mktime(time.strptime(url, "%B %d, %Y - %A")))
    mlb.get_game_calendar(game_type, start_date)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 16:
    mlb.do_search(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 17:
    mlb.get_game_highlights()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 18:
    mlb.get_mlb_playlist(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 19:
    mlb.get_mlb_playlist(url, name)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 20:
    mlb.get_players(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 21:
    mlb.get_videos('current_playlist', int(url))
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 22:
    mlb.mlb_podcasts()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 23:
    mlb.get_full_count()
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 24:
    mlb.get_topic_playlist(url, eval(game_type))
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 25:
    mlbtv.get_mlb_game(event, True)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 26:
    mlb.get_game_highlights_of_date(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 27:
    mlb.get_realtime_video(url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 28:
    mlb.get_playlist_cats(False, url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 29:
    mlb.get_playlist_cats(True, url)
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if mode == 30:
    pass
