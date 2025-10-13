---
created: 2020-09-26-Saturday 09:40
modified: 2023-03-10-Friday 23:15
---

 `.^ $ + ? * ( ) \`: characters that would need to be escaped.
`^` match from the beginning, `$` end of string.
`[ ]` character classes: matches one character from a range or series of characters. `^` inside negates (matches the inverse).
`|` separates alternative patterns (OR operator).
`(...)` starts and ends a group of regexp patterns. `(?P...)` named grouping. Eg: `(soft|hard)ware`

***Repetition Qualifiers:*** Affects the amount to match from the preceding character or group. Can have a variable or specific range.

- `*` match 0 or more occurrences of the preceding entity.
- `?` match 0 or 1 occurrence of the preceding entity.
- `+` match 1 or more occurrences of the preceding entity.
- `{n}` match exactly n occurrences of the preceding entity.
- `{n,}` match at least n occurrences of the preceding entity.
- `{n,m}` match between n & m occurrences of the preceding entity.

[[2023-02-20-Monday]] From ChatGPT
The regular expression that matches any HTML header syntax, including `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, and `<h6>`, is:

`<\s*h[1-6]\s*>.*?<\s*/\s*h[1-6]\s*>`

In this regular expression, the pattern `<\s*h[1-6]\s*>` matches the opening tag of any HTML header element, with the `h[1-6]` part matching any digit from 1 to 6. The `\s*` matches zero or more whitespace characters before or after the tag name.

The `.*?` pattern matches any number of characters, including line breaks, between the opening and closing tags of the HTML header element. The `?` character after the `.*` makes the match non-greedy, meaning it will match the shortest possible sequence of characters that satisfies the pattern.

The pattern `<\s*/\s*h[1-6]\s*>` matches the closing tag of the HTML header element, with the same tag name as the opening tag.

Here's an example code snippet that uses this regular expression to match all occurrences of any HTML header syntax in a string:

```py
import re  
my_string = "<h1>Heading 1</h1> <h2>Heading 2</h2> <h3>Heading 3</h3>"
regex_pattern = r"<\s*h[1-6]\s*>.*?<\s*/\s*h[1-6]\s*>" 
matches = re.findall(regex_pattern, my_string)  
print(matches)  # Output: ['<h1>Heading 1</h1>', '<h2>Heading 2</h2>', '<h3>Heading 3</h3>']
```

In this example, the `re.findall()` function searches the `my_string` variable for all occurrences of the regular expression pattern specified in `regex_pattern`, and returns a list of all matching substrings. The resulting output is a list containing the strings `'<h1>Heading 1</h1>'`, `'<h2>Heading 2</h2>'`, and `'<h3>Heading 3</h3>'`.
