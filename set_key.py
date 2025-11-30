import os

def set_api_key_from_file(file_path="APIKEY18.txt"):
    """
    Read the API key from a text file and store it in the correct environment variable.
    """
    try:
        with open(file_path, "r") as f:
            api_key = f.read().strip()

        # Set the correct environment variable
        os.environ["OPENAI_API_KEY"] = api_key

        print("API key loaded successfully.")
        return True

    except Exception as e:
        print(f"Failed to load API key: {e}")
        return False
