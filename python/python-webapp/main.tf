provider "aws" {
  region = "us-east-1"  # Set your desired AWS region
}

resource "aws_ecs_cluster" "my_cluster" {
  name = "my-cluster"  # Set your ECS cluster name
}

resource "aws_ecs_task_definition" "my_task_definition" {
  family                   = "my_app"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  execution_role_arn        = aws_iam_role.ecs_execution_role.arn

  container_definitions = jsonencode([
    {
      name  = "my_app"
      image = "https://hub.docker.com/my_personal/my_app:latest"  # Replace with your Docker image URL
    }
  ])
}

resource "aws_iam_role" "ecs_execution_role" {
  name = "ecs_execution_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = "sts:AssumeRole",
        Effect = "Allow",
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_ecs_service" "my_service" {
  name            = "my_service"
  cluster         = aws_ecs_cluster.my_cluster.id
  task_definition = aws_ecs_task_definition.my_task_definition.arn
  launch_type     = "FARGATE"

  network_configuration {
    subnets = ["subnet-xxxxxxxxxxxxxx"]  # Set your subnet ID(s)
    security_groups = ["sg-xxxxxxxxxxxxxx"]  # Set your security group ID(s)
  }

  tags = {
    Name = "my-service"
  }
}
