from complain_bot import InternetSpeedTwitterBot


if __name__ == "__main__":

    bot = InternetSpeedTwitterBot()

    try:
        bot.get_internet_speed()
    except Exception as ex:
        print(str(ex))