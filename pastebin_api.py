import requests

API_POST_URL = 'https://pastebin.com/api/api_post.php'
DEVELOPER_API_KEY = '967hUnVSvDE1WfN0mRnyysL_KhrnXoy-'

def main():
    paste_url = post_new_paste('title', 'this is test')
    pass

def post_new_paste(title, body_text, expiration='10M', listed=True):
    """Creates anew public PasteBin paste

    Args:
        title (str): Paste Title
        body_text (str): Paste body text
        expiration (str, optional): HOw long the paste will last. (See https://pastebin.com/doc_api). Defaults to '10M'.
        listed (bool, optional): Whether the paste is listed or not. Defaults to True.

    Returns:
        str: URL of the new paste. None if failed
    """

    # Create dictionary of parameter values
    params = {
        'api_dev_key': DEVELOPER_API_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if listed else 1
    }

    # Send the post request to PasteBin API
    print("Posting new paste to PasteBin...", end='')
    resp_msg = requests.post(API_POST_URL, data=params)

    # Check if paste was created successfully
    if resp_msg.status_code == requests.codes.ok:
        print("success")
        return resp_msg.text
    else:
        print("failure")
        print(f"respose code {resp_msg.status_code} ({resp_msg.reason})")
        print(f"Error {resp_msg.text}")

if __name__ == '__main__':
    main()