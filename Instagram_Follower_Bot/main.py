from follower import Instagram_Follower


if __name__ == "__main__":

    bot = Instagram_Follower()

    #login into twitter
    bot.login()

    #find target account  
    #follow target account followers
    bot.find_followers()