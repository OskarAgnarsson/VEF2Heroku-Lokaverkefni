<!DOCTYPE html>
<html>
<head>
	<title>Lokaverkefni</title>
	<link rel="stylesheet" type="text/css" href="../static/style.css">
	<script src="https://cloud.tinymce.com/stable/tinymce.min.js"></script>
  	<script>tinymce.init({ selector:'textarea' });</script>
</head>
<body>
	<header class="siteHeader">
		<div class="siteTitle">
			<h1>Fréttasíða</h1>
		</div>
		<div class="skra">
			<ul>
				<li><a href="/innskra">Innskráning</a></li>
				<li><a href="/nyskra">Nýskráning</a></li>
			</ul>
		</div>
	</header>
	<section class="main">
		<section class="content">
			<div class="adalFrett">
				<a href="/frett{{result[0][0]}}"><h1 class="frettaTitill">{{result[0][1]}}</h1></a>
				<p class="preview">
					{{!result[0][2]}}<a href="/frett{{result[2][0]}}">...</a>
				</p>
			</div>
			<div class="eftirAdal">
				<div class="secondary">
					<a href="/frett{{result[1][0]}}"><h1 class="minniTitill">{{result[1][1]}}</h1></a>
					<p class="preview">
						{{!result[1][2]}}<a href="/frett{{result[2][0]}}">...</a>
					</p>
				</div>
				<div class="tertiary">
					<a href="/frett{{result[2][0]}}"><h1 class="minniTitill">{{result[2][1]}}</h1></a>
					<p class="preview">
						{{!result[2][2]}}<a href="/frett{{result[2][0]}}">...</a>
					</p>
				</div>
			</div>
			<div>
				
			</div>
		</section>
		<section class="sidebar">
			%for i in result[3:-1]:
			<div>
				<a href="/frett{{i[0]}}"><h2>{{i[1]}}</h2></a>
				<p>
					{{!i[2]}}<a href="/frett{{i[0]}}">...</a>
				</p>
			</div>
			%end
		</section>
	</section>
</body>
</html>