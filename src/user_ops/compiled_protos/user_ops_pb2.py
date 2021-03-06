# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_ops.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_ops.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0euser_ops.proto\"f\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1c\n\x06gender\x18\x03 \x01(\x0e\x32\x0c.User.Gender\"&\n\x06Gender\x12\x06\n\x02NA\x10\x00\x12\n\n\x06\x46\x45MALE\x10\x01\x12\x08\n\x04MALE\x10\x02\"(\n\x11\x43reateUserRequest\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\"\x1c\n\x0eGetUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\"(\n\x11UpdateUserRequest\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x8e\x01\n\x0cUserResponse\x12\x13\n\x04user\x18\x01 \x01(\x0b\x32\x05.User\x12,\n\x06status\x18\x02 \x01(\x0e\x32\x1c.UserResponse.ResponseStatus\x12\x0f\n\x07message\x18\x03 \x01(\t\"*\n\x0eResponseStatus\x12\x0b\n\x07SUCCESS\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\x32\xd3\x01\n\x07UserOps\x12\x32\n\x0b\x63reate_user\x12\x12.CreateUserRequest\x1a\r.UserResponse\"\x00\x12,\n\x08get_user\x12\x0f.GetUserRequest\x1a\r.UserResponse\"\x00\x12\x32\n\x0bupdate_user\x12\x12.UpdateUserRequest\x1a\r.UserResponse\"\x00\x12\x32\n\x0b\x64\x65lete_user\x12\x12.DeleteUserRequest\x1a\r.UserResponse\"\x00\x62\x06proto3')
)



_USER_GENDER = _descriptor.EnumDescriptor(
  name='Gender',
  full_name='User.Gender',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NA', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MALE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=82,
  serialized_end=120,
)
_sym_db.RegisterEnumDescriptor(_USER_GENDER)

_USERRESPONSE_RESPONSESTATUS = _descriptor.EnumDescriptor(
  name='ResponseStatus',
  full_name='UserResponse.ResponseStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=370,
  serialized_end=412,
)
_sym_db.RegisterEnumDescriptor(_USERRESPONSE_RESPONSESTATUS)


_USER = _descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='User.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='User.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='User.gender', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USER_GENDER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=120,
)


_CREATEUSERREQUEST = _descriptor.Descriptor(
  name='CreateUserRequest',
  full_name='CreateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='CreateUserRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=162,
)


_GETUSERREQUEST = _descriptor.Descriptor(
  name='GetUserRequest',
  full_name='GetUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='GetUserRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=164,
  serialized_end=192,
)


_UPDATEUSERREQUEST = _descriptor.Descriptor(
  name='UpdateUserRequest',
  full_name='UpdateUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='UpdateUserRequest.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=234,
)


_DELETEUSERREQUEST = _descriptor.Descriptor(
  name='DeleteUserRequest',
  full_name='DeleteUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='DeleteUserRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=236,
  serialized_end=267,
)


_USERRESPONSE = _descriptor.Descriptor(
  name='UserResponse',
  full_name='UserResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='UserResponse.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='UserResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='UserResponse.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USERRESPONSE_RESPONSESTATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=270,
  serialized_end=412,
)

_USER.fields_by_name['gender'].enum_type = _USER_GENDER
_USER_GENDER.containing_type = _USER
_CREATEUSERREQUEST.fields_by_name['user'].message_type = _USER
_UPDATEUSERREQUEST.fields_by_name['user'].message_type = _USER
_USERRESPONSE.fields_by_name['user'].message_type = _USER
_USERRESPONSE.fields_by_name['status'].enum_type = _USERRESPONSE_RESPONSESTATUS
_USERRESPONSE_RESPONSESTATUS.containing_type = _USERRESPONSE
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['CreateUserRequest'] = _CREATEUSERREQUEST
DESCRIPTOR.message_types_by_name['GetUserRequest'] = _GETUSERREQUEST
DESCRIPTOR.message_types_by_name['UpdateUserRequest'] = _UPDATEUSERREQUEST
DESCRIPTOR.message_types_by_name['DeleteUserRequest'] = _DELETEUSERREQUEST
DESCRIPTOR.message_types_by_name['UserResponse'] = _USERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

User = _reflection.GeneratedProtocolMessageType('User', (_message.Message,), dict(
  DESCRIPTOR = _USER,
  __module__ = 'user_ops_pb2'
  # @@protoc_insertion_point(class_scope:User)
  ))
_sym_db.RegisterMessage(User)

CreateUserRequest = _reflection.GeneratedProtocolMessageType('CreateUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEUSERREQUEST,
  __module__ = 'user_ops_pb2'
  # @@protoc_insertion_point(class_scope:CreateUserRequest)
  ))
_sym_db.RegisterMessage(CreateUserRequest)

GetUserRequest = _reflection.GeneratedProtocolMessageType('GetUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETUSERREQUEST,
  __module__ = 'user_ops_pb2'
  # @@protoc_insertion_point(class_scope:GetUserRequest)
  ))
_sym_db.RegisterMessage(GetUserRequest)

UpdateUserRequest = _reflection.GeneratedProtocolMessageType('UpdateUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUSERREQUEST,
  __module__ = 'user_ops_pb2'
  # @@protoc_insertion_point(class_scope:UpdateUserRequest)
  ))
_sym_db.RegisterMessage(UpdateUserRequest)

DeleteUserRequest = _reflection.GeneratedProtocolMessageType('DeleteUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEUSERREQUEST,
  __module__ = 'user_ops_pb2'
  # @@protoc_insertion_point(class_scope:DeleteUserRequest)
  ))
_sym_db.RegisterMessage(DeleteUserRequest)

UserResponse = _reflection.GeneratedProtocolMessageType('UserResponse', (_message.Message,), dict(
  DESCRIPTOR = _USERRESPONSE,
  __module__ = 'user_ops_pb2'
  # @@protoc_insertion_point(class_scope:UserResponse)
  ))
_sym_db.RegisterMessage(UserResponse)



_USEROPS = _descriptor.ServiceDescriptor(
  name='UserOps',
  full_name='UserOps',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=415,
  serialized_end=626,
  methods=[
  _descriptor.MethodDescriptor(
    name='create_user',
    full_name='UserOps.create_user',
    index=0,
    containing_service=None,
    input_type=_CREATEUSERREQUEST,
    output_type=_USERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_user',
    full_name='UserOps.get_user',
    index=1,
    containing_service=None,
    input_type=_GETUSERREQUEST,
    output_type=_USERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='update_user',
    full_name='UserOps.update_user',
    index=2,
    containing_service=None,
    input_type=_UPDATEUSERREQUEST,
    output_type=_USERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='delete_user',
    full_name='UserOps.delete_user',
    index=3,
    containing_service=None,
    input_type=_DELETEUSERREQUEST,
    output_type=_USERRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_USEROPS)

DESCRIPTOR.services_by_name['UserOps'] = _USEROPS

# @@protoc_insertion_point(module_scope)
