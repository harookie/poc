### ec2 접속
```shell
$ IP="3.34.2.160"
$ ssh -i ~/aws_ec2_key_pair.pem ec2-user@${IP}
```

### ec2 docker & docker compose 설치
```shell
$ sudo yum update -y
$ sudo amazon-linux-extras enable docker
$ sudo yum install docker -y
$ sudo systemctl start docker
$ sudo systemctl enable docker
$ sudo usermod -aG docker ec2-user
$ sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ docker-compose --version
```