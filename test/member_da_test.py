from model.member import Member
from data_access.member_da import MemberDA

member_da = MemberDA()

member1 = Member(1, "Sara", "Ahmadi", 22, "09127195482", "1234567890")
member2 = Member(2, "Ali", "Mohammadi", 25, "09364562789", "9874563210")

member_da.save(member1)
member_da.save(member2)

members = member_da.find_all()

print("Number of members:", len(members))

for member in members:
    print(member.name, member.family)


found_member = member_da.find_by_id(1)

if found_member:
    print("Found member:", found_member.name, found_member.family)

else:
    print("member not found")