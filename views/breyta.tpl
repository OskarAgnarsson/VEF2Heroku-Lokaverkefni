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
		<div class="topid"><h4>Texti</h4></div>
	</header>
	%for i in r:
		<form class="breyta" method="post" action="/breyta">
			<label>
				<input type="text" value="{{i[0]}}">
			</label>
			<label>
				<input type="text" value="{{i[1]}}">
			</label>
			<label>
				<input type="text" value="{{i[2]}}">
			</label>
			<label>
				<input type="text" value="{{i[3]}}">
			</label>
			<br>
			<input type="submit" name="breyta" value="Breyta">
			<input type="submit" name="breyta" value="Eyda">
		</form>
	%end

	<footer>
		<a href="/">Forsíða</a>
	</footer>
</body>
</html>