<html>
<head>
    <style type="text/css">
        ${css}
    </style>
</head>
<body>

	%for tes in customer_text():
		<table>
			<td>
				<tr>${tes['field1']}</td>
				<tr>${tes['field2']}</td>
			</td>
		</table>
	%endfor

	
</body>
</html>
