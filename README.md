# Markdown to HTML Converter

A simple program for converting a Mardown File to HTML.

## Features

- Headings
- Bold and Italic
- Links
- Lists
  - Unordered lists
  - Ordered lists
  - (No subitems)

## Requirements

- **Python 3.x**

## Usage

1. **Clone Repository**

```
git clone https://github.com/Fleacon/MDtoHTML.git
```

2. **Place Markdown file in the project folder**

3. **Run the script**

```
python main.py
```

4. **Input relative path**

```
Enter the Markdown file path: <relative path>
```

5. **Output in the out folder**

## Example

### Input (Markdown)

```Markdown
# Heading 1

## Heading 2

### Heading 3

This is **bold text** and this is _italic text_.

Here is a [link](https://example.com).

- Item 1
- Item 2
  - Subitem 1
  - Subitem 2

1. Step 1
2. Step 2
```

### Output (HTML)

```HTML
<html>
<body>
<h1>Heading 1</h1>


<h2>Heading 2</h2>


<h3>Heading 3</h3>


This is <strong>bold text</strong> and this is <em>italic text</em>.



Here is a <a href="https://example.com">link</a>.



<ul>
<li>Item 1</li>
<li>Item 2</li>
<li>Subitem 1</li>
<li>Subitem 2</li>
</ul>


<ol>
<li>Step 1</li>
<li>Step 2</li>
</ol>
</body>
</html>
```
