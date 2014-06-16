import datetime
from django.utils import timezone

from django.test import TestCase

from musicblog.models import SongPost, SongCarousel, Genre

def create_songpost(genre, title, artist_name, days,
        soundcloud_url='<iframe width="100%" height="100%" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/57451586&amp;auto_play=false&amp;hide_related=true&amp;show_user=false&amp;show_comments=false&amp;visual=true"></iframe>'):
    """
    Creates a song post of `genre` with a song titled `title` by an artist `artist_name`.
    The `days` variable is offset to now (negative for posts published in the past and
    positive for posts that have yet to be published)
    """

    genre = Genre.objects.create(genre_name=genre)
    
    return SongPost.objects.create(song_title=title, artist=artist_name, genre=genre,
            soundcloud_url=soundcloud_url,
            created_on=timezone.now() + datetime.timedelta(days=days))

class SongPostCreationTests(TestCase):

    def test_create_a_new_post(self):
        """
        Creating a new post should create a database object with correct field values
        """
        create_songpost(genre="Chill", title="About You", artist_name="XXYYXX", days=0)

        posts = SongPost.objects.all()
        the_post = posts[0]

        self.assertEqual(unicode(the_post), u"About You - XXYYXX (Chill)")

    def test_soundcloud_url_is_clean(self):
        """
        When creating a new post, make sure the soundcloud_url is validated and cleaned
        correctly
        """

        bad_soundcloud_url = '<iframe width="400px" height="400px" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/57451586&amp</iframe>'

        clean_soundcloud_url = '<iframe width="100%" height="100%" scrolling="no" frameborder="no" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/57451586&amp;auto_play=false&amp;hide_related=true&amp;show_user=false&amp;show_comments=false&amp;visual=true"></iframe>'

        post = create_songpost(genre="Chill", title="About You", artist_name="XXYYXX", days=0,
                soundcloud_url=bad_soundcloud_url)

        self.assertEqual(post.soundcloud_url, clean_soundcloud_url)


    

