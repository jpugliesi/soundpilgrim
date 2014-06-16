import re

# <iframe width="100%" height="100%" scrolling="no" frameborder="no" 
# src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/57451586&amp;auto_play=false&amp;hide_related=true&amp;show_user=false&amp;show_comments=false&amp;visual=true"></iframe>
#

soundcloud_url = '<iframe width="100%" height="100%" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/57451586&amp;auto_play=false&amp;hide_related=true&amp;show_user=false&amp;show_comments=false&amp;visual=true"></iframe>'


url_segment = re.search(r'src="(.+?)&amp', soundcloud_url)

print url_segment.group(1)

