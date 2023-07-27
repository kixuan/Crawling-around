from lxml import etree

# etree.parse()解析指定路径下的HTML文件,etree.HTMLParser()是解析器，用于指定解析的类型为HTML
html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result)
print(result.decode('utf-8'))
