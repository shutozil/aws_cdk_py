# aws_cdk_py

## How to start server
```
$ docker-compose build
$ docker-compose up -d
$ docker exec -it ContainerID /bin/bash
```

## For Developer
- after login shell
  - install python modules at cdk/setup.py
  - setup aws cli(devlopment, staging, production)
- [Caution]
  - Scripts(aws cli) are dependent at `.env`
```
$ ./setup.sh
```
- if does not work, you must be check permissions(setup.sh)
```
$ chmod 755 setup.sh
```

## Activating the Virtualenv
-  To activate your virtualenv on a Linux or MacOs platform:
```
$ source .env/bin/activate
```
- install the required python modules.
```
$ pip install --upgrade pip && pip install -r requirements.txt
```

## Learn Project Structure
- https://cdkworkshop.com/30-python/20-create-project/300-structure.html

## Synthesize a template from app
- This will output the following CloudFormation template:
```
$ cdk [--profile PROFILE] synth -c env=ENV
```

## Command List (ja-blog)
- https://dev.classmethod.jp/articles/aws-cdk-command-line-interface/

## Bootstrapping an environment
- The first time you deploy an AWS CDK app into an environment (account/region)
- need to install a bootstrap stack
```
$ cdk [--profile PROFILE] bootstrap -c env=ENV
```

## How to deploy
```
$ cdk [--profile PROFILE] deploy STACK_NAME -c env=ENV
```

## Handling Context at cdk.json
- https://docs.aws.amazon.com/cdk/latest/guide/get_context_var.html
- https://dev.classmethod.jp/articles/aws-cdk-command-line-interface/#toc-14
  - point
>Context 値は AWS CDK が自動で生成して使い回すものもあるし、開発者が明示的に保管しておく値もある


## Check Software Version
```
$ aws --version
$ cdk --version
```

## Setup aws configure
```
$ aws configure
```

## Check Profile
- https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-configure-files.html
```
$ cat ~/.aws/credentials
$ cat ~/.aws/config
$ aws configure list
```

## Show env var
```
# List
$ printenv

# Var
$ echo $VAR
```