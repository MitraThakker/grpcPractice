import grpc
import user_ops_pb2
import user_ops_pb2_grpc


class UserClient:
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50001
        self.channel = grpc.insecure_channel(f'{self.host}:{self.server_port}')
        self.stub = user_ops_pb2_grpc.UserOpsStub(self.channel)

    def create_user(self, request: user_ops_pb2.CreateUserRequest) -> user_ops_pb2.UserResponse:
        return self.stub.create_user(request)

    def get_user(self, request: user_ops_pb2.GetUserRequest) -> user_ops_pb2.UserResponse:
        return self.stub.get_user(request)

    def update_user(self, request: user_ops_pb2.UpdateUserRequest) -> user_ops_pb2.UserResponse:
        return self.stub.update_user(request)

    def delete_user(self, request: user_ops_pb2.DeleteUserRequest) -> user_ops_pb2.UserResponse:
        return self.stub.delete_user(request)


if __name__ == '__main__':
    user_client = UserClient()

    user_ = user_ops_pb2.User(name='Mitra Thakker', gender=2)
    create_user_request = user_ops_pb2.CreateUserRequest(user=user_)
    create_user_response = user_client.create_user(create_user_request)
    print(f'Create User Response: {create_user_response}')

    user_id = create_user_response.user.id
    get_user_request = user_ops_pb2.GetUserRequest(id=user_id)
    get_user_response = user_client.get_user(get_user_request)
    print(f'Get User Response: {get_user_response}')

    user_ = user_ops_pb2.User(id=user_id, name='Dashmit Dassan', gender=1)
    update_user_request = user_ops_pb2.UpdateUserRequest(user=user_)
    update_user_response = user_client.update_user(update_user_request)
    print(f'Update User Response: {update_user_response}')

    user_id = get_user_response.user.id
    get_user_request = user_ops_pb2.GetUserRequest(id=user_id)
    get_user_response = user_client.get_user(get_user_request)
    print(f'Get User Response: {get_user_response}')

    user_id = get_user_response.user.id
    delete_user_request = user_ops_pb2.DeleteUserRequest(id=user_id)
    delete_user_response = user_client.delete_user(delete_user_request)
    print(f'Delete User Response: {delete_user_response}')

    user_id = get_user_response.user.id
    get_user_request = user_ops_pb2.GetUserRequest(id=user_id)
    get_user_response = user_client.get_user(get_user_request)
    print(f'Get User Response: {get_user_response}')
