<script>
	const tabs = [
		{ label: "Home", href: "#" },
		{ label: "The Issue", href: "#what-is" },
		{ label: "Why It Matters", href: "#why-it-matters" },
		{ label: "The Data", href: "#data" },
		{ label: "Current Efforts", href: "#efforts" },
	];

	function handleNavClick(event, href) {
		event.preventDefault();
		if (href === "#") {
			window.scrollTo({ top: 0, behavior: "smooth" });
			setTimeout(() => {
				window.location.hash = "";
			}, 400);
		} else {
			const el = document.querySelector(href);
			if (el) {
				el.scrollIntoView({ behavior: "smooth" });
				setTimeout(() => {
					window.location.hash = href;
				}, 400);
			}
		}
	}
</script>

<header
	class="fixed top-0 left-0 w-full z-50 bg-black/40 backdrop-blur-md border-b border-white/10"
>
	<nav class="max-w-7xl mx-auto flex items-center justify-center px-6 py-4">
		<ul class="flex space-x-8">
			{#each tabs as tab}
				<li>
					<a
						href={tab.href}
						class="text-gray-300 hover:text-cyan-400 font-bold transition"
						onclick={(e) => handleNavClick(e, tab.href)}
					>
						{tab.label}
					</a>
				</li>
			{/each}
		</ul>
	</nav>
</header>
