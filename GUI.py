import tkinter as tk
import asyncio

from Judges import check_judges_status_async
from generateRandomIPs import generate_and_write_random_ips
from http_testing import http_test
from prepare_random_ips_text_file_for_HTTP_HTTPS_SOCKS4_SOCKS4A_SOCKS5 import prepare_random_ips_text_file_for_http

# Create the main window
root = tk.Tk()
root.title("Proxy Generator + Proxy Checker by github.com/raj14619")

# Set the initial size of the window
window_width = 900
window_height = 900
root.geometry(f"{window_width}x{window_height}")

#NOTES AND INFORMATION TO USER
message = tk.Message(root, text="WILL UPDATE INFORMATION ABOUT WHAT THIS PROGRAM DOES ANOTHER TIME",width=800)
message.pack()


# Create a label for Number Of Proxies To Generate
numbersOfProxiesToGenerateLabel = tk.Label(root, text="Number of Proxies to generate per cycle:")
numbersOfProxiesToGenerateLabel.pack()

# Create a text input field for Number of Proxies to generate
numbersOfProxiesToGenerateInputTextField = tk.Entry(root, width=100)
numbersOfProxiesToGenerateInputTextField.insert(0,1000000)
numbersOfProxiesToGenerateInputTextField.pack()

# Create a label for Ports to test for HTTP proxies
listOfPortsToTestForHTTPProxiesLabel = tk.Label(root, text="List of Ports to test for HTTP proxies:")
listOfPortsToTestForHTTPProxiesLabel.pack()

# Create a text input field for Ports to test for HTTP proxies
listOfPortsToTestForHTTPproxiesInputTextField = tk.Entry(root, width=100)
listOfPortsToTestForHTTPproxiesInputTextField.insert(0,"80,8080,3128,3129,3130,3127,8888,8000")
listOfPortsToTestForHTTPproxiesInputTextField.pack()


# Create a label for Ports to test for HTTPS proxies
#listOfPortsToTestForHTTPSproxiesLabel = tk.Label(root, text="List of Ports to test for HTTPS proxies:")
#listOfPortsToTestForHTTPSproxiesLabel.pack()

# Create a text input field for Ports to test for HTTPS proxies
#listOfPortsToTestForHTTPSproxiesInputTextField = tk.Entry(root, width=100)
#listOfPortsToTestForHTTPSproxiesInputTextField.insert(0,"443,8443,3128,8080,3127,3129,8888,8000,8443")
#listOfPortsToTestForHTTPSproxiesInputTextField.pack()


'''LISTBOX RELATED CODE'''

# Create a listbox
listbox = tk.Listbox(root, height=10,width=100)
listbox.pack(pady=10)

#prefill listbox with website judges
listbox.insert(tk.END,"http://azenv.net/")
listbox.insert(tk.END,"http://www.cooleasy.com/azenv.php")
listbox.insert(tk.END,"http://pascal.hoez.free.fr/azenv.php")
listbox.insert(tk.END,"http://www.proxy-listen.de/azenv.php")
listbox.insert(tk.END,"https://api.ipify.org/")
listbox.insert(tk.END,"https://ident.me/")




# Function to add an item to the listbox
def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)


# Function to delete the selected item from the listbox
def delete_item():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)


# Function to add an array of strings to the listbox
def add_items_to_listbox(items):
    for item in items:
        listbox.insert(tk.END, item)
# Create an entry widget for adding items

def get_listbox_items():
    items = []
    for i in range(listbox.size()):
        items.append(listbox.get(i))
    return items


entry = tk.Entry(root)
entry.pack()

# Create "Add" and "Delete" buttons
add_button = tk.Button(root, text="Add", command=add_item)
add_button.pack()
delete_button = tk.Button(root, text="Delete", command=delete_item)
delete_button.pack()


'''END OF LISTBOX RELATED CODE'''



# Create a button
button = tk.Button(root, text="Start")
button.pack()
button.config(command=lambda: asyncio.create_task(submit()))  # Use create_task to run the async function

# Function to handle button click
async def submit():
    while True:
        generate_and_write_random_ips()
        workingJudges = await check_judges_status_async(get_listbox_items())
        print(workingJudges)
        http_ports = listOfPortsToTestForHTTPproxiesInputTextField.get().split(',')
        prepare_random_ips_text_file_for_http(http_ports)
        await run_http_test()
        await asyncio.sleep(1)  # Wait for 1 second



async def run_http_test():
    await http_test()



button.config(command=lambda: asyncio.run(submit())) # will call submit function when the button is clicked


# Start the GUI application and keeps it running this is important to keep
root.mainloop()