import re

def convert_to_html(md_file):
    try:
        with open(md_file, 'r') as infile:
            lines = infile.readlines()
            file_name = infile.name[:-3]
        
        converted_lines = []
        for line in lines:
            line = convert_heading(line)
            line = convert_bold_and_italic(line)
            line = convert_links(line)
            converted_lines.append(line)
        converted_lines = convert_lists(converted_lines)

        html = "<html>\n<body>\n" + "\n".join(converted_lines) + "\n</body>\n</html>"

        try:
            file = open("out/" + file_name + '.html', "x")
            file.write(html);
        except:
            with open("out/" + file_name + '.html', "w") as outfile:
                outfile.seek(0)
                outfile.write(html)
                outfile.truncate()
    except:
        print(f'Error: File "{md_file}" was not found')

def convert_heading(line):
    match = re.match(r'^(#{1,6})\s+(.*)', line)
    if match:
        level = len(match.group(1))
        content = match.group(2)
        return fr"<h{level}>{content}</h{level}>"
    return line

def convert_bold_and_italic(line):
    line = re.sub(r'\*\*(\S.*\S)\*\*', r'<strong>\1</strong>', line)
    line = re.sub(r'__(\S.*\S)__', r'<strong>\1</strong>', line)

    line = re.sub(r'\*(\S.*\S)\*', r'<em>\1</em>', line)
    line = re.sub(r'_(\S.*\S)_', r'<em>\1</em>', line)
    return line

def convert_links(line):
    line = re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', line)
    return line

def convert_lists(lines):
    html_lines = []
    in_ul = False
    in_ol = False

    for line in lines:
        if re.match(r'^\s*-\s+.*', line):
            if not in_ul:
                html_lines.append('<ul>')
                in_ul = True
            html_lines.append(f'<li>{line.strip()[2:]}</li>')
        elif re.match(r'^\s*\d+\.\s+.*', line):
            if not in_ol:
                html_lines.append('<ol>')
                in_ol = True
            html_lines.append(f'<li>{line.strip()[3:]}</li>')
        else:
            if in_ul:
                html_lines.append('</ul>')
                in_ul = False
            if in_ol:
                html_lines.append('</ol>')
                in_ol = False
            html_lines.append(line)

    if in_ul:
        html_lines.append('</ul>')
    if in_ol:
        html_lines.append('</ol>')

    return html_lines
