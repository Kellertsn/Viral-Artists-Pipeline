import boto3
import json
import os
from datetime import datetime
from dotenv import load_dotenv
from lastfm_client import LastFmClient

load_dotenv()

def upload_to_s3(data, bucket_name, region):
    s3 = boto3.client("s3", region_name=region)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"viral-artists/{timestamp}.json"
    
    s3.put_object(
        Bucket=bucket_name,
        Key=filename,
        Body=json.dumps(data, indent=2),
        ContentType="application/json"
    )
    
    print(f"✅ Upload Success：s3://{bucket_name}/{filename}")

def main():
    print("🎵 Fetching Top Artists from Last.fm...")
    
    client = LastFmClient()
    artists = client.get_viral_artists()
    
    print(f"✅ Found {len(artists)} viral artists")
    print("\n🔥 Top 5 Viral Artists:")
    for i, artist in enumerate(artists[:5], 1):
        print(f"{i}. {artist['name']} | Listeners: {artist['listeners']:,} | Tags: {', '.join(artist['tags'])}")
    
    data = {
        "timestamp": datetime.now().isoformat(),
        "source": "Last.fm Chart",
        "artists": artists
    }
    
    bucket_name = os.getenv("AWS_BUCKET_NAME")
    region = os.getenv("AWS_REGION")
    
    upload_to_s3(data, bucket_name, region)
    
    print("\n🎉 Pipeline finish!")

if __name__ == "__main__":
    main()