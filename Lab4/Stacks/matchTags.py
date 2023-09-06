def is_valid_html(html):
    stack = []
    i = 0

    while i < len(html):
        if html[i] == '<':
            if html[i + 1] == '/':
                # Closing tag
                i += 2
                end = i
                while i < len(html) and html[i] != '>':
                    i += 1
                tag = html[end:i]
                if not stack or stack.pop() != tag:
                    return False
            else:
                # Opening tag
                i += 1
                end = i
                while i < len(html) and html[i] != '>':
                    i += 1
                tag = html[end:i]
                stack.append(tag)
        else:
            i += 1

    return len(stack) == 0

# Example usage:
html = "<html><body><p>Hello</p></body></html>"
assert(is_valid_html(html)==True)
