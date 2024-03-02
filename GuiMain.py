import tkinter as tk
import speedtest

def on_button_click():

    spacer = tk.Label(root, bg="black", height=2)
    spacer.pack()
    label = tk.Label(root, text="Internet speed test done",font=("Arial", 12),bg='black',fg='white')
    label.pack()

    test=speedtest.Speedtest()

    best=test.get_best_server()
    label = tk.Label(root, text=f"Found {best['host']} located in {best['country']}", font=("Arial", 12), bg='black', fg='white')
    label.pack()

    ping_result=test.results.ping
    label = tk.Label(root, text=f"Ping is :  {ping_result} Ms", font=("Arial", 12), bg='black', fg='white')
    label.pack()

    download_result=test.download()

    label = tk.Label(root, text=f"Download speed is : {round(download_result/1024/1024,2)} Mbps", font=("Arial", 12), bg='black', fg='white')
    label.pack()

    upload_result=test.upload()
    label = tk.Label(root, text=f"Upload speed is : {round(upload_result/1024/1024,2)} Mbps", font=("Arial", 12), bg='black', fg='white')
    label.pack()

# Create the main window
root = tk.Tk()
root.title("Internet speed test")
root.configure(bg="black")

root.geometry("600x300")

spacer = tk.Label(root, bg="black", height=2)
spacer.pack()

#button for start
button = tk.Button(root, text="Click to test the internet speed",bg="black",fg='white',font=("Arial", 12), command=on_button_click)
button.pack()

# Run the main event loop
root.mainloop()
