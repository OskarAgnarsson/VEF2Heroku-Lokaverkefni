<!DOCTYPE html>
<html>
<head>
	<title>Ritstjórasvæði</title>
	<link rel="stylesheet" type="text/css" href="../static/style.css">
	<script src="https://cloud.tinymce.com/stable/tinymce.min.js"></script>
  	<script>tinymce.init({ selector:'textarea' });</script>
</head>
<body>
	<header class="ritHeader">
		<h1>Ritstjórasvæði {{u}}</h1>
	</header>
	<section class="innskra">
		<h2>Ný Frétt</h2>

		<form method="POST" action="/nyfrett" accept-charset="ISO-8859-1">
			Titill:
			<br>
			<input type="text" name="titill" required>
			<br>
			Texti:
			<br>
			<textarea name="frett"></textarea>
			<br>
			<label>
				Höfundur:
				{{u}}
				<input type="radio" name="hof" value="{{u}}" required>
			</label>
			<br>
			<input type="submit" name="submit">
		</form>

		<h2>Breyta Frétt</h2>

		<form method="POST" action="/breytafrett" accept-charset="ISO-8859-1">
			<label>
				Höfundur:
				{{u}}
				<input type="radio" name="hof" value="{{u}}" required>
			</label>
			<br>
			<input type="submit">
		</form>
	</section>

	<footer>
		<a href="/">Logout</a>
	</footer>


</body>
</html>