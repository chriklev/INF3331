INF3331 Assignment 5
Christoffer Kleven Berg (chriklev)
----------------------------------
highlighter.py:
  Highlights syntax of a codefile with a given syntax- and themefile.
  Examples of how to run:
    $ python highlighter.py python.syntax python_superior.theme highlighter.py
    $ python highlighter.py diff.syntax diff.theme diff_output.txt
----------------------------------
grep.py:
  Highlights given regular expressions in a given file.
  Exampel of how to run:
    $ python3 grep.py demofile.txt --highlight "(\b\w*um\b)" "(\b[qQ]\w*\b)"
      (^^This exampel highlights words that end with "um", and words that start
      with "q" or "Q".)
----------------------------------
diff.py:
  Finds what lines have been added or deleted in a certain file, then prints
  results to file(diff_output.txt) and terminal.
  Exampel of how to run:
    $ python3 diff.py original.txt modified.txt
