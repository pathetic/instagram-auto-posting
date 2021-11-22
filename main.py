import os
import sys
import threading
import time
import config

from glob import glob

sys.path.append(os.path.join(sys.path[0], "../../"))
import schedule
from instabot import Bot, utils

bot = Bot()

bot.login(username=config.USERNAME, password=config.PASSWORD)
bot.logger.info("ULTIMATE script. Safe to run 24/7!")

posted_pic_list = utils.file(config.POSTED_PICS_FILE).list

pics = sorted([os.path.basename(x) for x in glob(config.PICS_PATH + "/*.jpg")])

def upload_pictures():
    try:
        for pic in pics:
            if pic in posted_pic_list:
                continue

            bot.logger.info("Uploading " + pic)
            bot.upload_photo(config.PICS_PATH + pic, caption="")
            if bot.api.last_response.status_code != 200:
                bot.logger.error("Something went wrong, read the following ->\n")
                bot.logger.error(bot.api.last_response)
                break

            if pic not in posted_pic_list:
                posted_pic_list.append(pic)
                with open("pics.txt", "a") as f:
                    f.write(pic + "\n")
                bot.logger.info("Succesfully uploaded: " + pic)
                break
    except Exception as e:
        bot.logger.error("Couldn't upload pic")
        bot.logger.error(str(e))

def run_threaded(job_fn):
    job_thread = threading.Thread(target=job_fn)
    job_thread.start()

schedule.every(4).hours.do(run_threaded, upload_pictures)

while True:
    schedule.run_pending()
    time.sleep(1)
