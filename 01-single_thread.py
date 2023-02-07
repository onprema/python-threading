# Example of a single-threaded application
from training import WEBSITES, visit_website


if __name__ == '__main__':
    print('Main thread starting')
    for website in WEBSITES:
        visit_website(website)
    print('Main thread ending')