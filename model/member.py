class Member:
    def __init__(self, member_id, name, age):
        self.member_id = member_id
        self.name = name
        self.age = age

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
        if not isinstance(name, str):
            raise ValueError("Invalid Member Name.")
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        try:
            age = int(age)
            if 1 <= age <= 120:
                self.__age = age
            else:
                raise ValueError("Age must be between 1 and 120.")
        except (ValueError, TypeError):
            raise ValueError("Invalid Member Age.")






