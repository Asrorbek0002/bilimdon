from datetime import date

from  pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    birthdate: date

dummy_date = {
    'id': 1,
    'first_name': 'Jone',
    'last_name': 'Leo',
    'username': 'jone_leo',
    'birthdate': date(year=2000, month=1, day=1)
}

user = UserSchema(**dummy_date)
user_dict = user.model_dump()
user_dict['is_user'] = True
print(user_dict)

















