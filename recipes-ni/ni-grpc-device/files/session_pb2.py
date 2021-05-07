# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: session.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='session.proto',
  package='nidevice_grpc',
  syntax='proto3',
  serialized_pb=_b('\n\rsession.proto\x12\rnidevice_grpc\"2\n\x07Session\x12\x0e\n\x04name\x18\x01 \x01(\tH\x00\x12\x0c\n\x02id\x18\x02 \x01(\rH\x00\x42\t\n\x07session\"V\n\x10\x44\x65viceProperties\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05model\x18\x02 \x01(\t\x12\x0e\n\x06vendor\x18\x03 \x01(\t\x12\x15\n\rserial_number\x18\x04 \x01(\t\"\x19\n\x17\x45numerateDevicesRequest\"L\n\x18\x45numerateDevicesResponse\x12\x30\n\x07\x64\x65vices\x18\x01 \x03(\x0b\x32\x1f.nidevice_grpc.DeviceProperties\";\n\x0eReserveRequest\x12\x16\n\x0ereservation_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\"&\n\x0fReserveResponse\x12\x13\n\x0bis_reserved\x18\x01 \x01(\x08\"F\n\x19IsReservedByClientRequest\x12\x16\n\x0ereservation_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\"1\n\x1aIsReservedByClientResponse\x12\x13\n\x0bis_reserved\x18\x01 \x01(\x08\"=\n\x10UnreserveRequest\x12\x16\n\x0ereservation_id\x18\x01 \x01(\t\x12\x11\n\tclient_id\x18\x02 \x01(\t\"*\n\x11UnreserveResponse\x12\x15\n\ris_unreserved\x18\x01 \x01(\x08\"\x14\n\x12ResetServerRequest\".\n\x13ResetServerResponse\x12\x17\n\x0fis_server_reset\x18\x01 \x01(\x08\x32\xd2\x03\n\x10SessionUtilities\x12\x63\n\x10\x45numerateDevices\x12&.nidevice_grpc.EnumerateDevicesRequest\x1a\'.nidevice_grpc.EnumerateDevicesResponse\x12H\n\x07Reserve\x12\x1d.nidevice_grpc.ReserveRequest\x1a\x1e.nidevice_grpc.ReserveResponse\x12i\n\x12IsReservedByClient\x12(.nidevice_grpc.IsReservedByClientRequest\x1a).nidevice_grpc.IsReservedByClientResponse\x12N\n\tUnreserve\x12\x1f.nidevice_grpc.UnreserveRequest\x1a .nidevice_grpc.UnreserveResponse\x12T\n\x0bResetServer\x12!.nidevice_grpc.ResetServerRequest\x1a\".nidevice_grpc.ResetServerResponseBB\n\x12\x63om.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')
)




_SESSION = _descriptor.Descriptor(
  name='Session',
  full_name='nidevice_grpc.Session',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='nidevice_grpc.Session.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='nidevice_grpc.Session.id', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='session', full_name='nidevice_grpc.Session.session',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=32,
  serialized_end=82,
)


_DEVICEPROPERTIES = _descriptor.Descriptor(
  name='DeviceProperties',
  full_name='nidevice_grpc.DeviceProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='nidevice_grpc.DeviceProperties.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model', full_name='nidevice_grpc.DeviceProperties.model', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vendor', full_name='nidevice_grpc.DeviceProperties.vendor', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='nidevice_grpc.DeviceProperties.serial_number', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=170,
)


_ENUMERATEDEVICESREQUEST = _descriptor.Descriptor(
  name='EnumerateDevicesRequest',
  full_name='nidevice_grpc.EnumerateDevicesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=197,
)


_ENUMERATEDEVICESRESPONSE = _descriptor.Descriptor(
  name='EnumerateDevicesResponse',
  full_name='nidevice_grpc.EnumerateDevicesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='devices', full_name='nidevice_grpc.EnumerateDevicesResponse.devices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=275,
)


_RESERVEREQUEST = _descriptor.Descriptor(
  name='ReserveRequest',
  full_name='nidevice_grpc.ReserveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reservation_id', full_name='nidevice_grpc.ReserveRequest.reservation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='nidevice_grpc.ReserveRequest.client_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=277,
  serialized_end=336,
)


_RESERVERESPONSE = _descriptor.Descriptor(
  name='ReserveResponse',
  full_name='nidevice_grpc.ReserveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_reserved', full_name='nidevice_grpc.ReserveResponse.is_reserved', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=376,
)


_ISRESERVEDBYCLIENTREQUEST = _descriptor.Descriptor(
  name='IsReservedByClientRequest',
  full_name='nidevice_grpc.IsReservedByClientRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reservation_id', full_name='nidevice_grpc.IsReservedByClientRequest.reservation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='nidevice_grpc.IsReservedByClientRequest.client_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=378,
  serialized_end=448,
)


_ISRESERVEDBYCLIENTRESPONSE = _descriptor.Descriptor(
  name='IsReservedByClientResponse',
  full_name='nidevice_grpc.IsReservedByClientResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_reserved', full_name='nidevice_grpc.IsReservedByClientResponse.is_reserved', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=450,
  serialized_end=499,
)


_UNRESERVEREQUEST = _descriptor.Descriptor(
  name='UnreserveRequest',
  full_name='nidevice_grpc.UnreserveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reservation_id', full_name='nidevice_grpc.UnreserveRequest.reservation_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='nidevice_grpc.UnreserveRequest.client_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=501,
  serialized_end=562,
)


_UNRESERVERESPONSE = _descriptor.Descriptor(
  name='UnreserveResponse',
  full_name='nidevice_grpc.UnreserveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_unreserved', full_name='nidevice_grpc.UnreserveResponse.is_unreserved', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=564,
  serialized_end=606,
)


_RESETSERVERREQUEST = _descriptor.Descriptor(
  name='ResetServerRequest',
  full_name='nidevice_grpc.ResetServerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=608,
  serialized_end=628,
)


_RESETSERVERRESPONSE = _descriptor.Descriptor(
  name='ResetServerResponse',
  full_name='nidevice_grpc.ResetServerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_server_reset', full_name='nidevice_grpc.ResetServerResponse.is_server_reset', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=630,
  serialized_end=676,
)

_SESSION.oneofs_by_name['session'].fields.append(
  _SESSION.fields_by_name['name'])
_SESSION.fields_by_name['name'].containing_oneof = _SESSION.oneofs_by_name['session']
_SESSION.oneofs_by_name['session'].fields.append(
  _SESSION.fields_by_name['id'])
_SESSION.fields_by_name['id'].containing_oneof = _SESSION.oneofs_by_name['session']
_ENUMERATEDEVICESRESPONSE.fields_by_name['devices'].message_type = _DEVICEPROPERTIES
DESCRIPTOR.message_types_by_name['Session'] = _SESSION
DESCRIPTOR.message_types_by_name['DeviceProperties'] = _DEVICEPROPERTIES
DESCRIPTOR.message_types_by_name['EnumerateDevicesRequest'] = _ENUMERATEDEVICESREQUEST
DESCRIPTOR.message_types_by_name['EnumerateDevicesResponse'] = _ENUMERATEDEVICESRESPONSE
DESCRIPTOR.message_types_by_name['ReserveRequest'] = _RESERVEREQUEST
DESCRIPTOR.message_types_by_name['ReserveResponse'] = _RESERVERESPONSE
DESCRIPTOR.message_types_by_name['IsReservedByClientRequest'] = _ISRESERVEDBYCLIENTREQUEST
DESCRIPTOR.message_types_by_name['IsReservedByClientResponse'] = _ISRESERVEDBYCLIENTRESPONSE
DESCRIPTOR.message_types_by_name['UnreserveRequest'] = _UNRESERVEREQUEST
DESCRIPTOR.message_types_by_name['UnreserveResponse'] = _UNRESERVERESPONSE
DESCRIPTOR.message_types_by_name['ResetServerRequest'] = _RESETSERVERREQUEST
DESCRIPTOR.message_types_by_name['ResetServerResponse'] = _RESETSERVERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Session = _reflection.GeneratedProtocolMessageType('Session', (_message.Message,), dict(
  DESCRIPTOR = _SESSION,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.Session)
  ))
_sym_db.RegisterMessage(Session)

DeviceProperties = _reflection.GeneratedProtocolMessageType('DeviceProperties', (_message.Message,), dict(
  DESCRIPTOR = _DEVICEPROPERTIES,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.DeviceProperties)
  ))
_sym_db.RegisterMessage(DeviceProperties)

EnumerateDevicesRequest = _reflection.GeneratedProtocolMessageType('EnumerateDevicesRequest', (_message.Message,), dict(
  DESCRIPTOR = _ENUMERATEDEVICESREQUEST,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.EnumerateDevicesRequest)
  ))
_sym_db.RegisterMessage(EnumerateDevicesRequest)

EnumerateDevicesResponse = _reflection.GeneratedProtocolMessageType('EnumerateDevicesResponse', (_message.Message,), dict(
  DESCRIPTOR = _ENUMERATEDEVICESRESPONSE,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.EnumerateDevicesResponse)
  ))
_sym_db.RegisterMessage(EnumerateDevicesResponse)

ReserveRequest = _reflection.GeneratedProtocolMessageType('ReserveRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESERVEREQUEST,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.ReserveRequest)
  ))
_sym_db.RegisterMessage(ReserveRequest)

ReserveResponse = _reflection.GeneratedProtocolMessageType('ReserveResponse', (_message.Message,), dict(
  DESCRIPTOR = _RESERVERESPONSE,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.ReserveResponse)
  ))
_sym_db.RegisterMessage(ReserveResponse)

IsReservedByClientRequest = _reflection.GeneratedProtocolMessageType('IsReservedByClientRequest', (_message.Message,), dict(
  DESCRIPTOR = _ISRESERVEDBYCLIENTREQUEST,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.IsReservedByClientRequest)
  ))
_sym_db.RegisterMessage(IsReservedByClientRequest)

IsReservedByClientResponse = _reflection.GeneratedProtocolMessageType('IsReservedByClientResponse', (_message.Message,), dict(
  DESCRIPTOR = _ISRESERVEDBYCLIENTRESPONSE,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.IsReservedByClientResponse)
  ))
_sym_db.RegisterMessage(IsReservedByClientResponse)

UnreserveRequest = _reflection.GeneratedProtocolMessageType('UnreserveRequest', (_message.Message,), dict(
  DESCRIPTOR = _UNRESERVEREQUEST,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.UnreserveRequest)
  ))
_sym_db.RegisterMessage(UnreserveRequest)

UnreserveResponse = _reflection.GeneratedProtocolMessageType('UnreserveResponse', (_message.Message,), dict(
  DESCRIPTOR = _UNRESERVERESPONSE,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.UnreserveResponse)
  ))
_sym_db.RegisterMessage(UnreserveResponse)

ResetServerRequest = _reflection.GeneratedProtocolMessageType('ResetServerRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESETSERVERREQUEST,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.ResetServerRequest)
  ))
_sym_db.RegisterMessage(ResetServerRequest)

ResetServerResponse = _reflection.GeneratedProtocolMessageType('ResetServerResponse', (_message.Message,), dict(
  DESCRIPTOR = _RESETSERVERRESPONSE,
  __module__ = 'session_pb2'
  # @@protoc_insertion_point(class_scope:nidevice_grpc.ResetServerResponse)
  ))
_sym_db.RegisterMessage(ResetServerResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\022com.ni.grpc.deviceB\010NiDeviceP\001\252\002\037NationalInstruments.Grpc.Device'))

_SESSIONUTILITIES = _descriptor.ServiceDescriptor(
  name='SessionUtilities',
  full_name='nidevice_grpc.SessionUtilities',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=679,
  serialized_end=1145,
  methods=[
  _descriptor.MethodDescriptor(
    name='EnumerateDevices',
    full_name='nidevice_grpc.SessionUtilities.EnumerateDevices',
    index=0,
    containing_service=None,
    input_type=_ENUMERATEDEVICESREQUEST,
    output_type=_ENUMERATEDEVICESRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Reserve',
    full_name='nidevice_grpc.SessionUtilities.Reserve',
    index=1,
    containing_service=None,
    input_type=_RESERVEREQUEST,
    output_type=_RESERVERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='IsReservedByClient',
    full_name='nidevice_grpc.SessionUtilities.IsReservedByClient',
    index=2,
    containing_service=None,
    input_type=_ISRESERVEDBYCLIENTREQUEST,
    output_type=_ISRESERVEDBYCLIENTRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Unreserve',
    full_name='nidevice_grpc.SessionUtilities.Unreserve',
    index=3,
    containing_service=None,
    input_type=_UNRESERVEREQUEST,
    output_type=_UNRESERVERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ResetServer',
    full_name='nidevice_grpc.SessionUtilities.ResetServer',
    index=4,
    containing_service=None,
    input_type=_RESETSERVERREQUEST,
    output_type=_RESETSERVERRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SESSIONUTILITIES)

DESCRIPTOR.services_by_name['SessionUtilities'] = _SESSIONUTILITIES

# @@protoc_insertion_point(module_scope)
