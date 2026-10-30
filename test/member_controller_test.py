from model.member import Member
from controller.member_controller import MemberController
from test.member_service_test import found_member

member_controller = MemberController()

member1 = Member(1, "Sara", "Ahmadi", 22, "09127195482", "1234567890")

member_controller.save(member1)

members = member_controller.find_all()

print("number of members:", len(members))

for member in members:
    print(member.name, member.family)

found_member = member_controller.find_by_id(1)

if found_member:
    print("Found member:", found_member.name, found_member.family)

else:
    print("Member not found")

not_found_member = member_controller.find_by_id(999)
print("Not found:", not_found_member)