#!/usr/bin/python3
# -*- coding: utf-8 -*-
from utils.config.Config import Config
from . import twint

from .TwitterAccount import TwitterAccount
from .TwitterMessage import TwitterMessage
from classes.Profile import Profile
from tools.Tool import Tool

from utils.datatypes import DataTypeInput
from utils.datatypes import DataTypeOutput
from utils.utils import print_debug
from utils.utils import print_error
from utils.utils import print_warning


class TwitterTool(Tool):
    """
    Class which describe a TwitterTool
    """
    deprecated = False

    def __init__(self):
        """The constructor of a TwitterTool"""
        super().__init__()

        self.__messages: list = []
        self.__users: list = []
        try:
            self.__twint_config = twint.Config()
        except Exception as e:
            print_error(" " + str(e), True)
        self.__twint_config.Store_object_tweets_list = self.__messages
        self.__twint_config.Store_object_users_list = self.__users
        self.__twint_config.Store_object = True
        self.__twint_config.Limit = Config.get().get('config', {}).get('tools', {}).get('twittertool', {}).get('tweet_limit', 0)
        self.__twint_config.Hide_output = True

    @staticmethod
    def get_config() -> dict[str]:
        """Function which return tool configuration as a dictionnary."""
        return {
            'active': True,
            'tweet_limit': 0,
        }

    @staticmethod
    def get_lst_input_data_types() -> dict[str, bool]:
        """
        Function which return the list of data types which can be use to run this Tool.
        It's will help to make decision to run Tool depending on current data.
        """
        return {
            DataTypeInput.USERNAME: True,
        }

    @staticmethod
    def get_lst_output_data_types() -> list[str]:
        """
        Function which return the list of data types which can be receive by using this Tool.
        It's will help to make decision to complete profile to get more information.
        """
        return [
            DataTypeOutput.FIRSTNAME,
            DataTypeOutput.LASTNAME,
            DataTypeOutput.LOCATION,
            DataTypeOutput.ACCOUNT,
        ]

    def execute(self):

        for username in self.get_default_profile().get_lst_usernames():

            self.__twint_config.Username = username

            try:
                # User information
                print_debug("Searching '" + self.__twint_config.Username + "' Twitter account")

                # Get tweets and retweets
                try:
                    twint.run.Profile(self.__twint_config)
                except Exception as e:
                    print_error(" " + str(e), True)

                if len(self.__messages) > 0:
                    tweets = []
                    for message in self.__messages:
                        tweet = TwitterMessage(
                            tweet_id=message.id,
                            tweet_content=message.tweet,
                            retweet=message.retweet,
                            author_id=message.auth_user_id,
                            author_name=message.auth_name,
                            author_username=message.auth_username,
                            date=message.datestamp + " " + message.timestamp,
                            timezone=message.timezone,
                            lst_urls=message.urls,
                            lst_images_urls=message.photos,
                            video=bool(message.video),
                            video_thumbnail=message.thumbnail,
                            language=message.lang,
                            lst_hashtags=message.hashtags,
                            lst_cashtags=message.cashtags,
                            replies_count=message.replies_count,
                            retweets_count=message.retweets_count,
                            likes_count=message.likes_count,
                            url=message.link
                        )
                        tweets.append(tweet)

                    print_debug(" " + str(len(self.__messages)) + " tweets found.")

                # Get profile
                try:
                    twint.run.Lookup(self.__twint_config)
                except Exception as e:
                    print_error(" " + str(e), True)

                print_debug(twint.output.users_list)
                if len(self.__users) > 0:
                    print_debug("Twitter account found for '" + username + "'")

                    profile: Profile = self.get_default_profile().clone()

                    user = self.__users[0]
                    twitter_target = TwitterAccount(
                        username=user.username,
                        id=user.id,
                        name=user.name,
                        bio=user.bio,
                        location=user.location,
                        url=user.url,
                        join_date=user.join_date,
                        join_time=user.join_time,
                        tweets_count=user.tweets,
                        following=user.following,
                        followers=user.followers,
                        likes=user.likes,
                        media_count=user.media_count,
                        private=user.is_private,
                        verified=user.is_verified,
                        avatar=user.avatar,
                        background=user.background_image,
                        lst_messages=tweets
                    )

                    profile.set_lst_accounts([twitter_target])
                    self.append_profile(profile)
                else:
                    print_warning(" No Twitter account found with username '" + username + "'")
            except Exception as e:
                print_error(" " + str(e), True)
