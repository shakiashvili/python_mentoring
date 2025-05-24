from pk.logger import log_error, log_info
import os


class FileOperations:
    @staticmethod
    def read_file(file_path: str) -> list:
        
        # To execute locally
        # current_script_path = os.path.abspath(__file__)  
        # src_directory = os.path.dirname(current_script_path)
        # task_directory = os.path.dirname(src_directory)
        # task_directory = os.path.dirname(task_directory)

        # file_path = os.path.join(task_directory, file_path)
        try:
            with open(file_path) as i:
                current = os.path.abspath(__file__)
                print(current)
                log_info(f'Reading the input file, {file_path}')
                return [line.strip().split() for line in i.readlines()]
        except FileNotFoundError:
            log_error("File not Found,Please use the correct path")
        except Exception as e:
            log_error(f"We have an error: {e}")

    @staticmethod
    def write_file(file_path: str, content: str) -> None:
        try:
            with open(file_path, 'w') as o:
                log_info(f'Writing into, {file_path}')
                o.write(str(content) + '\n')
        except Exception as e:
            log_error(f"We have an error: {e}")
