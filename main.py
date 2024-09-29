from dotenv import load_dotenv
import os

load_dotenv()

def main():
    print(os.environ.get("VERSION"))

main()
exit
