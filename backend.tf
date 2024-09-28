terraform {
  backend "s3" {
    bucket = "sctp-ce6-tfstate"
    key    = "tsanghan-ce6-20240928-http-apigw.tfstate"
    region = "ap-southeast-1"
  }
}