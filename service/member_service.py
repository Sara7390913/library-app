from data_access.member_da import MemberDA
from tools.logger import Logger


class MemberService:
    def __init__(self):
        self.__member_da = MemberDA()

    def save(self, member):
        self.__member_da.save(member)
        Logger.info(f"MemberService: member saved - {member.name}")

    def find_all(self):
        return self.__member_da.find_all()

    def find_by_id(self, member_id):
        return self.__member_da.find_by_id(member_id)
