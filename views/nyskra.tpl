<!DOCTYPE html>
<html>
<head>
	<title>Nýskráning</title>
	<link rel="stylesheet" type="text/css" href="../static/style.css">
	<script src="https://cloud.tinymce.com/stable/tinymce.min.js"></script>
  	<script>tinymce.init({ selector:'textarea' });</script>
</head>
<body>
	<header>
		<h1>Nýskráning</h1>
	</header>
	<section>
		<form method="post" action="/donyskra" accept-charset="ISO-8859-1">
			<label>
				Nafn:
				<br>
				<input type="text" name="nafn">
			</label>
			<br>
			<label>
				Notandanafn:
				<br>
				<input type="text" name="user">
			</label>
			<br>
			<label>
				Lykilorð:
				<br>
				<input type="text" name="pass">
			</label>
			<label>
				<input type="submit" name="innskra">
			</label>
		</form>
	</section>
</body>
</html>