class MemberDA:
    def __init__(self):
        self.__member_list = []


    def save(self, member):
        self.__member_list.append(member)


    def find_all(self):
        return self.__member_list

    def find_by_id(self, member_id):
        for member in self.__member_list:
            if member.member_id == member_id:
                return member
        return None
