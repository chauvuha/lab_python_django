import json
import threading
import urllib.request
import asyncio

# 1. Write a function to break a list into evenly sized chunks and
# calculate the sum of all sub-lists in parallel and write the results
# to a file named output.txt. Remember to keep the order of the
# sub-lists in the output file.
def sum_chunks(lst, chunk_size, output_filename):
    chunks = [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]
    chunk_sums = []
    for chunk in chunks:
        chunk_sum = sum(chunk)
        chunk_sums.append(chunk_sum)
    with open(output_filename, 'w') as f:
        for s in chunk_sums:
            f.write(str(s) + '\n')

# Testing codes:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sum_chunks(numbers, 3, 'outputs_folder/output.txt')

# 2. Write a function to read 10 json files using threads and merge
# into one big json file.
def merge_json_files(filenames):
    # Make a list to store all JSON files
    json_data = []

    def read_json_file(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            json_data.append(data)

    # Create a list of threads, one for each filename
    threads = []
    for filename in filenames:
        t = threading.Thread(target=read_json_file, args=[filename])
        threads.append(t)

    # Start each thread
    for thread in threads:
        thread.start()

    # Wait for each thread to finish
    for thread in threads:
        thread.join()

    # Merge the contents
    merged_data = {}
    for data in json_data:
        merged_data.update(data)

    # Write the merged data to a file
    with open('outputs_folder/merged_data.json', 'w') as f:
        json.dump(merged_data, f)

# Testing codes:
merge_json_files(['inputs_folder/data1.json', 'inputs_folder/data2.json', 'inputs_folder/data3.json'])

# 3. Write a function to download 2 images from a list of urls from the
# internet using threads.
def download_images(url_list):
    def download_image(url, filename):
        urllib.request.urlretrieve(url, filename)

    # Create a list of threads, one for each image to be downloaded
    threads = []
    for i, url in enumerate(url_list):
        if i < 2:
            filename = f'outputs_folder/image{i+1}.jpg'
            t = threading.Thread(target=download_image, args=[url, filename])
            threads.append(t)

    # Start each thread
    for thread in threads:
        thread.start()

    # Wait for each thread to finish
    for thread in threads:
        thread.join()

# Testing codes:
url_list = [
    'https://picsum.photos/200/300',
    'https://picsum.photos/200/300',
    'https://picsum.photos/200/300',
]

download_images(url_list)

# 4. use asyncio instead
async def download_image(url, filename):
    urllib.request.urlretrieve(url, filename)

async def download_images_asyncio(url_list):
    tasks = []
    for i, url in enumerate(url_list):
        if i < 2:
            filename = f'outputs_folder/image_asyncio{i+1}.jpg'
            tasks.append(asyncio.create_task(download_image(url, filename)))
    await asyncio.gather(*tasks)

# Testing codes:
asyncio.run(download_images_asyncio(url_list))



