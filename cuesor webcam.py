from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def move_mouse_square(duration=10, interval=0.5, distance=100):
    """
    Move the mouse cursor in a square pattern.

    Parameters:
    duration (int): Total duration to move the mouse in seconds.
    interval (float): Interval between each movement.
    distance (int): Distance to move the cursor in each direction.
    """
    # ... existing code ...

def auto_scroll(driver, duration=10, interval=0.5):
    """
    Automatically scroll the webpage.

    Parameters:
    driver (webdriver): The selenium webdriver instance.
    duration (int): Total duration to scroll in seconds.
    interval (float): Interval between each scroll.
    """
    start_time = time.time()
    
    while (time.time() - start_time) < duration:
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(interval)

# Setup selenium webdriver
driver = webdriver.Chrome()  # or use webdriver.Firefox() if using Firefox
driver.get('https://lms.guru.kemdikbud.go.id/courses/47980/discussion_topics/890153')  # replace with the desired website URL

# Call the functions
move_mouse_square(duration=10, interval=0.5, distance=100)
auto_scroll(driver, duration=10, interval=0.5)

# Close the browser after scrolling
driver.quit()