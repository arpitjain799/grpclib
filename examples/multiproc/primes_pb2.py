# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: multiproc/primes.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16multiproc/primes.proto\x12\x06primes\x1a\x1egoogle/protobuf/wrappers.proto\"\x19\n\x07Request\x12\x0e\n\x06number\x18\x01 \x01(\x03\"5\n\x05Reply\x12,\n\x08is_prime\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.BoolValue23\n\x06Primes\x12)\n\x05\x43heck\x12\x0f.primes.Request\x1a\r.primes.Reply\"\x00\x62\x06proto3')



_REQUEST = DESCRIPTOR.message_types_by_name['Request']
_REPLY = DESCRIPTOR.message_types_by_name['Reply']
Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'multiproc.primes_pb2'
  # @@protoc_insertion_point(class_scope:primes.Request)
  })
_sym_db.RegisterMessage(Request)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'multiproc.primes_pb2'
  # @@protoc_insertion_point(class_scope:primes.Reply)
  })
_sym_db.RegisterMessage(Reply)

_PRIMES = DESCRIPTOR.services_by_name['Primes']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=66
  _REQUEST._serialized_end=91
  _REPLY._serialized_start=93
  _REPLY._serialized_end=146
  _PRIMES._serialized_start=148
  _PRIMES._serialized_end=199
# @@protoc_insertion_point(module_scope)
