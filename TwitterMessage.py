#!/usr/bin/python3
# -*- coding: utf-8 -*-
from datetime import date

from classes.message.Message import Message


class TwitterMessage(Message):
    """
    Class which define a TwitterMessage in OPSE context
    """

    def __init__(
        self,
        tweet_id: int,
        tweet_content: str,
        retweet: bool,
        author_id: int,
        author_name: str,
        author_username: str,
        date: date,
        timezone: str,
        lst_urls: list[str],
        lst_images_urls: list[str],
        video: bool,
        video_thumbnail: str,
        language: str,
        lst_hashtags: list[str],
        lst_cashtags: list[str],
        replies_count: int,
        retweets_count: int,
        likes_count: int,
        url: str,
        mentions = None,
        replies = None,
    ):
        """Constructor of an OPSE TwitterMessage"""
        super().__init__(tweet_content, author_name)
        self.__tweet_id = tweet_id
        self.__retweet = retweet
        self.__author_id = author_id
        self.__author_username = author_username
        self.__date = date
        self.__timezone = timezone
        self.__lst_urls = lst_urls
        self.__lst_images_urls = lst_images_urls
        self.__video = video
        self.__video_thumbnail = video_thumbnail
        self.__language = language
        self.__lst_hashtags = lst_hashtags
        self.__lst_cashtags = lst_cashtags
        self.__replies_count = replies_count
        self.__retweets_count = retweets_count
        self.__likes_count = likes_count
        self.__url = url
        # self.__mentions = mentions
        # self.__replies = replies

    def get_tweet_id(self) -> int:
        """Getter of self.__tweet_id"""
        return self.__tweet_id

    def get_retweet(self) -> bool:
        """Getter of self.__retweet"""
        return self.__retweet

    def get_author_id(self) -> int:
        """Getter of self.__author_id"""
        return self.__author_id

    def get_author_username(self) -> str:
        """Getter of self.__author_username"""
        return self.__author_username

    def get_date(self) -> str:
        """Getter of self.__date"""
        return self.__date

    def get_timezone(self) -> str:
        """Getter of self.__timezone"""
        return self.__timezone

    def get_lst_urls(self) -> list[str]:
        """Getter of self.__lst_urls"""
        return self.__lst_urls

    def get_lst_images_urls(self) -> list[str]:
        """Getter of self.__lst_images_urls"""
        return self.__lst_images_urls

    def get_video(self) -> bool:
        """Getter of self.__video"""
        return self.__video

    def get_video_thumbnail(self) -> str:
        """Getter of self.__video_thumbnail"""
        return self.__video_thumbnail

    def get_language(self) -> str:
        """Getter of self.__language"""
        return self.__language

    def get_lst_hashtags(self) -> list[str]:
        """Getter of self.__lst_hashtags"""
        return self.__lst_hashtags

    def get_lst_cashtags(self) -> list[str]:
        """Getter of self.__lst_cashtags"""
        return self.__lst_cashtags

    def get_replies_count(self) -> int:
        """Getter of self.__replies_count"""
        return self.__replies_count

    def get_retweets_count(self) -> int:
        """Getter of self.__retweets_count"""
        return self.__retweets_count

    def get_likes_count(self) -> int:
        """Getter of self.__likes_count"""
        return self.__likes_count

    def get_url(self) -> str:
        """Getter of self.__url"""
        return self.__url

    # def get_mentions(self) -> list:
    #     """Getter of self.__mentions"""
    #     return self.__mentions

    # def get_replies(self) -> list:
    #     """Getter of self.__replies"""
    #     return self.__replies
