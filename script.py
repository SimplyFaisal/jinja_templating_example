from jinja2 import Template
import json



if __name__ == '__main__':
    # create a dictionary from the schema file
    schema = json.load(open('schema.json'))
    # read in the html as a string
    view = open('view.html').read()
    # convert the string view into a template that jinja can compile
    template = Template(view)
    # bind our schema object to the view
    html = template.render(schema=schema)
    # save the resultant html string to disk
    outfile = open('outfile.html', 'w')
    outfile.write(html)