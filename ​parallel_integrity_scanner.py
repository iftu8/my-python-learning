import hashlib
import concurrent.futures
import time
import os

class FileIntegrityScanner:
    def __init__(self, block_size=65536):
        # 64KB block size for optimizing memory buffer during large file reads
        self.block_size = block_size

    def calculate_sha256(self, file_path):
        """Computes the SHA-256 cryptographic hash of a file efficiently."""
        sha256_hash = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                # Reading the file in binary chunks to prevent RAM crash
                for byte_block in iter(lambda: f.read(self.block_size), b""):
                    sha256_hash.update(byte_block)
            return file_path, sha256_hash.hexdigest(), "SUCCESS"
        except FileNotFoundError:
            return file_path, None, "FILE_NOT_FOUND"
        except Exception as e:
            return file_path, None, f"ERROR: {str(e)}"

    def parallel_scan(self, file_list):
        """Executes multi-threaded hashing across available CPU cores."""
        results = {}
        
        # Using ThreadPoolExecutor for high-performance concurrent operations
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Mapping the function to all files simultaneously
            future_to_hash = {executor.submit(self.calculate_sha256, path): path for path in file_list}
            
            for future in concurrent.futures.as_completed(future_to_hash):
                file_path, file_hash, status = future.result()
                results[file_path] = {"hash": file_hash, "status": status}
                
        return results

# --- Enterprise Simulation Sandbox ---
if __name__ == "__main__":
    print("🚀 Initializing Multi-Threaded Integrity Engine...")
    time.sleep(1)

    # Creating dummy operational files to test the complex logic locally
    mock_files = ["system_config.cfg", "user_database.db", "secure_payment.log"]
    for name in mock_files:
        with open(name, "w") as mock_file:
            mock_file.write(f"Critical System Data Core for {name} generated at {time.time()}")

    print(f"📊 Detected {len(mock_files)} priority files for system-wide scan.")
    
    # Executing the high-performance scanner
    scanner = FileIntegrityScanner()
    start_time = time.perf_counter()
    scan_report = scanner.parallel_scan(mock_files)
    end_time = time.perf_counter()

    # --- Deep Analytics Output ---
    print("\n================= 🛡️ SYSTEM INTEGRITY REPORT =================")
    print(f"Execution Metric: Scanned in {end_time - start_time:.6f} seconds")
    print("---------------------------------------------------------------")
    
    for path, meta in scan_report.items():
        if meta["status"] == "SUCCESS":
            print(f"📄 File: {path:<20} | SHA-256: {meta['hash']}")
        else:
            print(f"📄 File: {path:<20} | Status: {meta['status']}")
            
    print("===============================================================")

    # Cleanup simulation files
    for name in mock_files:
        if os.path.exists(name):
            os.remove(name)
