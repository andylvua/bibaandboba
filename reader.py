import json


class Reader:
    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__file = json.load(open(file_name, "rb"))
        self.__companion_id = str(self.__file["id"])
        self.__companion_name = str(self.__file["name"])
        self.__messages_dict_list = self.__file["messages"]
        self.__messages = self.read_messages()

    def read_messages(self) -> list:
        companion_messages = []

        for message in self.__messages_dict_list:
            message_from_id = message.get("from_id", "")
            message_is_empty = message.get("text", "") == ""
            message_is_str = isinstance(message.get("text", None), str)

            if self.__companion_id in message_from_id and not message_is_empty and message_is_str:
                companion_messages.append(message["text"])

        return companion_messages

    def get_companion_id(self) -> str:
        return self.__companion_id

    def get_companion_name(self) -> str:
        return self.__companion_name

    def get_messages(self) -> list:
        return self.__messages

    def get_messages_dict(self) -> list:
        return self.__messages_dict_list

    def get_messages_count(self) -> int:
        return len(self.__messages)

    def get_file_name(self) -> str:
        return self.__file_name
