#!/bin/sh

# CA 인증서 파일 생성
echo 01 > ca.srl
openssl genrsa -des3 -out ca-key.pem 2048
openssl req -new -x509 -days 365 -key ca-key.pem -out ca.pem

# 서버 키, 인증서 서명 요청 파일 생성
openssl genrsa -des3 -out server-key.pem 2048
openssl req -subj '/CN=docker.example.com' -new -key server-key.pem -out server.csr

# 서버 인증서 파일 생성
openssl x509 -req -days 365 -in server.csr -CA ca.pem -CAkey ca-key.pem -out server-cert.pem

# 클라이언트 키, 인증서 서명 요청 파일 생성
openssl genrsa -des3 -out key.pem 2048
openssl req -subj '/CN=client' -new -key key.pem -out client.csr

# 인증서 파일을 사용하여 접속을 허용하도록 설정 파일 생성, 클라이언트 인증서 파일 생성
echo extendedKeyUsage = clientAuth > extfile.cnf
openssl x509 -req -days 365 -in client.csr -CA ca.pem -CAkey ca-key.pem -out cert.pem -extfile extfile.cnf

# 서버용 server-key.pem 파일, 클라이언트용 key.pem 파일의 암호 제거
openssl rsa -in server-key.pem -out server-key.pem
openssl rsa -in key.pem -out key.pem

# 현재 리눅스 사용자 계정 디렉터리에 .docker 디렉터리를 생성, 클라이이언트에 필요한 파일 복사
mkdir ~/.docker
cp ca.pem ~/.docker/ca.pem
cp cert.pem ~/.docker/cert.pem
cp key.pem ~/.docker/key.pem
