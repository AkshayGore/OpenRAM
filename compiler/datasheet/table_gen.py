class table_gen:
    """small library of functions to generate the html tables"""

    def __init__(self, name):
        self.name = name
        self.rows = []
        self.table_id = 'data'

    def add_row(self, row):
        """add a row to table_gen object"""
        self.rows.append(row)

    def gen_table_head(self):
        """generate html table header"""
        html = ''

        html += '<thead>'
        html += '<tr>'
        for col in self.rows[0]:
            html += '<th>' + str(col) + '</th>'
        html += '</tr>'
        html += '</thead>'
        return html

    def gen_table_body(self):
        """generate html body (used after gen_table_head)"""
        html = ''

        html += '<tbody>'
        html += '<tr>'
        for row in self.rows[1:]:
            html += '<tr>'
            for col in row:
                html += '<td>' + str(col) + '</td>'
            html += '</tr>'
        html += '</tr>'
        html += '</tbody>'
        return html

    def to_html(self):
        """writes table_gen object to inline html"""
        html = ''
        html += '<table id= \"'+self.table_id+'\">'
        html += self.gen_table_head()
        html += self.gen_table_body()
        html += '</table>'

        return html
