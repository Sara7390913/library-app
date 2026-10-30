from model.member import Member

member = Member(1, name="Sara", family="Hashemi", age=20, mobile_number="09127195482", national_code="1234567890")

print(member.member_id)
print(member.name)
print(member.family)
print(member.age)
print(member.mobile_number)
print(member.national_code)


member.name = "Maryam"
member.age = 25

print(member.name)
print(member.age)

#=============================================
# test invalid name pass
#=============================================
try:
    member.name = 123
except ValueError as e:
    print(e)

#=============================================
# test invalid family pass
#=============================================
try:
    member.family = 154
except ValueError as e:
    print(e)

#=============================================
# test age pass
#=============================================
try:
    member.age = -5
except ValueError as e:
    print(e)

#=============================================
# test mobile_number pass
#=============================================
try:
    member.mobile_number = "123456"
except ValueError as e:
    print(e)

#=============================================
# test national_code pass
#=============================================
try:
    member.national_code = "32648"
except ValueError as e:
    print(e)