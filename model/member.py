from tools.logger import Logger
from tools.validation import (name_validator, family_validator, age_validator, mobile_number_validator,
                              national_code_validator)


class Member:
    def __init__(self, member_id, name, family, age, mobile_number, national_code):
        self.member_id = member_id
        self.name = name
        self.family = family
        self.age = age
        self.mobile_number = mobile_number
        self.national_code = national_code
        Logger.info(f"Member created: {self.name}")


    @property
    def member_id(self):
        return self.__member_id

    @member_id.setter
    def member_id(self, member_id):
        try:
            member_id = int(member_id)
            if member_id > 0:
                self.__member_id = member_id
            else:
                raise ValueError("Member ID must be positive.")

        except (ValueError, TypeError):
            raise ValueError("Invalid Member ID.")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        name_validator(name)
        self.__name = name

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, family):
        family_validator(family)
        self.__family = family

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        age_validator(age)
        self.__age = age

    @property
    def mobile_number(self):
        return self.__mobile_number

    @mobile_number.setter
    def mobile_number(self, mobile_number):
        mobile_number_validator(mobile_number)
        self.__mobile_number = mobile_number

    @property
    def national_code(self):
        return self.__national_code

    @national_code.setter
    def national_code(self, national_code):
        national_code_validator(national_code)
        self.__national_code = national_code
