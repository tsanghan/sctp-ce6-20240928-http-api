terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.69.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "2.6.0"
    }
  }
  required_version = "~>1.8.2"
}

provider "aws" {
  region = "ap-southeast-1"
}

provider "archive" {}