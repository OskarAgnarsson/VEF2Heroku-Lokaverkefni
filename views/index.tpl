<!DOCTYPE html>
<html>
<head>
	<title>Lokaverkefni</title>
	<link rel="stylesheet" type="text/css" href="../static/style.css">
	<script src="https://cloud.tinymce.com/stable/tinymce.min.js"></script>
  	<script>tinymce.init({ selector:'textarea' });</script>
</head>
<body>
	<header>
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
					textPreview1<a href="/">...</a>
				</p>
			</div>
			<div class="eftirAdal">
				<div class="secondary">
					<a href="/frett{{result[1][0]}}"><h1 class="minniTitill">{{result[1][1]}}</h1></a>
					<p class="preview">
						textPreview2<a href="/">...</a>
					</p>
				</div>
				<div class="tertiary">
					<a href="/frett{{result[2][0]}}"><h1 class="minniTitill">{{result[2][1]}}</h1></a>
					<p class="preview">
						textPreview3<a href="/">...</a>
					</p>
				</div>
			</div>
		</section>
		<section class="sidebar">
			<div>
				<h1>kool</h1>
			</div>
			<div>
				<h1>kool</h1>
			</div>
			<div>
				<h1>kool</h1>
			</div>
			<div>
				<h1>kool</h1>
			</div>
		</section>
	</section>
</body>
</html>