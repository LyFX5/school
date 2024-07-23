
from urllib.request import urlopen
import json
from urllib.error import HTTPError
from tqdm import tqdm


class VideoLoader:
    def __init__(self):
        self.VideosLang = 'ru'

    def get_link_to_video(self, video: str) -> str:
        # takes the ted page with video
        # returns the link of the video for HTML

        s = video.find("https://py.tedcdn.com")
        e = video.find('.mp4')

        link = ''
        for i in range(s, e + 4):
            link += video[i]

        return link

    def download_ted_video_and_subs(self, VideoID, Videolang):

        subs_json_domain = f"https://www.ted.com/talks/subtitles/id/{VideoID}/lang/{Videolang}"
        video_domain = f"https://www.ted.com/talks/{VideoID}"

        subs_json = None
        video = None

        try:
            subs_json = urlopen((subs_json_domain))
            video = urlopen(video_domain)
        except HTTPError as e:
            return None

        assert video != None and subs_json != None

        subs_json = subs_json.read().decode('utf8')
        video = video.read().decode('utf8')

        subs_json_dictionary = json.loads(subs_json)

        link_to_video = self.get_link_to_video(video)

        list_of_rows = []

        for caption in subs_json_dictionary['captions']:
            row = (VideoID, link_to_video, caption['duration'], caption['content'], caption['startOfParagraph'], caption['startTime'])
            list_of_rows.append(row)

        return list_of_rows

    def download_videos(self, videos_ids, videos_langs):

        videos = []
        not_loaded_videos_ids = []

        for ID, lang in tqdm(zip(videos_ids, videos_langs)):
            list_of_rows = self.download_ted_video_and_subs(ID, lang)
            if list_of_rows == None:
                not_loaded_videos_ids.append(ID)
            else:
                videos.append(list_of_rows)

        print(f'All videos were downloaded except {not_loaded_videos_ids}.')

        return [videos, not_loaded_videos_ids]

