import speedtest
test=speedtest.Speedtest()

print("loading server...")
print("choosing best server...")
best=test.get_best_server()
print("Found",best['host'], "located in",best['country'])

print("Performing ping test...")
ping_result=test.results.ping
print("Ping is : ",ping_result,"Ms")

print("Performing download speed test...")
download_result=test.download()
print("Download speed is : ",round(download_result/1024/1024,2),"Mb")

print("Performing upload speed test...")
upload_result=test.upload()
print("Upload speed is : ",round(upload_result/1024/1024,2),"Mb")


