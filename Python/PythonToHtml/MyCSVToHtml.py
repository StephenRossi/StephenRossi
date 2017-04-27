import sys, time, math

csv = open("NamesTest.csv", "r")
html = open("NamesTestHtml.html", "w")

#print(csv.read())

html.write("<html>")
html.write("<head>")
html.write("<title>Did I does it?</title>")
html.write("</head>")
html.write("<body style='background-color: grey'>")
html.write("<center>")
html.write("<table border = 1 style='border: 1px solid blue;border-raduis:15px; color: white; Background-color: black; margin-top: 30px'>")
for i in csv:
        a = i.split(",")
        html.write("<tr>")
        for k in a:
                html.write("<td>")
                html.write(k)
                html.write("</td>")
        #print(a[0])
        html.write("</tr>")
html.write("</table>")
html.write("</center>")
html.write("</body>")
html.write("</html>")
html.close()
print(i)


