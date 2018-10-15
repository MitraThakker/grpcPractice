import grpc
import logging
import time
import user_ops_pb2
import user_ops_pb2_grpc

from concurrent import futures
from uuid import uuid4

logging.basicConfig(
    level=logging.INFO
)


class UserService(user_ops_pb2_grpc.UserOpsServicer):
    def __init__(self):
        self.server_port = 50001
        self.users = dict()

    def create_user(self, request: user_ops_pb2.CreateUserRequest, context) -> user_ops_pb2.UserResponse:
        user_: user_ops_pb2.User = request.user
        user_.id = user_.id or str(uuid4())
        if user_.id in self.users:
            return user_ops_pb2.UserResponse(user=user_, status=1, message=f'User {user_.id} exists!')
        self.users[user_.id] = user_
        return user_ops_pb2.UserResponse(user=user_, message=f'ID: {user_.id}')

    def get_user(self, request: user_ops_pb2.GetUserRequest, context) -> user_ops_pb2.UserResponse:
        user_id = request.id
        if user_id in self.users:
            return user_ops_pb2.UserResponse(user=self.users[user_id])
        return user_ops_pb2.UserResponse(status=1, message=f'User {user_id} does not exist!')

    def update_user(self, request: user_ops_pb2.UpdateUserRequest, context) -> user_ops_pb2.UserResponse:
        user_id = request.user.id
        if user_id in self.users:
            self.users[user_id] = request.user
            return user_ops_pb2.UserResponse(user=self.users[user_id], message=f'Updated user {user_id}!')
        return user_ops_pb2.UserResponse(status=1, message=f'User {user_id} does not exist!')

    def delete_user(self, request: user_ops_pb2.DeleteUserRequest, context) -> user_ops_pb2.UserResponse:
        user_id = request.id
        if user_id in self.users:
            user_ = self.users[user_id]
            del self.users[user_id]
            return user_ops_pb2.UserResponse(user=user_, message=f'Deleted user {user_id}!')
        return user_ops_pb2.UserResponse(status=1, message=f'User {user_id} does not exist!')

    def serve(self):
        server_ = grpc.server(futures.ThreadPoolExecutor())
        user_ops_pb2_grpc.add_UserOpsServicer_to_server(UserService(), server_)
        server_.add_insecure_port(f'[::]:{self.server_port}')
        server_.start()
        logging.info('UserService is running...')

        try:
            while True:
                time.sleep(60 * 60 * 24)
        except KeyboardInterrupt:
            server_.stop(0)
            logging.warning('UserService stopped!')


if __name__ == '__main__':
    user_service = UserService()
    user_service.serve()
