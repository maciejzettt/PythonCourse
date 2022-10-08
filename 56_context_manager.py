

class GenHTML:

    def __init__(self):
        pass

    def __enter__(self):
        print("<html>\n\t<body>\n\t<table>")
        print(" <TR> \
                <TH>Number</TH><TH>Description</TH> \
                </TR>")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("\t</table>\n</html>")


with GenHTML():
    print("     <TR> \
                     <TD>1</TD><TD>Say hello!</TD) \
                 </TR> \
                 <TR> \
                     <TD>2</TD><TD>Say good bye!</TD) \
                 </TR>")
