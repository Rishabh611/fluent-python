import html
from collections import abc

from functools import singledispatch

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'

@htmlize.register
def _(text: str) -> str:
    content = html.escape(text).replace("\n", "<br/>\n")
    return f'<p>{content}</pre>'

@htmlize.register
def _(seq: abc.Sequence) -> str:
    inner = '<li></li>'.join(htmlize(item) for item in seq)
    return f'<ul>{inner}\n</ul>'