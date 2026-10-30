from model.member import Member
from service.member_service import MemberService

member_service = MemberService()

member1 = Member(1, "Sara", "Ahmadi", 22, "09127195482", "1234567890")

member_service.save(member1)

members = member_service.find_all()

print("Number of members:", len(members))


for member in members:
    print(member.name, member.family)

found_member = member_service.find_by_id(1)

if found_member:
    print("Found member:", found_member.name, found_member.family)

else:
    print("Member not found.")