import requests
import time

# ANTI-PATTERN 1: Global mutable state for sessions (Memory Leak risk)
user_sessions = {}

def process_orders(order_urls):
    for url in order_urls:
        try:
            # ANTI-PATTERN 2: Synchronous, blocking HTTP call in a loop with NO TIMEOUT.
            # If 'unreliable-inventory-service' hangs, this entire thread hangs forever.
            # ANTI-PATTERN 3: No circuit breaker or retry mechanism.
            response = requests.get(url)
            print(f"Processed {url}: {response.status_code}")
        except Exception:
            # ANTI-PATTERN 4: Bare exception. Fails silently, masking critical network errors.
            pass

def connect_to_db():
    # ANTI-PATTERN 5: Hardcoded production secrets in source code
    db_password = "super_secret_production_password_123!"
    
    # ANTI-PATTERN 6: No connection pooling. Opens a new raw connection every time.
    print(f"Connecting to DB with {db_password}")

if __name__ == "__main__":
    # ANTI-PATTERN 7: Long-running process with no health check endpoint or graceful shutdown
    while True:
        process_orders(["http://unreliable-inventory-service.internal/api/v1/update"])
        time.sleep(1)