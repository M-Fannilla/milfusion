import os
from tqdm import tqdm


def delete_vertices_json_files():
    # Get the current directory
    current_dir = os.getcwd()

    # Collect all _vertices.json files
    files_to_delete = []
    for root, dirs, files in os.walk(current_dir):
        for file in files:
            if file.endswith("_vertices.json"):
                files_to_delete.append(os.path.join(root, file))

    # Display progress bar and delete files
    for file_path in tqdm(files_to_delete, desc="Deleting _vertices.json files"):
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")


if __name__ == '__main__':
    delete_vertices_json_files()
