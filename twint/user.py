# -*- coding: utf-8 -*-
import datetime
import logging as logme


class user:
    type = "user"

    def __init__(self):
        pass


User_formats = {"join_date": "%Y-%m-%d", "join_time": "%H:%M:%S %Z"}


# ur object must be a json from the endpoint https://api.twitter.com/graphql
def User(ur):
    logme.debug(__name__ + ":User")
    if "data" not in ur and "user" not in ur["data"]:
        msg = "malformed json! cannot be parsed to get user data"
        logme.fatal(msg)
        raise KeyError(msg)
    _usr = user()

    # ***
    # OPSE Project : Fix "url" issue on Lookup twint#1003

    # :type `str`
    try:
        _usr.id = ur["data"]["user"]["rest_id"]
    except:
        _usr.id = ""
    try:
        _usr.name = ur["data"]["user"]["legacy"]["name"]
    except:
        _usr.name = ""
    try:
        _usr.username = ur["data"]["user"]["legacy"]["screen_name"]
    except:
        _usr.username = ""
    try:
        _usr.bio = ur["data"]["user"]["legacy"]["description"]
    except:
        _usr.bio = ""
    try:
        _usr.location = ur["data"]["user"]["legacy"]["location"]
    except:
        _usr.location = ""
    try:
        _usr.url = ur["data"]["user"]["legacy"]["url"]
    except:
        _usr.url = ""

    # :type `datetime`
    try:
        # parsing date to user-friendly format
        _dt = ur["data"]["user"]["legacy"]["created_at"]
        _dt = datetime.datetime.strptime(_dt, "%a %b %d %H:%M:%S %z %Y")
        # date is of the format year,
        _usr.join_date = _dt.strftime(User_formats["join_date"])
        _usr.join_time = _dt.strftime(User_formats["join_time"])
    except:
        _usr.join_date = ""
        _usr.join_time = ""

    # :type `int`
    try:
        _usr.tweets = int(ur["data"]["user"]["legacy"]["statuses_count"])
    except:
        _usr.tweets = 0
    try:
        _usr.following = int(ur["data"]["user"]["legacy"]["friends_count"])
    except:
        _usr.following = 0
    try:
        _usr.followers = int(ur["data"]["user"]["legacy"]["followers_count"])
    except:
        _usr.followers = 0
    try:
        _usr.likes = int(ur["data"]["user"]["legacy"]["favourites_count"])
    except:
        _usr.likes = 0
    try:
        _usr.media_count = int(ur["data"]["user"]["legacy"]["media_count"])
    except:
        _usr.media_count = 0

    # :type `bool`
    try:
        _usr.is_private = ur["data"]["user"]["legacy"]["protected"]
    except:
        _usr.is_private = False
    try:
        _usr.is_verified = ur["data"]["user"]["legacy"]["verified"]
    except:
        _usr.is_verified = False

    # :type `str`
    try:
        _usr.avatar = ur["data"]["user"]["legacy"]["profile_image_url_https"]
    except:
        _usr.avatar = ""
    try:
        _usr.background_image = ur["data"]["user"]["legacy"]["profile_banner_url"]
    except:
        _usr.background_image = ""
    # ***

    # TODO : future implementation
    # legacy_extended_profile is also available in some cases which can be used to get DOB of user
    return _usr
