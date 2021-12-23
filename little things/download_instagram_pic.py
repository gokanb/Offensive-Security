import instaloader
bot = instaloader.Instaloader()
username = 'usernam'
print(bot.download_profile(username, profile_pic_only=False))