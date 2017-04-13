from common.database import Database


class Video(object):
    def __init__(self, account, title, link, img):
        self.account = account
        self.title = title
        self.link = link
        self.img = img

    def save_to_db(self):
        Database.insert(collection='videos', data=self.json())

    def json(self):
        return {
            "account": self.account,
            "title": self.title,
            "link": self.link,
            "img": self.img
        }

    def find_video(account):
        user_video = Database.find(collection='videos', query={"account": account})
        return user_video

    def delete_video(account, link):
        Database.remove(collection='videos', query={"account": account, "link": link})
