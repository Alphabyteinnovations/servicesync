// client_service_go/unified_client/unified_client.go
package unified_client

type UnifiedClient interface {
	SendGoRequest() (string, error)
	SendRustRequest() (string, error)
	SendPythonRequest() (string, error)
	Close()
}
