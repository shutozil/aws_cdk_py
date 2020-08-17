# aws_cdk_py

## How to start server
```
$ docker-compose build
$ docker-compose up -d
$ docker exec -it ContainerID /bin/bash
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
$ cdk [--profile PROFILE] synth
```

## Command List (ja-blog)
- https://dev.classmethod.jp/articles/aws-cdk-command-line-interface/

## Bootstrapping an environment
- The first time you deploy an AWS CDK app into an environment (account/region)
- need to install a bootstrap stack
```
$ cdk [--profile PROFILE] bootstrap
```

## How to deploy
```
$ cdk [--profile PROFILE] deploy STACK_NAME --context env=ENV
```

## Handling Context at cdk.json
- https://docs.aws.amazon.com/cdk/latest/guide/get_context_var.html
- https://dev.classmethod.jp/articles/aws-cdk-command-line-interface/#toc-14
  - Context 値は AWS CDK が自動で生成して使い回すものもあるし、開発者が明示的に保管しておく値もある


## Check Software Version
```
$ aws --version
$ cdk --version
```

## Check Profile
- https://docs.aws.amazon.com/ja_jp/cli/latest/userguide/cli-configure-files.html
```
$ cat ~/.aws/credentials
$ cat ~/.aws/config
```
