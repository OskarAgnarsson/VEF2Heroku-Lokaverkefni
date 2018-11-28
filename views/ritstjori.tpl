<!DOCTYPE html>
<html>
<head>
	<title>Ritstjórasvæði</title>
	<link rel="stylesheet" type="text/css" href="../static/style.css">
	<script src="https://cloud.tinymce.com/stable/tinymce.min.js"></script>
  	<script>tinymce.init({ selector:'textarea' });</script>
</head>
<body>
	<h1>Halló {{u}}</h1>

	<h2>Ný Frétt</h2>

	<form method="post" action="/postfrett" accept-charset="ISO-8859-1">
		<label>
			Titill:
			<br>
			<input type="text" name="titill" required>
		</label>
		<br>
		Texti:
		<br>
		<textarea name="frett" required></textarea>
		<br>
		Höfundur:
		{{u}}
		<input type="radio" name="hof" value="{{u}}" required>
		<br>
		<input type="submit" name="submit" value="post">
	</form>

	<h2>Breyta Frétt</h2>

	<form method="post" action="/breytafrett" accept-charset="ISO-8859-1">
		<input type="radio" name="hof" value="{{u}}" required>
		<br>
		<input type="submit">
	</form>

	<footer>
		<a href="/">Logout</a>
	</footer>


</body>
</html>