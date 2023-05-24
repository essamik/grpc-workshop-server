from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EmployeeCreationRequest(_message.Message):
    __slots__ = ["birthday", "firstName", "gender", "lastName"]
    BIRTHDAY_FIELD_NUMBER: _ClassVar[int]
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    birthday: str
    firstName: str
    gender: str
    lastName: str
    def __init__(self, firstName: _Optional[str] = ..., lastName: _Optional[str] = ..., gender: _Optional[str] = ..., birthday: _Optional[str] = ...) -> None: ...

class EmployeeCreationResponse(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class MedianAgeResponse(_message.Message):
    __slots__ = ["Age"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    Age: int
    def __init__(self, Age: _Optional[int] = ...) -> None: ...

class MessageRequest(_message.Message):
    __slots__ = ["text"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class MessageResponse(_message.Message):
    __slots__ = ["text"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...
