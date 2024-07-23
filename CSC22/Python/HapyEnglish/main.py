
from db_api import TableManager
from loading_api import VideoLoader

if __name__ == "__main__":

    # create table
    table_manager = TableManager()  # create table_manager object

    table_manager.create_connection()
    table_manager.create_cursor()
    table_manager.create_table()
    print("table_manager")
    # work with table

        # download videos
    # video_loader = VideoLoader()  # create loader object
    #
    # videos_ids = list(range(1, 11))
    # videos_langs = ['en'] * 10
    # [videos, not_loaded_videos_ids] = video_loader.download_videos(videos_ids, videos_langs)
    # print("video_loader")
    #     # upload videos to tabel
    # table_manager.upload_videos_to_table(videos)  # субтитры загрузятся, если не были до сих пор загружены

    # close table
    table_manager.save_changes()
    table_manager.close_connection()

    print("web_app")
    # seqrch something in table via web interface
    from web_app import app
    app.run(host="0.0.0.0",  port=5000)






