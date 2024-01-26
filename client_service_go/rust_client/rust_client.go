// client_service_go/rust_client/rust_client.go
package rust_client

import (
	"context"
	"log"
	"client_service/unified_client"
	"client_service/proto/greetings"
	"google.golang.org/grpc"
)

type RustClient struct {
	conn   *grpc.ClientConn
	client greetings.GreeterClient
}

func NewRustClient(serverAddress string) (*RustClient, error) {
	conn, err := grpc.Dial(serverAddress, grpc.WithInsecure())
	if err != nil {
		return nil, err
	}

	client := greetings.NewGreeterClient(conn)
	return &RustClient{
		conn:   conn,
		client: client,
	}, nil
}

func (rc *RustClient) SendRustRequest() (string, error) {
	ctx := context.Background()
	response, err := rc.client.SayHi(ctx, &greetings.HelloReply{
		Message: "Hello from Rust Client",
	})
	if err != nil {
		log.Printf("Rust server communication error: %v", err)
		return "", err
	}
	return response.Message, nil
}

func (rc *RustClient) Close() {
	if rc.conn != nil {
		rc.conn.Close()
	}
}
