import json
from typing import Union, TextIO, BinaryIO
from io import BufferedReader, BytesIO, TextIOWrapper

FileInput = Union[str, bytes, BufferedReader, BinaryIO, BytesIO, TextIO]


def parse_file_input(file: FileInput):
    if isinstance(file, str):
        if not file.endswith('.json'):
            extension = file.split('.')[-1]
            raise ValueError(f"File must be json, not {extension}")
        return json.load(open(file, "rb"))
    if isinstance(file, bytes):
        return json.loads(file.decode("utf-8"))
    if isinstance(file, BufferedReader):
        return json.load(file)
    if isinstance(file, BytesIO):
        return json.loads(file.getvalue())
    if isinstance(file, TextIOWrapper):
        return json.load(file)


class Reader:
    """
    Reader class is a wrapper around a json file. It provides methods to read the file, get the companion id, name,
    messages, messages count, file name and messages dictionary.
    """
    def __init__(self, file: FileInput):
        """
        The __init__ function is called automatically every time the class is instantiated.
        It sets up all the attributes that will be used by instances of this class.

        :param self: Reference the object itself
        :param file: :class:`str` | :class:`bytes` | :class:`BufferedReader` | \
                :class:`BytesIO` | :class:`TextIO`:
                Store the file that is used to create this object
        :raises: ValueError: If file is not a json file
        :raises: ValueError: If file is not a telegram chat history
        :raises: ValueError: If file is not a personal chat history
        :return: None
        """
        __file = parse_file_input(file)
        if not all(key in __file for key in ["id", "name", "messages"]):
            raise ValueError("Looks like you have a wrong json file or it's not a telegram chat history")
        if __file["type"] != "personal_chat":
            raise ValueError("You must use a personal chat history")

        self.__companion_id = str(__file["id"])
        self.__companion_name = str(__file["name"])
        self.__messages_dict_list = __file["messages"]
        self.__messages = self.read_messages()

    def read_messages(self) -> list:
        """
        The read_messages function reads the messages from a list of dictionaries and returns a list of strings.
        The function takes one argument, which is the list of dictionaries that contain all the messages.
        It iterates through each message in the dictionary and checks if it's from companion, if it's not empty and
        if it's a string.

        :param self: Access variables that belongs to the class
        :return: A list of all the messages sent by the companion
        """
        companion_messages = []

        for message in self.__messages_dict_list:
            message_from_id = message.get("from_id", "")
            message_is_empty = message.get("text", "") == ""
            message_is_str = isinstance(message.get("text", None), str)

            if self.__companion_id in message_from_id and not message_is_empty and message_is_str:
                companion_messages.append(message["text"])

        return companion_messages

    def get_companion_id(self) -> str:
        """
        Returns the id of the companion object.

        :param self: Access the attributes and methods of the class
        :return: The id of the companion that is currently active
        """
        return self.__companion_id

    def get_companion_name(self) -> str:
        """
        Returns the name of the companion.

        :param self: Access the attributes and methods of the class
        :return: The name of the companion
        """
        return self.__companion_name

    def get_messages(self) -> list:
        """
        Retrieves messages in a list.

        :param self: Refer to the object itself
        :return: A list of all the messages from companion
        """
        return self.__messages

    def get_messages_dict(self) -> list:
        """
        Returns a list of dictionaries, where each dictionary contains the information for one message. Basically,
        it returns the actual messages that is stored in the initial json file.

        :param self: Access the attributes and methods of the class in python
        :return: A list dictionaries with message information
        """
        return self.__messages_dict_list

    def get_messages_count(self) -> int:
        """
        Returns the number of messages in a chat.

        :param self: Access the attributes and methods of the class in python
        :return: The number of messages
        """
        return len(self.__messages)
