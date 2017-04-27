def writeIt():
    HTML_str = """
        <center>
        <table border=1 style="margin-top: 180px">
           <tr>
               <th> Name </th>
               <th> Age </th>
           </tr>
           <tr>
               <td> Steve </td>
               <td> 16 </td>
           </tr>
           <tr>
               <td> Abby </td>
               <td> 16 </td>
           </tr>
           <tr>
               <td> Joey </td>
               <td> 15 </td>
           </tr>
        </table>
        <center>
    """

    htmlFile = open("WriteNameTable.html", 'w')
    htmlFile.write(HTML_str)
    htmlFile.close()
    print("File Created!")

writeIt()
