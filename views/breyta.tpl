<!DOCTYPE html>
<html>
<head>
	<title>Breyta frétt</title>
	<link rel="stylesheet" type="text/css" href="../static/style.css">
	<script src="https://cloud.tinymce.com/stable/tinymce.min.js"></script>
  	<script>tinymce.init({ selector:'textarea' });</script>
</head>
</head>
<body>
	<header class="top">
		<div class="topid"><h4>Frett_ID</h4></div>
		<div class="topid"><h4>Rit_ID</h4></div>
		<div class="topid"><h4>Titill</h4></div>
	</header>
	%for i in r:
		<form method="post" action="/breyta">
			<div class="breyta">
				<label>
					{{i[0]}}
					<input type="radio" name="f" value="{{i[0]}}" required>
				</label>
				<label>
					<input type="text" name="r" value="{{i[1]}}">
				</label>
				<label>
					<input type="text" name="ti" value="{{i[2]}}">
				</label>
			</div>
			<h4>Texti</h4>
			<label>
				<textarea name="te">
					{{i[3]}}
				</textarea>
			</label>
			<br>
			<input type="submit" name="breyta" value="Breyta">
			<input type="submit" name="breyta" value="Eyða">
		</form>
	%end

	<footer>
		<a href="/">Forsíða</a>
	</footer>
</body>
</html>