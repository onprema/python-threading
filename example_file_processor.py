import threading
import os
import random
from queue import Queue
from collections import Counter
import time

class FileProcessor:
    def __init__(self, directory, file_pattern, max_threads=4):
        self.directory = directory  # Directory containing the files to process
        self.file_pattern = file_pattern  # File extension or pattern to match
        self.max_threads = max_threads  # Maximum number of threads to use
        self.queue = Queue()  # Queue to hold files to be processed
        self.lock = threading.Lock()  # Lock for thread-safe updates to shared data
        self.total_word_count = Counter()  # Shared counter for word frequencies across all files

    def process_file(self, filepath):
        # Process a single file and return its word count
        time.sleep(random.uniform(0.1, 0.5))  # Simulate latency
        with open(filepath, 'r') as file:
            # Read the file and split into words
            word_count = Counter(file.read().split())
        return word_count

    def worker(self):
        while True:
            # Get a file path from the queue
            filepath = self.queue.get()
            
            # None is our signal to stop the worker
            if filepath is None:
                break
            
            print(f"Processing: {filepath}")
            
            # Process the file and get its word count
            file_word_count = self.process_file(filepath)
            
            # Update the total word count in a thread-safe manner
            with self.lock:
                self.total_word_count.update(file_word_count)
            
            # Mark the task as done
            self.queue.task_done()

    def run(self):
        # Populate the queue with files to process
        for filename in os.listdir(self.directory):
            if filename.endswith(self.file_pattern):
                self.queue.put(os.path.join(self.directory, filename))

        # Create and start the worker threads
        threads = []
        for _ in range(self.max_threads):
            t = threading.Thread(target=self.worker)
            t.start()
            threads.append(t)

        # Wait for all tasks in the queue to be completed
        self.queue.join()

        # Stop the workers by sending them None
        for _ in range(self.max_threads):
            self.queue.put(None)
        
        # Wait for all threads to finish
        for t in threads:
            t.join()

        return self.total_word_count

def create_sample_logs(directory, num_files=10, lines_per_file=100):
    """
    Create a directory with sample log files containing random words.
    
    :param directory: The directory to create and fill with log files
    :param num_files: Number of log files to create
    :param lines_per_file: Number of lines in each log file
    """
    # Ensure the directory exists
    os.makedirs(directory, exist_ok=True)
    
    # List of sample words to use in log files
    words = ["INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL", "GET", "POST", "PUT", "DELETE", 
             "database", "server", "client", "network", "file", "user", "system", "process", 
             "memory", "CPU", "disk", "application", "service", "module", "function", "class"]
    
    # Create log files
    for i in range(num_files):
        filename = os.path.join(directory, f"sample_log_{i+1}.log")
        with open(filename, 'w') as file:
            for _ in range(lines_per_file):
                # Generate a random log line
                log_line = " ".join(random.choices(words, k=random.randint(5, 15)))
                file.write(log_line + "\n")
    
    print(f"Created {num_files} sample log files in {directory}")

if __name__ == "__main__":
    # Generate the sample log files
    create_sample_logs("./logs", num_files=1000, lines_per_file=1000)

    # Create a FileProcessor instance
    processor = FileProcessor("./logs", ".log", max_threads=40)
    
    # Run the processor and get the total word count
    word_count = processor.run()
    
    # Print the top 10 most common words
    print("Top 10 words:")
    for word, count in word_count.most_common(10):
        print(f"{word}: {count}")