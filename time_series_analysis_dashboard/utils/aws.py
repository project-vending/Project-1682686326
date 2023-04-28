
import boto3

def upload_file_to_s3(file_path, bucket_name, s3_key):
    """
    Upload a file to AWS S3.

    Parameters:
    file_path (str): Local path to the file to upload.
    bucket_name (str): Name of the S3 bucket to upload the file to.
    s3_key (str): Key to use for the uploaded file in S3.

    Returns:
    (bool): True if the upload succeeds, False otherwise.
    """
    try:
        s3 = boto3.client('s3')
        s3.upload_file(file_path, bucket_name, s3_key)
        return True
    except:
        return False
