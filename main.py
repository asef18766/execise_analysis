import requests
from requests.sessions import session
import logging
logging.basicConfig(level = logging.DEBUG)

def main():
    playername = "特務小熊熊"
    
    sess = session()
    resp = sess.get(f"https://lol.moa.tw/searchlogs/querySummoner", params={"sn":playername})
    print(resp.status_code)
    print(resp.text)
    
if __name__ == "__main__" :
    main()