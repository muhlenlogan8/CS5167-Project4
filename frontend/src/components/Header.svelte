<script>
	const tabs = [
		{ label: "Home", href: "#" },
		{ label: "What is Energy Inequality?", href: "#what-is-energy" },
	];
</script>

<header
	class="fixed top-0 left-0 w-full z-50 bg-black/40 backdrop-blur-md border-b border-white/10"
>
	<nav class="max-w-7xl mx-auto flex items-center justify-between px-6 py-4">
		<h1 class="text-xl font-bold tracking-wide text-gray-300">Energy Inequality</h1>

		<ul class="hidden md:flex space-x-8">
			{#each tabs as tab}
				<li>
					<a href={tab.href} class="text-gray-300 hover:text-white transition">
						{tab.label}
					</a>
				</li>
			{/each}
		</ul>
	</nav>
</header>