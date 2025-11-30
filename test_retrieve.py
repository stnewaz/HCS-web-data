from set_key import set_api_key_from_file
from retrieve_context import retrieve_context

def main():
    set_api_key_from_file()

    query = "What rights do I have as a student at SFU regarding academic concessions?"

    context, flag = retrieve_context(query)

    print("Flag:", flag)
    print("Context:", context)

if __name__ == "__main__":
    main()
