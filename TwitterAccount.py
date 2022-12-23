#!/usr/bin/python3
# -*- coding: utf-8 -*-
from classes.account.Account import Account


class TwitterAccount(Account):
    """
    Class which define a TwitterAccount in OPSE context
    """

    def __init__(
        self,
        username: str = None,
        email: str = None,
        id: str = None,
        name: str = None,
        bio: str = None,
        location: str = None,
        url: str = None,
        join_date: str = None,
        join_time: str = None,
        tweets_count: int = None,
        following: int = None,
        followers: int = None,
        likes: int = None,
        media_count: int = None,
        private: bool = None,
        verified: bool = None,
        avatar: str = None,
        background: str = None,
        lst_messages: list = None,
    ):
        """Constructor of an OPSE TwitterAccount"""
        super().__init__(username, url, lst_messages)
        self.__id: str = id
        self.__email: str = email
        self.__name: str = name
        self.__bio: str = bio
        self.__location: str = location
        self.__join_date: str = join_date
        self.__join_time: str = join_time
        self.__tweets_count: int = tweets_count
        self.__following: int = following
        self.__followers: int = followers
        self.__likes: int = likes
        self.__media_count: int = media_count
        self.__private: bool = private
        self.__verified: bool = verified
        self.__avatar: str = avatar
        self.__background: str = background

    def get_id(self) -> str:
        """Getter of self.__id"""
        return self.__id

    def get_email(self) -> str:
        """Getter of self.__email"""
        return self.__email

    def get_name(self) -> str:
        """Getter of self.__name"""
        return self.__name

    def get_bio(self) -> str:
        """Getter of self.__bio"""
        return self.__bio

    def get_location(self) -> str:
        """Getter of self.__location"""
        return self.__location

    def get_join_date(self) -> str:
        """Getter of self.__join_date"""
        return self.__join_date

    def get_join_time(self) -> str:
        """Getter of self.__join_time"""
        return self.__join_time

    def get_tweets_count(self) -> int:
        """Getter of self.__tweets_count"""
        return self.__tweets_count

    def get_following(self) -> int:
        """Getter of self.__following"""
        return self.__following

    def get_followers(self) -> int:
        """Getter of self.__followers"""
        return self.__followers

    def get_likes(self) -> int:
        """Getter of self.__likes"""
        return self.__likes

    def get_media_count(self) -> int:
        """Getter of self.__media_count"""
        return self.__media_count

    def get_private(self) -> bool:
        """Getter of self.__private"""
        return self.__private

    def get_verified(self) -> bool:
        """Getter of self.__verified"""
        return self.__verified

    def get_avatar(self) -> str:
        """Getter of self.__avatar"""
        return self.__avatar

    def get_background(self) -> str:
        """Getter of self.__background"""
        return self.__background
