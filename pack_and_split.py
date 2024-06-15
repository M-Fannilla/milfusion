import subprocess

zip_cmd = ["zip", "-r", "images.zip", "images"]
split_cmd = ["split", "-b", "10G", "images.zip", "images.zip.part"]
join_cmd = ["cat", "images.zip.part*", ">", "images.zip"]
unzip_cmd = ["unzip", "images.zip"]

if __name__ == "__main__":
    subprocess.run(zip_cmd)
    subprocess.run(split_cmd)
    subprocess.run(join_cmd)
    subprocess.run(unzip_cmd)
