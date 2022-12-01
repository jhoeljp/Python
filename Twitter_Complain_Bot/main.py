from complain_bot import InternetSpeedTwitterBot


if __name__ == "__main__":

    bot = InternetSpeedTwitterBot()

    try:
        #get internet speed and ISP 
        info = bot.get_internet_speed()

        #compose messsage to tweet 
        Complain = f"Hello {info['ISP_Name']}, why is my interent speed {info['Download']}down/{info['Upload']}up when I am paying for "

        #login and send tweet
        bot.tweet_at_provider(Complain,info['Download'])

    except Exception as ex:
        print(str(ex))