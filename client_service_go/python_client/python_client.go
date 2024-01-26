// client_service_go/python_client/python_client.go
package python_client

import (
	"context"
	"log"
	"client_service/unified_client"
	"client_service/proto/greetings"
	"google.golang.org/grpc"
)

type PythonClient struct {
	conn   *grpc.ClientConn
	client greetings.GreeterClient
}

func NewPythonClient(serverAddress string) (*PythonClient, error) {
	conn, err := grpc.Dial(serverAddress, grpc.WithInsecure())
	if err != nil {
		return nil, err
	}

	client := greetings.NewGreeterClient(conn)
	return &PythonClient{
		conn:   conn,
		client: client,
	}, nil
}

func (pc *PythonClient) SendPythonRequest() (string, error) {
	ctx := context.Background()
	response, err := pc.client.SayHi(ctx, &greetings.HelloReply{
		Message: "Hello from Python Client",
	})
	if err != nil {
		log.Printf("Python server communication error: %v", err)
		return "", err
	}
	return response.Message, nil
}

func (pc *PythonClient) Close() {
	if pc.conn != nil {
		pc.conn.Close()
	}
}
