from TelegramBotAPI.types.type import Type
from TelegramBotAPI.types.field import Field
from TelegramBotAPI.types.primitive import Integer, String, Boolean, Float, InputFile
from TelegramBotAPI.types.compound import ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply


class sendMessage(Type):
    chat_id = Field(Integer)
    text = Field(String)
    disable_web_page_preview = Field(Boolean, optional=True)
    reply_to_message_id = Field(Integer, optional=True)
    reply_markup = Field(ReplyKeyboardHide, ReplyKeyboardMarkup, ForceReply, optional=True)


class getUpdates(Type):
    offset = Field(Integer, optional=True)
    limit = Field(Integer, optional=True)
    timeout = Field(Integer, optional=True)


class setWebhook(Type):
    url = Field(String)


class getMe(Type):
    chat_id = Field(Integer, optional=True)
    text = Field(String, optional=True)
    disable_web_page_preview = Field(Boolean)
    reply_to_message_id = Field(Integer)
    reply_markup = Field(ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply)


class forwardMessage(Type):
    chat_id = Field(Integer, optional=True)
    from_chat_id = Field(Integer, optional=True)
    message_id = Field(Integer, optional=True)


class sendPhoto(Type):
    chat_id = Field(Integer, optional=True)
    photo = Field(InputFile, String, optional=True)
    caption = Field(String)
    reply_to_message_id = Field(Integer)
    reply_markup = Field(ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply)


class sendAudio(Type):
    chat_id = Field(Integer, optional=True)
    audio = Field(InputFile, String, optional=True)
    reply_to_message_id = Field(Integer)
    reply_markup = Field(ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply)


class sendDocument(Type):
    chat_id = Field(Integer, optional=True)
    document = Field(InputFile, String, optional=True)
    reply_to_message_id = Field(Integer)
    reply_markup = Field(ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply)


class sendSticker(Type):
    chat_id = Field(Integer, optional=True)
    sticker = Field(InputFile, String, optional=True)
    reply_to_message_id = Field(Integer)
    reply_markup = Field(ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply)


class sendVideo(Type):
    chat_id = Field(Integer, optional=True)
    video = Field(InputFile, String, optional=True)
    reply_to_message_id = Field(Integer)
    reply_markup = Field(ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply)


class sendLocation(Type):
    chat_id = Field(Integer, optional=True)
    latitude = Field(Float, optional=True)
    longitude = Field(Float, optional=True)
    reply_to_message_id = Field(Integer)
    reply_markup = Field(ReplyKeyboardMarkup, ReplyKeyboardHide, ForceReply)


class sendChatAction(Type):
    chat_id = Field(Integer, optional=True)
    action = Field(String, optional=True)


class getUserProfilePhotos(Type):
    user_id = Field(Integer, optional=True)
    offset = Field(Integer)
    limit = Field(Integer)
