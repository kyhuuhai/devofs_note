# 1.Create container instance
## 1.1 Get AMI
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/retrieve-ecs-optimized_AMI.html

`aws ssm get-parameters --names /aws/service/ecs/optimized-ami/amazon-linux-2023/recommended --region ap-southeast-1`

=> `ami-0651755cb449c45ba`

```
{
    "Parameters": [
        {
            "Name": "/aws/service/ecs/optimized-ami/amazon-linux-2023/recommended",
            "Type": "String",
            "Value": "{\"ecs_agent_version\":\"1.85.2\",\"ecs_runtime_version\":\"Docker version 25.0.3\",\"image_id\":\"ami-0651755cb449c45ba\",\"image_name\":\"al2023-ami-ecs-hvm-2023.0.20240725-kernel-6.1-x86_64\",\"image_version\":\"2023.0.20240725\",\"os\":\"Amazon Linux 2023\",\"schema_version\":1,\"source_image_name\":\"al2023-ami-minimal-2023.5.20240722.0-kernel-6.1-x86_64\"}",
            "Version": 44,
            "LastModifiedDate": "2024-07-27T04:07:04.683000+07:00",
            "ARN": "arn:aws:ssm:ap-southeast-1::parameter/aws/service/ecs/optimized-ami/amazon-linux-2023/recommended",
            "DataType": "text"
        }
    ],
    "InvalidParameters": []
}

```

## 1.2 user data instance
https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch_container_instance.html
```
#!/bin/bash
echo ECS_CLUSTER=your_cluster_name >> /etc/ecs/ecs.config
```

## 1.3 IAM instance profile
ecsInstanceRole

# Check Status SSM Agent
https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-status-and-restart.html
`sudo systemctl status amazon-ssm-agent`
