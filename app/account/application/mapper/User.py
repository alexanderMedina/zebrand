from app.account.application.dto.User import UserDto
from app.account.domain.model.User import User

class UserMapper():

    def fromDomainToDto(user: User):
        
        user = UserDto(
            id=user.id, 
            name=user.name, 
            email=user.email,
            admin=user.admin
        )

        return user

    def fromDtoToDomain(user: UserDto):
        user_dict = user.dict()
        product = User(**user_dict)
        return product