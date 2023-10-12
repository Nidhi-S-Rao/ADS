import re

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
                while i < len(html) and (html[i].isalnum() or html[i] in ['-', '_']):
                    i += 1
                tag = html[end:i]
                #print(tag)

                # Parse attributes
                """attributes = {}
                while i < len(html) and html[i] != '>':
                    attr_match = re.match(r'\s*([a-zA-Z_][a-zA-Z0-9_-]*)\s*=\s*("([^"]*)"|\'([^\']*)\')', html[i:])
                    if attr_match:
                        attr_name, _, attr_value1, attr_value2 = attr_match.groups()
                        attr_value = attr_value1 if attr_value1 else attr_value2
                        attributes[attr_name] = attr_value
                        i += len(attr_match.group(0))
                    else:
                        i += 1"""

                stack.append(tag)
                # You can do something with the attributes if needed, e.g., print them
                #print(f"Tag: {tag}, Attributes: {attributes}")

        else:
            i += 1

    return len(stack) == 0

# Example usage:
html = '<html lang="en"><body class="container"><p>Hello</p></body></html>'
assert(is_valid_html(html))