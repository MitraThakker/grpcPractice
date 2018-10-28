import grpc

from compiled_protos.user_ops_pb2 import (CreateUserRequest,
                                          GetUserRequest,
                                          UpdateUserRequest,
                                          DeleteUserRequest,
                                          User,
                                          UserResponse)
from compiled_protos.user_ops_pb2_grpc import UserOpsStub


class UserClient:
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50001
        self.channel = grpc.insecure_channel(f'{self.host}:{self.server_port}')
        self.stub = UserOpsStub(self.channel)

    def create_user(self, request: CreateUserRequest) -> UserResponse:
        return self.stub.create_user(request)

    def get_user(self, request: GetUserRequest) -> UserResponse:
        return self.stub.get_user(request)

    def update_user(self, request: UpdateUserRequest) -> UserResponse:
        return self.stub.update_user(request)

    def delete_user(self, request: DeleteUserRequest) -> UserResponse:
        return self.stub.delete_user(request)


if __name__ == '__main__':
    user_client = UserClient()

    user_ = User(name='Mitra Thakker', gender=2)
    create_user_request = CreateUserRequest(user=user_)
    create_user_response = user_client.create_user(create_user_request)
    print(f'Create User Response: {create_user_response}')

    user_id = create_user_response.user.id
    get_user_request = GetUserRequest(id=user_id)
    get_user_response = user_client.get_user(get_user_request)
    print(f'Get User Response: {get_user_response}')

    user_ = User(id=user_id, name='Dashmit Dassan', gender=1)
    update_user_request = UpdateUserRequest(user=user_)
    update_user_response = user_client.update_user(update_user_request)
    print(f'Update User Response: {update_user_response}')

    user_id = get_user_response.user.id
    get_user_request = GetUserRequest(id=user_id)
    get_user_response = user_client.get_user(get_user_request)
    print(f'Get User Response: {get_user_response}')

    user_id = get_user_response.user.id
    delete_user_request = DeleteUserRequest(id=user_id)
    delete_user_response = user_client.delete_user(delete_user_request)
    print(f'Delete User Response: {delete_user_response}')

    user_id = get_user_response.user.id
    get_user_request = GetUserRequest(id=user_id)
    get_user_response = user_client.get_user(get_user_request)
    print(f'Get User Response: {get_user_response}')
