from django.shortcuts import render
from csv import reader
from csv import writer
from django.views.generic import TemplateView
from markdown import markdown

def write_table(path, table):
    with open(path, 'w', newline='') as f:
        writer(f).writerows(table)

def read_table(path):
    with open(path) as f:
        return [row for row in reader(f)]
    
def print_table(table):
    for row in table:
        print(row[0], row[1], row[2])

class TableView(TemplateView):
    template_name = 'table.html'

    def get_context_data(self, **kwargs):
        path = 'numbers.csv'
        return {'table': read_table(path)}
    
def doc_data(document):
    path = Path(document)
    markdown_text = path.read_text()
    return {'html': markdown(markdown_text)}

class DocumentView(TemplateView):
    template_name = 'document.html'

    def get_context_data(self, **kwargs):
        return doc_data(self.kwargs.get('doc'))