import codecs
import re


def delete_html_tags(html_file, result_file="cleaned.txt"):
    # Read file
    with codecs.open(html_file, "r", "utf-8") as file:
        html = file.read()

    # Delete HTML-tag
    clean_text = re.sub(r"<[^>]+>", "", html)

    # Remove rows that have no information
    non_empty_lines = [line.strip() for line in clean_text.splitlines() if line.strip()]
    clean_text = "\n".join(non_empty_lines)

    # Write cleaned text to file
    with codecs.open(result_file, "w", "utf-8") as file:
        file.write(clean_text)


delete_html_tags("draft.html", "cleaned.txt")
