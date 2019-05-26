from jinja2 import Template 
import os
template = Template("""
<html>
<body>
<h1>{{ h1 }}</h1>
<h2>{{ h2 }}</h2>
  <p>
  {% for branch in branches -%}
    <ul>
      <li> {{ branch }}
      <ul>
      <li><a href="https://codership.github.io/docs/pdf/{{ branch }}/galera.pdf">PDF</a></li>
      </ul>
      </li>
    </ul>
{% endfor -%}
  </p>
  </body>
</html>
""")
docroot = os.path.join(os.getcwd(), 'docs', 'pdf') 
filename = os.path.join(os.getcwd(), 'index.html')
with open(filename, 'w') as fh:
    fh.write(template.render(
        h1 = "Welcome to Codership Github pages",
        h2 = "Codership documentation per-branch/per-type",
        branches = list(filter(lambda d: os.path.isdir(os.path.join(docroot,d)), os.listdir(docroot)))
    ))
