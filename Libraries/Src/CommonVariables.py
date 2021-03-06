def get_variables():
    variables = {
        'ADMIN_SESSION': 'Admin Session',
        'API_BASE_URL': 'https://glacial-earth-31542.herokuapp.com',
        'ADMIN': {
            'OPTIONS_REQUEST_HEADERS': {
                'Cookie': 'tabstyle=raw-tab; csrftoken=YZOeA3UsxKOCmIhaBPWP4o0Od2rBtkqo3cHCvcJpk45790iM37RHxbweEw7qWZ51; sessionid=rpibesdbd7s6wbwxwrriqi8seg2lsi7w',
                'Host': 'glacial-earth-31542.herokuapp.com',
                'Connection': 'keep-alive',
                'Accept': 'application/json',
                # Note: this is different from what browser sends to server. Refer to OPTIONS_RESPONSE_HEADERS['content-type']
                'Origin': 'https://glacial-earth-31542.herokuapp.com',
                'X-Requested-With': 'XMLHttpRequest',
                'Sec-Fetch-Dest': 'empty',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Referer': 'https://glacial-earth-31542.herokuapp.com/api/postings/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,fi;q=0.8',
            },
            'GET_REQUEST_HEADERS': {
                'Cookie': 'tabstyle=raw-tab; csrftoken=YZOeA3UsxKOCmIhaBPWP4o0Od2rBtkqo3cHCvcJpk45790iM37RHxbweEw7qWZ51; sessionid=rpibesdbd7s6wbwxwrriqi8seg2lsi7w',
                'Host': 'glacial-earth-31542.herokuapp.com',
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36',
                'Sec-Fetch-Dest': 'document',
                'Accept': 'application/json',  # Note: this is different from what browser sends to server.
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Referer': 'https://glacial-earth-31542.herokuapp.com/api/postings/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,fi;q=0.8',
            },
            'POST_REQUEST_HEADERS': {
                'Host': 'glacial-earth-31542.herokuapp.com',
                'Connection': 'keep-alive',
                 # Content-Length: 64
                'Origin': 'https://glacial-earth-31542.herokuapp.com',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36',
                'Content-Type': 'application/json',
                'Accept': 'text/html; q=1.0, */*',
                'Sec-Fetch-Dest': 'empty',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFTOKEN': '795vLL03vWakjyWxM3odA8Fs2OFy1J8VcmYTGUP0igrP6QX9elj53VbStilnuoNy',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Referer': 'https://glacial-earth-31542.herokuapp.com/api/postings/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,fi;q=0.8',
                'Cookie': 'tabstyle=raw-tab; csrftoken=YZOeA3UsxKOCmIhaBPWP4o0Od2rBtkqo3cHCvcJpk45790iM37RHxbweEw7qWZ51; sessionid=rpibesdbd7s6wbwxwrriqi8seg2lsi7w',
            },
            'PUT_REQUEST_HEADERS': {
                'Host': 'glacial-earth-31542.herokuapp.com',
                'Connection': 'keep-alive',
                 # 'Content-Length': '243',
                'Origin': 'https://glacial-earth-31542.herokuapp.com',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36',
                'Content-Type': 'application/json',
                'Accept': 'text/html; q=1.0, */*',
                'Sec-Fetch-Dest': 'empty',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFTOKEN': '795vLL03vWakjyWxM3odA8Fs2OFy1J8VcmYTGUP0igrP6QX9elj53VbStilnuoNy',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Referer': '',  # expects the url of the posting resource here!
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,fi;q=0.8',
                'Cookie': 'tabstyle=raw-tab; csrftoken=YZOeA3UsxKOCmIhaBPWP4o0Od2rBtkqo3cHCvcJpk45790iM37RHxbweEw7qWZ51; sessionid=rpibesdbd7s6wbwxwrriqi8seg2lsi7w',
            },
            'DELETE_REQUEST_HEADERS': {
                'Host': 'glacial-earth-31542.herokuapp.com',
                'Connection': 'keep-alive',
                'Origin': 'https://glacial-earth-31542.herokuapp.com',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept': 'text/html; q=1.0, */*',
                'Sec-Fetch-Dest': 'empty',
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFTOKEN': '795vLL03vWakjyWxM3odA8Fs2OFy1J8VcmYTGUP0igrP6QX9elj53VbStilnuoNy',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Referer': '',  # expects the url of the posting resource here!
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,fi;q=0.8',
                'Cookie': 'tabstyle=raw-tab; csrftoken=YZOeA3UsxKOCmIhaBPWP4o0Od2rBtkqo3cHCvcJpk45790iM37RHxbweEw7qWZ51; sessionid=rpibesdbd7s6wbwxwrriqi8seg2lsi7w',
            },
            'EXPECTED_API_SPEC': {
                'name': 'Blog Post Api',
                'description': '',
                'renders': [
                    'application/json',
                    'text/html'
                ],
                'parses': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ],
                'actions': {
                    'POST': {
                        'url': {
                            'type': 'field',
                            'required': False,
                            'read_only': True,
                            'label': 'Url'
                        },
                        'id': {
                            'type': 'integer',
                            'required': False,
                            'read_only': True,
                            'label': 'ID'
                        },
                        'user': {
                            'type': 'field',
                            'required': False,
                            'read_only': True,
                            'label': 'User'
                        },
                        'title': {
                            'type': 'string',
                            'required': False,
                            'read_only': False,
                            'label': 'Title',
                            'max_length': 120
                        },
                        'content': {
                            'type': 'string',
                            'required': False,
                            'read_only': False,
                            'label': 'Content',
                            'max_length': 120
                        },
                        'timestamp': {
                            'type': 'datetime',
                            'required': False,
                            'read_only': True,
                            'label': 'Timestamp'
                        }
                    }
                }
            },
            'OPTIONS_RESPONSE_HEADERS': {
                'Allow': 'GET, POST, HEAD, OPTIONS',
                'Vary': 'Accept, Cookie',
                'Content-Type': 'application/json',
            },
        },
        'NO_PRIVILIGE_USER': {
            'OPTIONS_REQUEST_HEADERS': {
                'Host': 'glacial-earth-31542.herokuapp.com',
                'Connection': 'keep-alive',
                'Accept': 'application/json',
                'Sec-Fetch-Dest': 'empty',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://glacial-earth-31542.herokuapp.com',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Referer': 'https://glacial-earth-31542.herokuapp.com/api/postings/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cookie': 'csrftoken=RHyE3NK61KZ3moRSwU27V39doEwRonc1F96Grq7MjsuqhSOY1LjGvVD9pQItGqgw',
            },
            'OPTIONS_RESPONSE_HEADERS': {
                'Allow': 'GET, POST, HEAD, OPTIONS',
                'Vary': 'Accept, Cookie',
                'Content-Type': 'application/json',
            },
            'EXPECTED_API_SPEC': {
                "name": "Blog Post Api",
                "description": "",
                "renders": [
                    "application/json",
                    "text/html"
                ],
                "parses": [
                    "application/json",
                    "application/x-www-form-urlencoded",
                    "multipart/form-data"
                ]
            },
            'GET_REQUEST_HEADERS': {
                'Host': 'glacial-earth-31542.herokuapp.com',
                'Connection': 'keep-alive',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
                'Sec-Fetch-Dest': 'document',
                'Accept': 'application/json',  # Note: this is different from what browser sends to server.
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-User': '?1',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9',
                'Cookie': 'csrftoken=RHyE3NK61KZ3moRSwU27V39doEwRonc1F96Grq7MjsuqhSOY1LjGvVD9pQItGqgw',
            },
            'POST_REQUEST_HEADERS': {
                'Host': 'glacial-earth-31542.herokuapp.com',
                'Connection': 'keep-alive',
                'Origin': 'https://glacial-earth-31542.herokuapp.com',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Sec-Fetch-Dest': 'empty',
                'X-Requested-With': 'XMLHttpRequest',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Referer': 'https://glacial-earth-31542.herokuapp.com/api/postings/',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,fi;q=0.8',
                'Cookie': 'csrftoken=RHyE3NK61KZ3moRSwU27V39doEwRonc1F96Grq7MjsuqhSOY1LjGvVD9pQItGqgw',
            },
           'PUT_REQUEST_HEADERS': {
                'Host': 'glacial-earth-31542.herokuapp.com',
                'Connection': 'keep-alive',
                'Origin': 'https://glacial-earth-31542.herokuapp.com',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36',
                'Content-Type': 'application/json',
                'Accept': 'text/html; q=1.0, */*',
                'Sec-Fetch-Dest': 'empty',
                'X-Requested-With': 'XMLHttpRequest',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Referer': '',  # expects the url of the posting resource here!
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,fi;q=0.8',
                'Cookie': 'csrftoken=RHyE3NK61KZ3moRSwU27V39doEwRonc1F96Grq7MjsuqhSOY1LjGvVD9pQItGqgw',
            },
            'DELETE_REQUEST_HEADERS': {
                'Host': 'glacial-earth-31542.herokuapp.com',
                'Connection': 'keep-alive',
                'Origin': 'https://glacial-earth-31542.herokuapp.com',
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.132 Chrome/80.0.3987.132 Safari/537.36',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Accept': 'text/html; q=1.0, */*',
                'Sec-Fetch-Dest': 'empty',
                'X-Requested-With': 'XMLHttpRequest',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'cors',
                'Referer': '',  # expects the url of the posting resource here!
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-US,en;q=0.9,fi;q=0.8',
                'Cookie': 'csrftoken=RHyE3NK61KZ3moRSwU27V39doEwRonc1F96Grq7MjsuqhSOY1LjGvVD9pQItGqgw',
            },
        },
        'INCOMPLETE_TARGET_POSTINGS': [
            {'title': 'Posting 1', 'content': 'Posting 1 content'},
            {'title': 'Posting 2', 'content': 'Posting 2 content'},
            {'title': 'Posting 3', 'content': 'Posting 3 content'},
        ],
        'NULL_TITLE_POSTING': {
            'content': 'only has content, but no title'
        },
        'NULL_CONTENT_POSTING': {
	        "title": "Null Content Posting"
        },
        'NULL_TITLE_NULL_CONTENT_POSTING': {

        },
        'OVERWRITTEN_TITLE': 'Overwritten title',
        'OVERWRITTEN_CONTENT': 'Overwritten content',
        'POSTINGS_URI': '/api/postings/',
        'INVALID_POSTINGS_URI': '/api/invalid/uri',
    }
    return variables



