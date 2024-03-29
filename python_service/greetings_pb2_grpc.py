# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import greetings_pb2 as greetings__pb2


class GreeterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/greetings.Greeter/SayHello',
                request_serializer=greetings__pb2.HelloRequest.SerializeToString,
                response_deserializer=greetings__pb2.HelloReply.FromString,
                )
        self.SayHi = channel.unary_unary(
                '/greetings.Greeter/SayHi',
                request_serializer=greetings__pb2.HelloReply.SerializeToString,
                response_deserializer=greetings__pb2.HelloReply.FromString,
                )
        self.SayThankYou = channel.unary_unary(
                '/greetings.Greeter/SayThankYou',
                request_serializer=greetings__pb2.ThankYouRequest.SerializeToString,
                response_deserializer=greetings__pb2.WelcomeReply.FromString,
                )


class GreeterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHi(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayThankYou(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=greetings__pb2.HelloRequest.FromString,
                    response_serializer=greetings__pb2.HelloReply.SerializeToString,
            ),
            'SayHi': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHi,
                    request_deserializer=greetings__pb2.HelloReply.FromString,
                    response_serializer=greetings__pb2.HelloReply.SerializeToString,
            ),
            'SayThankYou': grpc.unary_unary_rpc_method_handler(
                    servicer.SayThankYou,
                    request_deserializer=greetings__pb2.ThankYouRequest.FromString,
                    response_serializer=greetings__pb2.WelcomeReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'greetings.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greetings.Greeter/SayHello',
            greetings__pb2.HelloRequest.SerializeToString,
            greetings__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHi(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greetings.Greeter/SayHi',
            greetings__pb2.HelloReply.SerializeToString,
            greetings__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayThankYou(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/greetings.Greeter/SayThankYou',
            greetings__pb2.ThankYouRequest.SerializeToString,
            greetings__pb2.WelcomeReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
