from aws_cdk import (
    aws_ec2,
    core,
)


class TestCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        cidr = '24.102.0.0/16'

        vpc = aws_ec2.Vpc(
            self,
            id='test-vpc',
            cidr=cidr,
            nat_gateways=1,
            subnet_configuration=[
                aws_ec2.SubnetConfiguration(
                    cidr_mask=18,
                    name='public',
                    subnet_type=aws_ec2.SubnetType.PUBLIC,
                ),
                aws_ec2.SubnetConfiguration(
                    cidr_mask=18,
                    name='private',
                    subnet_type=aws_ec2.SubnetType.PRIVATE,
                ),
                aws_ec2.SubnetConfiguration(
                    cidr_mask=24,
                    name='protected',
                    subnet_type=aws_ec2.SubnetType.PUBLIC,
                )
            ],
        )

        security_group = aws_ec2.SecurityGroup(
            self,
            id='test-security-group',
            vpc=vpc,
            security_group_name='test-security-group'
        )

        security_group.add_ingress_rule(
            peer=aws_ec2.Peer.ipv4(cidr),
            connection=aws_ec2.Port.tcp(22),
        )

        image_id = aws_ec2.AmazonLinuxImage(generation=aws_ec2.AmazonLinuxGeneration.AMAZON_LINUX_2).get_image(self).image_id

        aws_ec2.CfnInstance(
            self,
            id='test-instance',
            availability_zone="ap-northeast-1a",
            image_id=image_id,
            instance_type="t2.micro",
            key_name='cdk-test-ec2-key',
            security_group_ids=[security_group.security_group_id],
            subnet_id=vpc.private_subnets[0].subnet_id,
            tags=[{
                "key": "Name",
                "value": "test-instance"
            }]
        )
