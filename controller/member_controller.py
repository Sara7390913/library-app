from service.member_service import MemberService
from tools.logger import Logger


class MemberController:
    def __init__(self):
        self.member_service = MemberService()

    def save(self, member):
        try:
            self.member_service.save(member)
            Logger.info("MemberController: member saved successfully")
        except (ValueError, TypeError) as e:
            Logger.error(f"Error saving member: {e}")
            raise

    def find_all(self):
        try:
            return self.member_service.find_all()
        except Exception as e:
            Logger.error(f"Error finding member: {e}")
            raise

    def find_by_id(self, member_id):
        try:
            return self.member_service.find_by_id(member_id)
        except Exception as e:
            Logger.error(f"Error finding member by ID: {e}")
            raise
