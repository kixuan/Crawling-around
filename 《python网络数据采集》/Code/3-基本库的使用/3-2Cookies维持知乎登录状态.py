import requests

headers = {
    'Cookie': '_zap=86399ee0-964c-4544-a2d5-38d5668eb9cd; d_c0=ABAYc3r_4xaPTsCxngEFhpm6lUFccQn4Fwk=|1686037806; YD00517437729195:WM_TID=tE7LcwHWN0FEARFBRELALoyEAYBR2mRv; _xsrf=ewXay5Y7V43b719jjVL9CWQ9yQXMZu9g; captcha_session_v2=2|1:0|10:1686485481|18:captcha_session_v2|88:cWpOSFFhOWIrMzZ1bjhGU0RrUTRXbitQZlcrQjZTNnhBOFc3aXdjTWMrTGdQdHVpZWxsTkhVaE9sOHRCU0IvWg==|ffd733983c3bb2a1ec473385408fc2447d2b0446405a407d5c8a149bb841e803; __snaker__id=183V9zKLONIYeNg7; gdxidpyhxdE=iU4sUaQqDUKCWXVKTnTPGh7mKa8II41w1rYz\8gDm3GinmutI5L3iGghRckRVhvsz4IviipLv6CnA5EMhmclPBVbOOM67bgOa61exeTsxGXdu2Y4x/nB+XaBGsXGBS\twIT8SY3usvZgMWqiBUJmLbG6sonIfZE5xUioAQsVYJhhtYSb:1686486380545; YD00517437729195:WM_NI=CG78HCBCY0ckB2wgvz4+HBqOQzq1Oc03CFP1+f36hdOa33k5KFRDQkzPAkQX60jbvwgJF7TgHjVgeLJ1Td/pQDWok2c2UMOyoTCsJ6Z6ZDbLAA1C0r1OFejsSmTgZDsDRVY=; YD00517437729195:WM_NIKE=9ca17ae2e6ffcda170e2e6eea7b748bc94e1b8fc59b08e8fa6c85e929a9ab0d53ca1b2adbaf474bc8bfcadd52af0fea7c3b92a8199f9d9cb49829d97d1e26182eeb988f572f8f588a3f44593a6bfd2ce69f4ed8da7d33be9bafdd7eb708dbffdd4ea3f899a9ea5d461ba908f8cd454f6f0a683f57da5968ad8d76d8cb69a88e8488aef9c85ae7c939c9990ea3aa1ee9baece73ad8c8d94c93e9aea96a5e148839fffa4b37af3918a86e97991b39c88d950b19c9eb7dc37e2a3; q_c1=deea4d7296144e1e833c5992451e1415|1686485499000|1686485499000; z_c0=2|1:0|10:1686500893|4:z_c0|92:Mi4xMngwTkR3QUFBQUFBRUJoemV2X2pGaGNBQUFCZ0FsVk4tZ2R6WlFERGNYLVlqczRqcmFHcmdvNlBZU0ZweEZKNTVR|a32388999697fcc357861859e519e37ba5c4dbc3f914924c332b67ffa8c54f2f; tst=r; SESSIONID=9dLsXkTdIP8hG74IiLekxRI7HyfaDV8QW8SB5dwqgQO; KLBRSID=81978cf28cf03c58e07f705c156aa833|1686556769|1686556764',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)