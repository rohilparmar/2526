def get_csv_to_s3(datasem5a-0344,AKIATMCDJTRNXICBL34M,ch.txt)
    s3 = boto3.client('s3')
    try:
        s3.download_file(datasem5a-0344,AKIATMCDJTRNXICBL34M,ch.txt)
        print("file download  successful to s3")
    expact Expaction as e:
        print(f"an error occurred: {str(e)}")
bucket_name = 'datasem5a-0344'
file_name = 'ch.txt'
s3_key =  'AKIATMCDJTRNXICBL34M'