
import json
import sqlite3

with open("mylibrary.json", "r", encoding="utf8") as f:
    bib = json.load(f)

db = sqlite3.connect('bibliography.sqlite')
db.row_factory = sqlite3.Row

biblio_schema = """
DROP TABLE IF EXISTS biblio;

CREATE TABLE biblio (
  citekey text UNIQUE,
  title text,
  author text,
  publication text,
  year text
);
"""

# Create table
db.executescript(biblio_schema)

def format_author(r):

    author = ""
    authors = r.get("author")

    if authors:

        # First author
        aut = authors[0]
        literal = aut.get("literal")
        family = aut.get("family")
        given = aut.get("given")
        if literal:
            author = author + literal
        else:
            if given:
                author = author + given[0] + ". "
            if family:
                author = author + family

        # Second author
        if len(authors) > 1:
            author = author + ", "
            aut = authors[1]
            literal = aut.get("literal")
            family = aut.get("family")
            given = aut.get("given")
            if literal:
                author = author + literal
            else:
                if given:
                    author = author + given[0] + ". "
                if family:
                    author = author + family

            # Rest of authors
            if len(authors) > 2:
                author = author + " et al"

    return author

pubs = set()

def format_publication(r):

    pt = r.get("type")
    pubs.add(pt)

    if pt == "book" or pt == "chapter":
        return r.get("publisher", "")
    if pt == "paper-conference":
        return r.get("publisher", "")
    if pt == "article":
        return r.get("publisher", "")
    if pt == "article-journal":
        return r.get("container-title", "")
    if pt == "thesis":
        return r.get("publisher", "")
    if pt == "report":
        p = r.get("publisher", "")
        if p:
            return p
        else:
            return r.get("collection-title", "")
        

def format_date(r):
    issued = r.get("issued")
    if issued:
        date = issued.get("date-parts")[0]
        year = date[0]
        return str(year)
        

with db:
    for r in bib:
        id = r["id"]
        title = r["title"]
        author = format_author(r)
        publication = format_publication(r)
        year = format_date(r)

        line = author + ', "' + title + '"'
        if publication:
            line = line + ", " + publication
        if year:
            line = line + ", " + year
        line = line + "."
        print(f"{line}\n")

        db.execute(
            'INSERT INTO biblio (citekey, title, author, publication, year) VALUES (?, ?, ?, ?, ?)',
            (id, title, author, publication, year)
        )

