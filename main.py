import asyncio
from playwright.async_api import async_playwright
import random
import os

# Read numbers from numbers.txt
with open('numbers.txt', 'r') as file:
    numbers = file.readlines()


# URL to open
url = 'https://tuyensinh.vlu.edu.vn/ket-qua-trung-tuyen'  # Replace with the actual URL

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

async def main():
    async with async_playwright() as p:
        print('Opening the browser...')
        # browser = await p.firefox.launch(headless=True, args=[
        #     '--no-sandbox',
        #     '--disable-setuid-sandbox',
        #     '--disable-infobars',
        #     '--disable-dev-shm-usage',
        #     '--disable-extensions',
        #     '--window-size=1280,800'
        # ])
        browser = await p.firefox.launch(headless=True, args=[
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-infobars',
        '--disable-dev-shm-usage',
        '--disable-extensions',
        '--window-size=1280,800',
        '--enable-gpu-rasterization',
        '--enable-zero-copy',
        '--enable-native-gpu-memory-buffers',
        '--disable-software-rasterizer',
        '--disable-background-timer-throttling',
        '--disable-backgrounding-occluded-windows',
        '--disable-renderer-backgrounding',
        '--disk-cache-size=0',  # Disable disk cache
        '--media-cache-size=0'  # Disable media cache  
        ])

        context = await browser.new_context(
            user_agent=user_agent,
            viewport={'width': 1280, 'height': 800},
            device_scale_factor=1,
            is_mobile=False,
            has_touch=False,
            java_script_enabled=True,
            storage_state={}
        )
        # browser = await p.webkit.launch(headless=True)  # Set headless to False if needed
        # context = await browser.new_context(user_agent=user_agent)
        page = await context.new_page()

         # Read the checked numbers from the file
        checked_numbers = set()
        if os.path.exists('checked.txt'):
            with open('checked.txt', 'r') as f:
                checked_numbers = set(line.strip() for line in f)
        else:
            #Create checked.txt if it doesn't exist
            with open('checked.txt', 'w') as f:
                pass

        for number in numbers:
            number = number.strip()      
            # Check if the number exists in the checked.txt
            if number in checked_numbers:
                continue
            
            # Write the checked number to the file
            with open('checked.txt', 'a') as f:
                f.write(f"{number}\n")
            
            await page.goto(url)
            # await page.wait_for_timeout(random.uniform(3000, 5000))  # Wait for the page to load

            # Find the search box element using the provided CSS selector
            search_box = await page.wait_for_selector('#vaadin-text-field-input-0 > slot:nth-child(2) > input:nth-child(1)')
            await search_box.fill('')

            # await page.wait_for_timeout(random.uniform(1000, 2000))  # Simulate human-like delay
            
            # Simulate typing the number
            for char in number:
                await search_box.type(char)
                # await page.wait_for_timeout(random.uniform(100, 200))

            # Press Enter
            await search_box.press('Enter')
            await page.wait_for_timeout(random.uniform(1000,1200))  # Wait for the search results to load

            data_path = os.path.join('data', f'{number}.html')      
            # # Save the HTML content to a file
            content = await page.content()
            with open(data_path, 'w', encoding='utf-8') as file:
                file.write(content)
                
            # Check if the content contains the specified phrase and delete the file if it does
            if 'Họ và tên' in content:
                num_files = len(os.listdir('data'))
                print(f"number of files: {num_files}")
            elif "chưa có trong hồ sơ trúng tuyển" in content:
                os.remove(data_path)
            else:
                # Move the file to the data_error folder
                # error_folder = 'data_error'
                # if not os.path.exists(error_folder):
                #     os.makedirs(error_folder)
                # shutil.move(data_path, os.path.join(error_folder, f'{number}.html'))
                os.remove(data_path)
                with open('missing.txt', 'a') as f:
                    f.write(f"{number}\n")

                # Print the number of lines in missing.txt
                with open('missing.txt', 'r') as f:
                    num_missing = sum(1 for _ in f)
                    print(f"number of missing files: {num_missing}")


            # Press the ESC key on the current webpage
            await page.keyboard.press('Escape')
            await page.wait_for_timeout(random.uniform(50, 100))

            # Print the number of lines in checked.txt
            with open('checked.txt', 'r') as f:
                num_checked = sum(1 for _ in f)
                print(f"number of checked numbers: {num_checked}")
            # await page.wait_for_timeout(random.uniform(1000, 2000))


        await browser.close()

asyncio.run(main())
print('Done')
