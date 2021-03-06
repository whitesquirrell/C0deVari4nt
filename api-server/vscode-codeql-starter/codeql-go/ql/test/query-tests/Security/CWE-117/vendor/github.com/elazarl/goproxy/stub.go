// Code generated by depstubber. DO NOT EDIT.
// This is a simple stub for github.com/elazarl/goproxy, strictly for use in testing.

// See the LICENSE file for information about the licensing of the original library.
// Source: github.com/elazarl/goproxy (exports: ProxyCtx; functions: )

// Package goproxy is a stub of github.com/elazarl/goproxy, generated by depstubber.
package goproxy

import (
	tls "crypto/tls"
	net "net"
	http "net/http"
)

type CertStorage interface {
	Fetch(_ string, _ func() (*tls.Certificate, error)) (*tls.Certificate, error)
}

type ConnectAction struct {
	Action    ConnectActionLiteral
	Hijack    func(*http.Request, net.Conn, *ProxyCtx)
	TLSConfig func(string, *ProxyCtx) (*tls.Config, error)
}

type ConnectActionLiteral int

type HttpsHandler interface {
	HandleConnect(_ string, _ *ProxyCtx) (*ConnectAction, string)
}

type Logger interface {
	Printf(_ string, _ ...interface{})
}

type ProxyConds struct{}

func (_ *ProxyConds) Do(_ RespHandler) {}

func (_ *ProxyConds) DoFunc(_ func(*http.Response, *ProxyCtx) *http.Response) {}

type ProxyCtx struct {
	Req          *http.Request
	Resp         *http.Response
	RoundTripper RoundTripper
	Error        error
	UserData     interface{}
	Session      int64
	Proxy        *ProxyHttpServer
}

func (_ *ProxyCtx) Charset() string {
	return ""
}

func (_ *ProxyCtx) Logf(_ string, _ ...interface{}) {}

func (_ *ProxyCtx) RoundTrip(_ *http.Request) (*http.Response, error) {
	return nil, nil
}

func (_ *ProxyCtx) Warnf(_ string, _ ...interface{}) {}

type ProxyHttpServer struct {
	KeepDestinationHeaders bool
	Verbose                bool
	Logger                 Logger
	NonproxyHandler        http.Handler
	Tr                     *http.Transport
	ConnectDial            func(string, string) (net.Conn, error)
	CertStore              CertStorage
	KeepHeader             bool
}

func (_ *ProxyHttpServer) NewConnectDialToProxy(_ string) func(string, string) (net.Conn, error) {
	return nil
}

func (_ *ProxyHttpServer) NewConnectDialToProxyWithHandler(_ string, _ func(*http.Request)) func(string, string) (net.Conn, error) {
	return nil
}

func (_ *ProxyHttpServer) OnRequest(_ ...ReqCondition) *ReqProxyConds {
	return nil
}

func (_ *ProxyHttpServer) OnResponse(_ ...RespCondition) *ProxyConds {
	return nil
}

func (_ *ProxyHttpServer) ServeHTTP(_ http.ResponseWriter, _ *http.Request) {}

type ReqCondition interface {
	HandleReq(_ *http.Request, _ *ProxyCtx) bool
	HandleResp(_ *http.Response, _ *ProxyCtx) bool
}

type ReqHandler interface {
	Handle(_ *http.Request, _ *ProxyCtx) (*http.Request, *http.Response)
}

type ReqProxyConds struct{}

func (_ *ReqProxyConds) Do(_ ReqHandler) {}

func (_ *ReqProxyConds) DoFunc(_ func(*http.Request, *ProxyCtx) (*http.Request, *http.Response)) {}

func (_ *ReqProxyConds) HandleConnect(_ HttpsHandler) {}

func (_ *ReqProxyConds) HandleConnectFunc(_ func(string, *ProxyCtx) (*ConnectAction, string)) {}

func (_ *ReqProxyConds) HijackConnect(_ func(*http.Request, net.Conn, *ProxyCtx)) {}

type RespCondition interface {
	HandleResp(_ *http.Response, _ *ProxyCtx) bool
}

type RespHandler interface {
	Handle(_ *http.Response, _ *ProxyCtx) *http.Response
}

type RoundTripper interface {
	RoundTrip(_ *http.Request, _ *ProxyCtx) (*http.Response, error)
}
