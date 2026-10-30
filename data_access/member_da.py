from tools.logger import Logger
import json
import os
from model.member import Member

class MemberDA:
    def __init__(self):
        self.__member_list = []
        self.__file_name = "members.json"
        if os.path.exists(self.__file_name):
            try:
                with open(self.__file_name, "r", encoding="utf-8") as file:
                    data = json.load(file)

                for item in data:
                    member = Member(item["member_id"], item["name"],
                                    item["family"], item["age"], item["mobile_number"],
                                    item["national_code"])
                    self.__member_list.append(member)

            except (json.JSONDecodeError, OSError) as error:
                Logger.error(f"Error loading members: {error}")

    def save(self, member):
        self.__member_list.append(member)

        data = []

        for item in self.__member_list:
            data.append({
                "member_id": item.member_id,
                "name": item.name,
                "family": item.family,
                "age": item.age,
                "mobile_number": item.mobile_number,
                "national_code": item.national_code}
            )
        try:
            with open(self.__file_name, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            Logger.info(f"Member saved: {member.name}")
        except OSError as error:
            Logger.error(f"Error saving member: {error}")
            raise



    def find_all(self):
        return self.__member_list

    def find_by_id(self, member_id):
        for member in self.__member_list:
            if member.member_id == member_id:
                return member
        return None
